from django.shortcuts import render, redirect
from .models import *
from apps.logreg_app.models import Users

def zoo_list(request):
    user = Users.objects.get(id=request.session['id'])
    zoos = Zoo.objects.filter(owner=user)
    context={
        "user" : user,
        "zoos" : zoos,
    }
    return render(request, 'zoo_app/zoo_list.html', context)

def create_zoo(request):
    user = Users.objects.get(id=request.session['id'])
    context={
        "user" : user,
    }
    return render(request, 'zoo_app/create_zoo.html', context)

def creating_zoo(request):
    user = Users.objects.get(id=request.session['id'])
    if request.method == "POST":
        zoo = Zoo.objects.create_zoo(user, str.capitalize(request.POST['name']))
        return redirect('/zoo/'+str(zoo.id))
    else:    
        return redirect('/zoo/create_zoo')

def zoo(request, id):
    user = Users.objects.get(id=request.session['id'])
    zoo = Zoo.objects.get(id=int(id))
    exhibits = zoo.get_exhibits()
    context={
        "user" : user,
        "zoo" : zoo,
        "exhibits" : exhibits,
    }
    return render(request, 'zoo_app/zoo.html', context)

def build_store(request, id, location):
    user = Users.objects.get(id=request.session['id'])
    zoo = user.zoos.get(id=int(id))
    context={
        "user" : user,
        "zoo" : zoo,
        "location" : int(location),
    }
    return render(request, 'zoo_app/building_store.html', context)

def animal_store(request, building_id):
    user = Users.objects.get(id=request.session['id'])
    habitat = Habitat.objects.get(id=building_id)
    zoo = habitat.zoo
    context={
        "user" : user,
        "zoo" : zoo,
        "this_building" : habitat,
    }
    return render(request, 'zoo_app/animal_store.html', context)

def building(request, building_id):
    user = Users.objects.get(id=request.session['id'])
    habitat = Habitat.objects.get(id=building_id)
    zoo = habitat.zoo
    context={
        "user" : user,
        "zoo" : zoo,
        "this_building" : habitat,
    }
    return render(request, 'zoo_app/building.html', context)

def manage(request, id):
    user = Users.objects.get(id=request.session['id'])
    context={
        "user" : user,
        "zoo" : user.zoos.get(id=int(id)),
    }
    return render(request, 'zoo_app/manage.html', context)

def daily_log(request):
    user = Users.objects.get(id=request.session['id'])
    context={
        "user" : user,
    }
    return render(request, 'zoo_app/daily_log.html', context)

def buy_building(request, id, location):
    if request.method=="POST":
        user = Users.objects.get(id=request.session['id'])
        zoo = Zoo.objects.get(id=int(id))
        habitat = zoo.add_exhibit(request.POST['climate'], str.capitalize(request.POST['name']), int(location))
    return redirect('/zoo/building/'+str(habitat.id))

def buy_animal(request, building_id):
    if request.method=="POST":
        user = Users.objects.get(id=request.session['id'])
        Habitat.objects.get(id=int(building_id)).add_animal(request.POST['breed'], str.capitalize(request.POST['name']))
    return redirect('/zoo/building/'+str(building_id))

def change_ticket_price(request, zoo_id):
    if request.method=="POST":
        Zoo.objects.change_ticket_price_validator(request.POST)
        zoo = Zoo.objects.get(id=int(zoo_id)).change_ticket_price(request.POST['price'])
    return redirect('/zoo/manage')

def buy_food(request, animal_id):
    if request.method=="POST":
        animal = Animal.objects.get(id=int(animal_id))
        animal.feed(request.POST['food'])
        animal_habitat = animal.habitat.id
        return redirect('/zoo/building/'+str(animal_habitat))
    return redirect('/zoo/1')

def advance_day(request):
    request.session['daily_log'] = {}
    user = Users.objects.get(id=request.session['id'])
    for zoo in user.zoos.all():
        info = zoo.advance_day()
        daily_money = user.advance_day_money(info['daily_visitors'], zoo.ticket_price) 
        request.session['daily_log'][zoo.name] = {"name": zoo.name, "daily_money" : daily_money,
        "daily_visitors" : info['daily_visitors']}
        request.session['daily_log'][zoo.name]["weather"] = info['weather']
        request.session['daily_log'][zoo.name]["ticket_price"] = zoo.ticket_price
    user.advance_day()
    print(request.session['daily_log'])
    return redirect('/zoo/daily_log')