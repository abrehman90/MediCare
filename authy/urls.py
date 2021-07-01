from django.urls import path
from authy.views import Signup,logoutUser

from django.contrib.auth import views as authViews 



urlpatterns = [
	path('signup/', Signup, name='login'),
	path('logout/', logoutUser, name='logout'),
]