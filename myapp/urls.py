"""hackon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.contrib import admin
from django.urls import path, include, re_path
from myapp.views.home import *
from myapp.views.question_views import *

urlpatterns = [
    path('', Home),
    path('rules/',rules),
    path('leaderboard/',Leaderboard),
    path('developers/', Developers),
    path('task/',tasks),
    re_path(r'^task/(?P<level>[0-9]{1,2})/$', solve_question),
    #re_path(r'^task/(?P<id>\w+)/$', get_question),
    re_path(r'^(?P<filename>\w.+)/$', download_file),
]
