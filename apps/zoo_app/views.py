from django.shortcuts import render, redirect
from .models import *
from apps.logreg_app.models import Users
from django.contrib import messages

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
        if user.money < 30000:
            messages.error(request, "<p style='color: red;'>You cannot afford this.</p>", extra_tags="money")
        else:
            zoo = Zoo.objects.create_zoo(user, request.POST['name'])
            return redirect('/zoo/'+str(zoo.id))
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
    capacity = habitat.capacity
    fullness = habitat.how_full()
    context={
        "user" : user,
        "zoo" : zoo,
        "this_building" : habitat,
        "capacity" : capacity,
        "fullness" : fullness,
    }
    return render(request, 'zoo_app/building.html', context)

def manage(request, id):
    user = Users.objects.get(id=request.session['id'])
    context={
        "user" : user,
        "zoo" : user.zoos.get(id=int(id)),
    }
    return render(request, 'zoo_app/manage.html', context)

def buy_building(request, id, location):
    if request.method=="POST":
        user = Users.objects.get(id=request.session['id'])
        if request.POST['climate'] == "forest" and user.money < 6000:
            messages.error(request, "<p style='color: red;'>You cannot afford this.</p>", extra_tags="money")
        elif request.POST['climate'] == "arctic" and user.money < 7000:
            messages.error(request, "<p style='color: red;'>You cannot afford this.</p>", extra_tags="money")
        elif request.POST['climate'] == "jungle" and user.money < 8000:
            messages.error(request, "<p style='color: red;'>You cannot afford this.</p>", extra_tags="money")
        elif request.POST['climate'] == "savanna" and user.money < 9000:
            messages.error(request, "<p style='color: red;'>You cannot afford this.</p>", extra_tags="money")
        else:
            zoo = Zoo.objects.get(id=int(id))
            habitat = zoo.add_exhibit(request.POST['climate'], str(request.POST['name']), int(location))
            return redirect('/zoo/building/'+str(habitat.id))
    return redirect('/zoo/'+str(id)+'/build_store/'+str(location))

def buy_animal(request, building_id):
    user = Users.objects.get(id=request.session['id'])
    if request.method=="POST":
        if request.POST['breed'] == "grizzly_bear" and user.money < 4000:
            messages.error(request, "<p style='color: red;'>You cannot afford this.</p>", extra_tags="money")
        elif request.POST['breed'] == "wolf" and user.money < 2000:
            messages.error(request, "<p style='color: red;'>You cannot afford this.</p>", extra_tags="money")
        elif request.POST['breed'] == "owl" and user.money < 1000:
            messages.error(request, "<p style='color: red;'>You cannot afford this.</p>", extra_tags="money")
        elif request.POST['breed'] == "giraffe" and user.money < 4000:
            messages.error(request, "<p style='color: red;'>You cannot afford this.</p>", extra_tags="money")
        elif request.POST['breed'] == "lion" and user.money < 4000:
            messages.error(request, "<p style='color: red;'>You cannot afford this.</p>", extra_tags="money")
        elif request.POST['breed'] == "rhino" and user.money < 4000:
            messages.error(request, "<p style='color: red;'>You cannot afford this.</p>", extra_tags="money")
        elif request.POST['breed'] == "african_elephant" and user.money < 4000:
            messages.error(request, "<p style='color: red;'>You cannot afford this.</p>", extra_tags="money")
        elif request.POST['breed'] == "polar_bear" and user.money < 4000:
            messages.error(request, "<p style='color: red;'>You cannot afford this.</p>", extra_tags="money")
        elif request.POST['breed'] == "arctic_fox" and user.money < 1200:
            messages.error(request, "<p style='color: red;'>You cannot afford this.</p>", extra_tags="money")
        elif request.POST['breed'] == "penguin" and user.money < 2000:
            messages.error(request, "<p style='color: red;'>You cannot afford this.</p>", extra_tags="money")
        elif request.POST['breed'] == "tiger" and user.money < 3200:
            messages.error(request, "<p style='color: red;'>You cannot afford this.</p>", extra_tags="money")
        elif request.POST['breed'] == "orangutan" and user.money < 4000:
            messages.error(request, "<p style='color: red;'>You cannot afford this.</p>", extra_tags="money")
        elif request.POST['breed'] == "fruit_bat" and user.money < 2000:
            messages.error(request, "<p style='color: red;'>You cannot afford this.</p>", extra_tags="money")
        elif request.POST['breed'] == "asian_elephant" and user.money < 3800:
            messages.error(request, "<p style='color: red;'>You cannot afford this.</p>", extra_tags="money")
        else:
            animal = Habitat.objects.get(id=int(building_id)).add_animal(request.POST['breed'], str(request.POST['name']))
            if not animal:
                messages.error(request, "<p style='color: red;'>Your exhibit is too full.</p>", extra_tags="capacity")
    return redirect('/zoo/building/'+str(building_id))

def change_ticket_price(request, zoo_id):
    if request.method=="POST":
        if (request.POST['ticket_price']).isdigit()==False:
            messages.error(request, "<p style='color: red;'>New ticket price is invalid.</p>", extra_tags="ticket_price")
        else:
            zoo = Zoo.objects.get(id=int(zoo_id)).change_ticket_price(int(request.POST['ticket_price']))
    return redirect('/zoo/'+str(zoo_id)+'/manage')

def buy_food(request, animal_id):
    animal = Animal.objects.get(id=int(animal_id))
    animal_habitat = animal.habitat.all()[0].id
    if request.method=="POST":
        user = Users.objects.get(id=request.session['id'])
        if request.POST['food'] == "grasses" and user.money < 80:
            messages.error(request, "<p style='color: red;'>You cannot afford this.</p>", extra_tags="money")
        elif request.POST['food'] == "leaves" and user.money < 100:
            messages.error(request, "<p style='color: red;'>You cannot afford this.</p>", extra_tags="money")
        elif request.POST['food'] == "fruit" and user.money < 120:
            messages.error(request, "<p style='color: red;'>You cannot afford this.</p>", extra_tags="money")
        elif request.POST['food'] == "meat" and user.money < 140:
            messages.error(request, "<p style='color: red;'>You cannot afford this.</p>", extra_tags="money")
        elif request.POST['food'] == "fish" and user.money < 160:
            messages.error(request, "<p style='color: red;'>You cannot afford this.</p>", extra_tags="money")
        else:
            message = animal.feed(request.POST['food'])
            messages.success(request, "<p style='color: blue;'>"+message+"</p>", extra_tags=animal.id)
    return redirect('/zoo/building/'+str(animal_habitat))

def advance_day(request):
    request.session['daily_log'] = {}
    user = Users.objects.get(id=request.session['id'])
    for zoo in user.zoos.all():
        info = zoo.advance_day()
        print(info["messages"])
        daily_money = user.advance_day_money(info['daily_visitors'], zoo.ticket_price) 
        request.session['daily_log'][zoo.name] = {"name": zoo.name, "daily_money" : daily_money, "daily_visitors" : info['daily_visitors'], "messages": info["messages"]}
        request.session['daily_log'][zoo.name]["weather"] = info['weather']

        zoo.ticket_price = zoo.tomorrows_ticket_price
        zoo.save()
        request.session['daily_log'][zoo.name]["ticket_price"] = zoo.ticket_price
    user.advance_day()
    print(request.session['daily_log'])
    return redirect('/zoo/'+str(zoo.id))