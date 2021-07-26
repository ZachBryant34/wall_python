from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from login_app.models import User
from .models import Message, Comment
from datetime import datetime, timedelta

def index(request):
    
    if 'user_id' not in request.session:
        messages.error(request, 'Please log in to view this page.')
        return redirect('/')
    context = {
        'all_messages': Message.objects.all().order_by('-created_at')
    }
    return render(request, 'wall.html', context)
    

def messages(request):
    Message.objects.create(message=request.POST['message'], user=User.objects.get(id=request.session['user_id']))
    return redirect('/wall')

def comments(request,id):
    Comment.objects.create(comment=request.POST['comment'],user=User.objects.get(id=request.session['user_id']), message=Message.objects.get(id=id))
    return redirect('/wall')

def message_delete(request,id):
    message = Message.objects.get(id=id)
    # now = datetime.now()
    # post_time = message.created_at
    # if now > (post_time + timedelta(minutes=30)):
    #     messages.error(request, 'Can only delete post within 30 minutes of creation.')
    #     return redirect('/wall')
    # else:
    message.delete()
    return redirect('/wall')

def comment_delete(request,id):
    Comment.objects.get(id=id).delete()
    return redirect('/wall')
# Create your views here.
