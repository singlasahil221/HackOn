from django.core.management.base import BaseCommand
from myapp.models import UserSubmission, UserQuestion, Question, UserProfile
from django.contrib.auth.models import User

class Command(BaseCommand):
	help = 'reduge submission of the questions.'

	def handle(self, *args, **kwargs):
		unlocked_question = Question.objects.filter(status = "UNLOCKED")
		for user in UserProfile.objects.all():
			user_question_obj = UserQuestion.objects.filter(user = user)
			print("User : ", user.user.username)
			for obj_instance in user_question_obj:
				submission_time = user.usersubmission_set.filter(question = obj_instance.question,status="AC")[0].created_at
				creation_time   =  obj_instance.question.updated_at
				print("Question :", obj_instance.question.title, "start time :",submission_time ,creation_time)
