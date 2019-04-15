from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, FileResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from myapp.models.schema_file import *
from myapp.serializers.modelsSerializers import *
from datetime import datetime, timedelta
import pytz
import json
from myapp.views.Level import *
from hackon import settings
utc=pytz.UTC
import os


@login_required
def tasks(request):
	try:
		user_profile_obj = UserProfile.objects.get(user=request.user)

	except ObjectDoesNotExist:
		user_profile_obj = UserProfile(user = request.user)
		user_profile_obj.save()

	all_taks_status = Question.objects.all().values('level','title','status','maximum_marks').distinct('level')
	n_hacked_tasks = UserQuestion.objects.filter(user=user_profile_obj, marks_obtained__gt = 0)
	n_hacked = n_hacked_tasks.values_list('level',flat=True)
	hacked_tasks = n_hacked_tasks.values('question')
	hacked_tasks = Question.objects.filter(pk__in = hacked_tasks).values('level','title','status','maximum_marks').distinct('level')
	return render(request, 'all_tasks.html', {'task':all_taks_status,'hacked_tasks':n_hacked_tasks, 'hacked':n_hacked})



# ------------ admin --------------- #
# @login_required
# def get_question(request, id):
# 	print("ha")
# 	if request.method == 'GET':
# 		message = 'Server Error'
# 		level = id
# 		if request.user.is_superuser :
# 			question = Question.objects.get(question_id = id)
# 			profile = UserProfile.objects.get(user = request.user)
# 			user_question_obj = UserQuestion.objects.create(user = profile, question = question, level = question.level)
# 			user_question_obj.save()
# 			print(user_question_obj)
# 			serializers = UserQuestionSerializer(user_question_obj)
# 			user_question_obj = serializers.data
# 			return render(request,"task.html",{'question' : user_question_obj,'message' : message,'level':question.level})
# 		return HttpResponse(message)








# -------     alot question to the user     -------- #

@login_required
def solve_question(request, level):
	if request.method == 'GET':
		message = "Unlocked!"
		user_question_obj = None
		#check if user profile already exists
		try:
			user_profile_obj = UserProfile.objects.get(user=request.user)

		except ObjectDoesNotExist:
			user_profile_obj = UserProfile(user = request.user)
			user_profile_obj.save()

		# if user is already alotted a question on that level
		try:
			user_question_obj = UserQuestion.objects.get(user = user_profile_obj, level = level)

		#alot a question to the user for that level
		except ObjectDoesNotExist:
			try:
				queryset = Question.objects.filter(level = level)
				if( queryset[0].status == 'UNLOCKED'):
					mod_value = len(queryset)
					index = UserQuestion.objects.filter(level = level).count() % mod_value
					user_question_obj = UserQuestion.objects.create(user = user_profile_obj, level = level, question = queryset[index])
					user_question_obj.save()
				#if level is locked return the message  = locked	
				else:
					message = "Locked"
			except IndexError:
				message = "Locked"
		serializers = UserQuestionSerializer(user_question_obj)
		user_question_obj = serializers.data
		return render(request,"task.html",{'question' : user_question_obj,'message' : message,'level':level})
		#return JsonResponse({'question' : user_question_obj,'message' : message})



	# ------- Answer Submission   ------- #

	if request.method == 'POST':

		message = "Submitted"
		user_submission_obj = None
		user_question_obj = None
		#check if question is unlocked and alotted to the user
		try:
			user_obj = request.user
			user_profile_obj = UserProfile.objects.get(user = user_obj)
			user_question_obj = UserQuestion.objects.get(user = user_profile_obj, level = level, question__status = "UNLOCKED")
			question_obj = user_question_obj.question
			answer = request.POST.get('answer','')
			time = request.POST.get('time','')
			print(time)
			# solution_func = "solution"+str(user_question_obj.question.question_id)
			# response = eval(solution_func)(user_question_obj,request.POST)
			if(level == '1'):
				response = (len(answer) == 13)
			elif level == "8":
				response = solve7(time, answer, question_obj.answer)
				
			elif level == '9':
				if user_question_obj.wrong_attempts == 5:
					response = True
				else:
					response = False
			else:
				response = (answer == question_obj.answer)
			#answer = lower(answer)
			user_submission_obj = UserSubmission(user = user_profile_obj, question = question_obj, answer = answer)
			#check if user already submitted the correct answer, then it will not affect other models and answer will not be considered for marking
			if user_question_obj.marks_obtained == 0:

				if response == True:  #if solution is correct

					marks_obtained = max(0,question_obj.maximum_marks - user_question_obj.wrong_attempts)

					#update user submission table for logs
					user_submission_obj.status = "AC"
					user_submission_obj.marks = marks_obtained

					#update user question table for user individual marks maintainance
					user_question_obj.marks_obtained = marks_obtained
					user_question_obj.time_taken = datetime.now().replace(tzinfo=None) - user_question_obj.question.updated_at.replace(tzinfo=None)

					#update total profile score
					#user_profile_obj.total_score += marks_obtained
					#user_profile_obj.total_time_taken += user_question_obj.time_taken
					#user_profile_obj.total_wrong_attempts += user_question_obj.wrong_attempts


					#update maximum marks of the question on the correct submission
					question_obj.maximum_marks = max(question_obj.maximum_marks-5, question_obj.minimum_marks)

				#mark the entry in log table, and increase wront answer count
				else:

					user_submission_obj.status = "WA"
					user_question_obj.wrong_attempts += 1

			#for already submitted question, the answer will be only recorded in the logs table
			else:
				message = "Already Submitted!"
				if response == True:
					user_submission_obj.status = "AC"
					user_submission_obj.marks = user_question_obj.marks_obtained

				else:
					user_submission_obj.status = "WA"
			user_profile_obj.save()
			user_submission_obj.save()
			user_question_obj.save()
			question_obj.save()
			serializers = UserQuestionSerializer(user_question_obj)
			user_question_obj = serializers.data
		except ObjectDoesNotExist:
			message = "Can not Submit!"
		return render(request,"task.html",{'question' : user_question_obj,'message' : user_submission_obj.status,'level':level})

		#return JsonResponse({"message" : message, "status" : user_submission_obj.status})

	if request.method == 'PUT':
		return HttpResponse("Server Error")





def download_file(request, filename):
	if os.path.exists(settings.STATIC_ROOT + '/assets1/'+filename):
		with open(settings.STATIC_ROOT + '/assets1/'+filename, 'rb+') as fh:
			response = HttpResponse(fh.read(), content_type="application/force-download")
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(settings.STATIC_ROOT + '/assets1/'+filename)
			return response
	return HttpResponse("Server Error")
