from django.core.management.base import BaseCommand
from myapp.models import Question


class Command(BaseCommand):
	help = 'Unlock the levels.'

	def add_arguments(self, parser):
		parser.add_argument('level', type=int, help='Indicates the level of the question to be locked')

	def handle(self, *args, **kwargs):
		level = kwargs['level']
		question_obj = Question.objects.filter(level__lte = level)
		for i in question_obj:
			i.status = 'LOCKED'
			i.save()
		self.stdout.write(self.style.SUCCESS("Done"))
		self.stdout.write(self.style.WARNING("Done"))
		self.stdout.write("Done")