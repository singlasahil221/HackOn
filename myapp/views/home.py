from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from myapp.models.question import *





# -------   Home   ------- #


def Home(request):
	return render(request, 'home.html', {})



# --------    LeaderBoard    -------- #


def Leaderboard(request):
	all_user = UserProfile.objects.all()
	print(all_user)
	return render(request, 'leaderboard.html', {'users':all_user})



# -------    Developers     ------- #



def Developers(request):
	return render(request, 'developers.html',{})


