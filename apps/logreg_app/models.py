from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

NAME_REGEX = re.compile(r'^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.-]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^[a-zA-Z0-9-!._]+$')
class Usermanager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if not EMAIL_REGEX.match(postData["email"]):
            errors['email'] = "Your email is invalid."
        else:
            if Users.objects.filter(email=postData["email"]):
                errors['email'] = "This email is already in use."
        if len(postData["first_name"]) < 2:
            errors['first_name'] = "Your first name must be at least 2 characters long."
        elif not NAME_REGEX.match(postData["first_name"]) == False:
            errors['first_name'] = "Your first name must contain only letters."
        if len(postData["last_name"]) < 2:
            errors['last_name'] = "Your last name must be at least 2 characters long."
        elif not NAME_REGEX.match(postData["first_name"]) == False:
            errors['last_name'] = "Your last name must contain only letters."
        if len(postData["password"]) < 8:
            errors['password'] = "Your password must be at least 8 characters long."
        elif not PASSWORD_REGEX.match(postData["password"]):
            errors['password'] = "Your password can only contain letters, numbers and the characters - _ ! and ."
        if postData["confirm_password"] != postData["password"]:
            errors['confirm_password'] = "The password confirmation field must be the same as the password's."
        return errors
    def log_validator(self, postData):
        errors={}
        if Users.objects.filter(email=postData['log_email']):
            identify = Users.objects.get(email=postData['log_email'])
            if bcrypt.checkpw(postData['log_password'].encode(), identify.password.encode())==False:
                errors["log_password"] = "Your password did not match this email address."
        else:
            errors["log_email"] = "Your email did not match any in our records."
        return errors
    def edit_validator(self, postData, id):
        errors = {}
        if not EMAIL_REGEX.match(postData["email"]):
            errors['email'] = "Your email is invalid."
        else:
            if Users.objects.filter(email=postData["email"]).exclude(id=id):
                errors['email'] = "This email is already in use."
        if len(postData["first_name"]) < 2:
            errors['first_name'] = "Your first name must be at least 2 characters long."
        elif str.isalpha(postData["first_name"]) == False:
            errors['first_name'] = "Your first name must contain only letters."
        if len(postData["last_name"]) < 2:
            errors['last_name'] = "Your last name must be at least 2 characters long."
        elif str.isalpha(postData["last_name"]) == False:
            errors['last_name'] = "Your last name must contain only letters."
        return errors

class Users(models.Model):
    email = models.CharField(max_length=55)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True) 
    money = models.IntegerField(default=50000)
    day = models.IntegerField(default=1)
    objects = Usermanager()

    def advance_day(self):
        self.day += 1
        self.save()
        return self.day
    
    def advance_day_money(self, daily_visitor, ticket_price):
        daily_money  = ticket_price * daily_visitor
        self.money += daily_money
        self.save()
        return daily_money