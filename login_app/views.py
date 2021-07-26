from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'index.html')
def process_registration(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'],birthdate=request.POST['birthdate'], password=pw_hash)
    request.session['user_id'] = user.id
    request.session['user_email'] = user.email
    request.session['user_first_name'] = user.first_name
    request.session['user_last_name'] = user.last_name
    return redirect('/wall')
def process_login(request):
    users = User.objects.filter(email=request.POST['email'])
    if len(users) != 1:
        messages.error(request, 'No user with this email exists.')
        return redirect('/')
    user = users[0]
    print(user.email)
    if not bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        messages.error(request, 'Password for this email is incorrect')
        return redirect('/')
    request.session['user_id'] = user.id
    request.session['user_email'] = user.email
    request.session['user_first_name'] = user.first_name
    request.session['user_last_name'] = user.last_name
    return redirect('/wall')

def destroy(request):
    request.session.flush()
    return redirect('/')
# Create your views here.
