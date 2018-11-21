from django.shortcuts import render, HttpResponse, redirect
from .models import Users
from django.contrib import messages
import bcrypt
import re
from apps.zoo_app.models import Zoo
def logreg(request):
    if 'id' in request.session:
        return redirect('/zoo/')
    return render(request, 'logreg_app/log_reg.html')
def logging_in(request):
    if request.method=="POST":
        errors = Users.objects.log_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/')
        else:
            user = Users.objects.get(email=request.POST['log_email'])
            request.session['id'] = user.id
            zoos = user.zoos
            if user.zoos.count() == 0:
                return redirect('/zoo/create_zoo')
            if user.zoos.count() == 1:
                zoo = Zoo.objects.get(owner=user)
                return redirect('/zoo/'+str(zoo.id))
            return redirect('/zoo')
    else: 
        return redirect('/')
def registering(request):
    if request.method=="POST":
        errors = Users.objects.reg_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/')
        else:
            pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            info = Users.objects.create(username=request.POST['username'], first_name=str.capitalize(request.POST['first_name']), last_name=str.capitalize(request.POST['last_name']), email=request.POST['email'], password=pw_hash)
            request.session['id'] = info.id
            return redirect('/zoo/create_zoo')
    else: 
        return redirect('/')
def edit(request, id):
    if 'id' in request.session:
        if int(id) == request.session['id']:
            context={
                "user" : Users.objects.get(id=request.session['id']),
            }
            return render(request, 'logreg_app/edit.html', context)
        else:
            return redirect('/zoo')
    else:
        return redirect('/')
def editing(request, id):
    if request.method=="POST":
        if int(id) == request.session['id']:
            errors = Users.objects.edit_validator(request.POST, int(id))
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value, extra_tags=key)
                return redirect('/myaccount/'+str(id))
            else:
                user = Users.objects.get(id=int(id))
                user.username = request.POST['username']
                user.first_name = request.POST['first_name']
                user.last_name = request.POST['last_name']
                user.email = request.POST['email']
                user.save()
                return redirect('/myaccount/'+str(id))
        else:
            return redirect('/zoo')
    return redirect('/myaccount/'+str(id))
def logout(request):
    request.session.clear()
    return redirect('/')