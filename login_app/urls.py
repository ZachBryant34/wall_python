from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index),
    path('user/register', views.process_registration),
    path('user/login', views.process_login),
    path('destroy', views.destroy),
]