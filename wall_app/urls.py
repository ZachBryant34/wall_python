from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('messages', views.messages),
    path('comments/<int:id>', views.comments),
    path('messages/<int:id>/delete', views.message_delete),
    path('comments/<int:id>/delete', views.comment_delete)
]