from django.shortcuts import render, redirect
from .models import *
from apps.logreg_app.models import Users

def zoo(request, id):
    user = Users.objects.get(id=request.session['id'])
    zoo = user.zoos.get(id=int(id))
    exhibits = zoo.get_exhibits()
    context={
        "user" : user,
        "zoo" : zoo,
        "exhibits" : exhibits,
    }
    return render(request, 'zoo_app/zoo.html', context)

def build_store(request, id):
    user = Users.objects.get(id=request.session['id'])
    zoo = user.zoos.get(id=int(id))
    exhibits = zoo.get_exhibits()
    context={
        "user" : user,
        "zoo" : zoo,
        "exhibits" : exhibits,
    }
    return render(request, 'zoo_app/building_store.html', context)

def animal_store(request, id, building):
    user = Users.objects.get(id=request.session['id'])
    context={
        "user" : user,
        "this_building" : user.zoo.get(id=int(id)).exhibits.get(location=int(building)),
    }
    return render(request, 'zoo_app/animal_store.html', context)

def building(request, id, building):
    user = Users.objects.get(id=request.session['id'])
    context={
        "user" : user,
        "this_building" : user.zoo.get(id=int(id)).exhibits.get(location=int(building)),
        "buildings" : Buildings.objects.all(),
    }
    return render(request, 'zoo_app/building.html', context)

def manage(request, id):
    user = Users.objects.get(id=request.session['id'])
    context={
        "user" : user,
        "zoo" : user.zoos.get(id=int(id)),
    }
    return render(request, 'zoo_app/manage.html', context)

def buy_building(request, id, building):
    if request.method=="POST":
        user = Users.objects.get(id=request.session['id'])
        zoo = user.zoos.get(id=int(id))
        zoo.add_exhibit_validator()
        zoo.add_exhibit(request.POST['climate'], request.POST['name'], int(building))
    return redirect('/zoo/building/'+str(id))
def buy_animal(request, id, building):
    if request.method=="POST":
        Animals.objects.create(name="")
    return redirect('/zoo/building/'+str(id))
def change_ticket_price(request):
    if request.method=="POST":

    return redirect('/zoo/manage')
def buy_food(request, id):
    if request.method=="POST":
        Animals.objects.get(id=int(id)).feed(request.POST['food'])
    return redirect('/zoo/building/'+str(id))
def advance_day(request):
    if request.method=="POST":
        request.session['daily_log'] = {}
        user = Users.objects.get(id=request.session['id'])
        for zoo in user.zoos.all()
            daily_visitors = zoo.objects.advance_day()
            daily_money = user.advance_day_money(daily_visitors, zoo.ticket_price) 
            request.session['daily_log'][zoo.name] = {"daily_money" : daily_money,
            "daily_visitors" : daily_visitors}
            request.session['daily_log'][zoo.name]["weather"] = zoo.advance_day_weather()
            request.session['daily_log'][zoo.name]["ticket_price"] = zoo.update_ticket_price()
        user.advance_day()
    return redirect('/zoo')