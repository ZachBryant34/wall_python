from django.db import models
import re
from datetime import datetime
class UserManager(models.Manager):
    def basic_validator(self, post_data):
        errors ={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(post_data['first_name']) < 2:
            errors['first_name'] = "First Name should be at least 2 characters"
        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Last Name should be at least 2 characters"
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Invalid email address!"
        # code to check if the email is unique
        users = User.objects.filter(email=post_data['email'])
        if len(users) == 1:
            errors['email_unique'] = "This email is already in use."
        # another way of doint it below
        # try:
        #     Register.objects.get(email=post_date['email'])
        #     errors['email_unique'] = "This email is already in use."
        # except:
        #     pass
        if post_data['password'] != post_data['conpass']:
            errors['conpass'] = "Passwords do not match"
        if len(post_data['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"
        if post_data['birthdate'] == "":
            errors['birthdate'] = "Birthdate is required"
        elif datetime.strptime(post_data['birthdate'],'%Y-%m-%d').date() > datetime.now().date():
            errors['birthdate'] = "Birthdate should be before today's date"
        today = datetime.now().date()
        born = datetime.strptime(post_data['birthdate'],'%Y-%m-%d').date()
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        if age < 13:
            errors['birthdate'] = "Must be 13 or over to register."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    birthdate = models.DateField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


