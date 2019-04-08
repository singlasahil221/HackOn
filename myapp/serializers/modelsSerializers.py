from rest_framework import serializers
from myapp.models.schema_file import *



class UserProfileSerializer(serializers.ModelSerializer):
	user__username  	 = serializers.CharField(source='user.username')

	class Meta:
		model 			 = UserProfile
		fields 			 = ('id','user__username', 'total_score', 'total_time_taken')




class UserQuestionSerializer(serializers.ModelSerializer):
	question__title  	 = serializers.CharField(source='question.title')
	question__statement  = serializers.CharField(source='question.statement')
	question__maximum_marks  = serializers.IntegerField(source='question.maximum_marks')
	question__id = serializers.CharField(source='question.question_id')

	class Meta:
		model 			 = UserQuestion
		fields 			 = ('id', 'level','wrong_attempts', 'marks_obtained', 'question__title', 'question__statement','question__maximum_marks','question__id')




class UserSubmissionSerializer(serializers.ModelSerializer):
	question__title  	 = serializers.CharField(source='question.title')
	question__level 	 = serializers.CharField(source='question.level')
	user__username  	 = serializers.CharField(source='user.username')

	class Meta:
		model 			 = UserSubmission
		fields 			 = ('id', 'user__username', 'question__level', 'question__title', 'answer', 'status', 'marks', 'created_at')




class QuestionSerializer(serializers.ModelSerializer):

	class Meta:
		model 			 = Question
		fields 			 = ('id', 'title', 'statement', 'maximum_marks', 'status')