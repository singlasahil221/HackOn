from django.contrib import admin

# Register your models here.

from myapp.models import (
	UserProfile,
	Question,
	UserSubmission,
	UserQuestion
	)


#Admin Logs
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id','username','total_score','total_time_taken','total_wrong_attempts')
	

	def username(self, obj):
		return obj.user.username


class QuestionAdmin(admin.ModelAdmin):
	list_display 	= ('question_id','level','title','maximum_marks', 'minimum_marks')


#Logs
class UserSubmissioAdmin(admin.ModelAdmin):
	list_display = ('id', 'username', 'question', 'answer', 'status', 'marks')

	def username(self, obj):
		return obj.user.user.username


class UserQuestionAdmin(admin.ModelAdmin):
	list_display = ('id', 'username', 'question', 'wrong_attempts', 'time_taken', 'marks_obtained')

	def username(self, obj):
		return obj.user.user.username


admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(UserSubmission, UserSubmissioAdmin)
admin.site.register(UserQuestion, UserQuestionAdmin)