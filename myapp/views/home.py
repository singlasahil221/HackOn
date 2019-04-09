from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from myapp.models.schema_file import *





# -------   Home   ------- #


def Home(request):
	return render(request, 'home.html', {})



# --------    LeaderBoard    -------- #


def Leaderboard(request):
	all_user = UserProfile.objects.all().exclude(user__is_superuser = True)
	#print(all_user)
	return render(request, 'leaderboard.html', {'users':all_user})



# -------    Developers     ------- #



def Developers(request):
	return render(request, 'developers.html',{})


def rules(request):
	return render(request,'rules.html',{})