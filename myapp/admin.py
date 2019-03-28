from django.contrib import admin
from admin_auto_filters.filters import AutocompleteFilter
# Register your models here.
from django.contrib.auth.models import User

from myapp.models import (
	UserProfile,
	Question,
	UserSubmission,
	UserQuestion
	)


#dropdown filters
class UserFilter(AutocompleteFilter):
	title = 'User'
	field_name = 'user'


class QuestionFilter(AutocompleteFilter):
	title = 'Question'
	field_name = 'question'





#Admin Logs
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id','username','total_score','total_time_taken','total_wrong_attempts')

	search_fields = (
		'user__username',
		)

	list_filter = [UserFilter]
	class Media:
		js = []


	def username(self, obj):
		return obj.user.username



class QuestionAdmin(admin.ModelAdmin):
	list_display 	= ('question_id','level','title','maximum_marks', 'minimum_marks')
	list_filter = (
		'level',
		)
	search_fields = (
		'title',
		)

#Logs
class UserSubmissionAdmin(admin.ModelAdmin):
	list_display = ('id', 'username', 'level', 'question', 'answer', 'status', 'marks')
	
	list_filter = (
		'status',
		'question__level',
		'question__title',
		)

	list_filter = [UserFilter, QuestionFilter, 'status','question__level',]
	class Media:
		js = []

	def username(self, obj):
		return obj.user.user.username

	def level(self,obj):
		return obj.question.level



class UserQuestionAdmin(admin.ModelAdmin):
	list_display = ('id', 'username', 'question', 'wrong_attempts', 'time_taken', 'marks_obtained')
	search_fields = (
		'user__user__username',
		)
	
	list_filter = [UserFilter, QuestionFilter]
	class Media:
		js = []

	def username(self, obj):
		return obj.user.user.username


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(UserSubmission, UserSubmissionAdmin)
admin.site.register(UserQuestion, UserQuestionAdmin)