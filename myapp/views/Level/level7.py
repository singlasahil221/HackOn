from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from myapp.models.schema_file import *



def solve7(time, submitted_answer, original_answer):
	if time == '':
		return False
	if time == '0' or int(time) > 10 :
		return False;
	return submitted_answer == 'across, after, among, any, are, because, but, can, cannot, could, did, either, else, ever, every, from, get, got, had, his, how, into, likely, must, not, off, other, own, rather, said, say, says, she, than, the, their, then, there, this, wants, was, was, what, when, where, while, will, with, yet, you'