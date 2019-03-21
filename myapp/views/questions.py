from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from myapp.models.question import *




@login_required
def Tasks(request):
	all_taks_status = Question.objects.all().values('level','status').distinct()
	return render(request, 'questions.html', {'task':all_taks_status})



@login_required
def question(request):
	return render(request, 'question.html', {})



# -------     alot question to the user     -------- #
@login_required
def Fetch_Question(request, level):
	message = "Unlocked"
	QuestionObject = None

	# if user is already alotted a question on that level
	try:
		QuestionObject = UserQuestion.objects.get(user = request.user, level = level)


	#alot a question to the user for that level
	except ObjectDoesNotExist:
		queryset = Question.objects.filter(level = level)
		if(queryset[0].status == 'UNLOCKED'):
			mod_value = max(1,level-2)
			index = UserQuestion.objects.filter(level = level).count() % mod_value
			QuestionObject = UserQuestion.objects.create(user = request.user, level = level, question = queryset[index])
			QuestionObject.save()

		#if level is locked return the message  = locked	
		else:
			message = "Level Locked"

	return JsonResponse({'question' : QuestionObject,'message' : message})

