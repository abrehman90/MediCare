from django.urls import path
from .views import *


urlpatterns = [
    path('',index,name='index'),
    path('NGO/',ngo,name='ngo'),
    path('buy/',form,name='form'),
    path('card-detail/',card,name='card'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('blog/',blog,name='blog'),
]