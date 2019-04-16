from django.db import models
from myapp.models.base import BaseModel
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from uuid import uuid4
"""
Winner will be declare on the basis of following :
	1. Maximum Scoring contestent
	2. Minimum Time Consumer
	3. Minimum Wrong attempts

"""


def _generate_unique_uri():
    """Generates a unique uri for the chat session."""
    return str(uuid4()).replace('-', '')[:15]



#LeaderBoard
class UserProfile(BaseModel):
	total_wrong_attempts 		= 	models.PositiveIntegerField(default = 0)
	total_time_taken 		= 	models.DurationField(default = timedelta)
	total_score 			= 	models.PositiveIntegerField(default = 0)
	user 				= 	models.OneToOneField(User, on_delete = models.CASCADE)
	# for directly arranging the leaderboard

	class Meta:
		ordering = ['-total_score', 'total_time_taken', 'total_wrong_attempts']
		
	def __str__(self): 
		return self.user.username 



#question_bank
class Question(BaseModel):
	status_choices 	= 	(
				("LOCKED","locked"),
				("UNLOCKED","unlocked"),
				("HIDDEN","hidden"),
				)

	level 			= 	models.PositiveIntegerField(default = 1)
	question_id 		= 	models.CharField(max_length = 100,default=_generate_unique_uri)
	title 			= 	models.CharField(max_length = 100)
	statement 		= 	models.TextField(max_length = 10000)
	answer			=	models.CharField(max_length = 1000)
	maximum_marks 		= 	models.IntegerField(default = 500)
	minimum_marks 		=   	models.IntegerField(default = 0)
	status			= 	models.CharField(max_length = 20, choices = status_choices)

	class Meta: 
		ordering = ['level','created_at']

	def __str__(self):
		return self.title



#Keep Data of which question alloted to which user at any particular level and scoring 
class UserQuestion(BaseModel):
	user 			= 	models.ForeignKey(UserProfile, on_delete = models.CASCADE)
	level 			= 	models.PositiveIntegerField(default = 1)
	question		= 	models.ForeignKey(Question, on_delete = models.CASCADE)       #question can be different on the same level
	wrong_attempts		=	models.PositiveIntegerField(default = 0)    
	marks_obtained		= 	models.PositiveIntegerField(default = 0)
	time_taken		= 	models.DurationField(default = timedelta)

	"""
	time_taken will be time between the user made the first submission and the user get his first AC 
	time_taken = last_updated_at - created_at;
	mark_obtained field to get the marks obtained in every question the user get PS : it should not be updated after creation
	"""

	class Meta:
		ordering 	= 	['level']

	def __str__(self):
		return "Level " + str(self.level)



# For logging of the users
class UserSubmission(BaseModel):
	status_choices 	=	(
				("AC","accepted"),
				("WA", "wrong")
				)

	user 			= 	models.ForeignKey(UserProfile,on_delete = models.CASCADE)
	question		=   	models.ForeignKey(Question, on_delete = models.CASCADE)
	answer 			=	models.CharField(max_length = 1000)
	status 			= 	models.CharField(max_length = 100, choices = status_choices)
	marks 			= 	models.PositiveIntegerField(default = 0)
	class Meta:
		ordering    =  ["-created_at"]

	def __str__(self):
		return "Answer of : " + self.user.user.username




