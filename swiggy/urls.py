from django.urls import path
from . import views
from . import models

urlpatterns=[
  path('',views.home,name='home'),
  path('signin',views.signin,name='signin'),
  path('signup',views.signup,name='signup'),
  path('thumbnail',views.thumbnail,name='thumbnail'),
  path('login',models.login,name='login'),
  path('register',models.register,name='register'),
  path('aboutus',views.aboutus,name='aboutus'),
  path('bestofcity',views.bestofcity,name='betofcity'),
  path('career',views.career,name='career'),
  path('contact',views.contact,name='contact'),
  path('dish',views.dish,name='dish'),
  path('microbreweries',views.microbreweries,name='microbreweries'),
  path('sportscreening',views.sportscreening,name='sportscreening'),
  path('trending',views.trending,name='trending'),
  path('zomatopro',views.zomatopro,name='zomatopro'),
]