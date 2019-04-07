from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from myapp.models.schema_file import *




def solution1(user_question_obj, dict_obj):
	username = dict_obj('username','')
	password = dict_obj('password','')
	if username and username == '' and password and password == '':
		return True
	return False