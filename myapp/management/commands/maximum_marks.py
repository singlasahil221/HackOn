from django.core.management.base import BaseCommand
from myapp.models import Question


class Command(BaseCommand):
	help = 'Update maximum_marks of the questions.'

	def add_arguments(self, parser):
		parser.add_argument('marks', type=int, help='Indicates the maximum_marks of the question')
		#optional argument
		parser.add_argument('-p', '--id', type=int, help='Indicates the id of the question')

	def handle(self, *args, **kwargs):
		question_id, marks = None,None
		if 'marks' in kwargs:
			marks = kwargs['marks']
		if 'id' in kwargs:
			question_id = kwargs['id']
		if question_id : 
			question_obj = Question.objects.get(id = question_id)
			question_obj.maximum_marks = marks
			question_obj.save()
			print("Done")
		else:
			question_obj = Question.objects.all()
			for i in question_obj:
				i.maximum_marks = marks
				i.save()
			print("Done")


