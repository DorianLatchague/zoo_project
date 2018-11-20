from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from apps.logreg_app.models import Users
import random

### HARDCODED DATABASES
price = {
    "food":{
        "meat" : 140,
        "grasses" : 80,
        "leaves" : 100,
        "fruit" : 120,
        "fish" : 160,
    }
}
animals = {
    "grizzly_bear": { # FOREST
        "description":"Here is a description of a grizzly bear!",
        "weather_prefs":{"overcast":0,"sunny":4,"rainy": -4,"stormy": -6}, #number between -10 and 10
        "diet":{ #numbers between -5 and 5
            "meat":{"taste": 4,"nutrition": 5,"price": price["food"]["meat"]},
            "grasses":{"taste": -4,"nutrition": 0, "price": price["food"]["grasses"]},
            "leaves":{"taste": -5, "nutrition": -2, "price": price["food"]["leaves"]},
            "fruit":{"taste": 5,"nutrition": 3, "price": price["food"]["fruit"]},
            "fish":{"taste": 5, "nutrition": 4, "price": price["food"]["fish"]} 
        },
        "lifespan":(1000,1250), #this is a tuple of min lifespan and max lifespan
        "popularity":95, #this should be a number between 80 and 100
        "size":4, #capacity of habitat is 12. This should be a 2, 3, or 4
        "price": 4000, #between 1000 and 4000
    },
    "wolf": { #FOREST
        "description":"Wolves are awesome and also cute!",
        "weather_prefs":{"overcast":0,"sunny":4,"rainy": -4,"stormy": -6}, #number between -10 and 10
        "diet":{ #numbers between -5 and 5
            "meat":{"taste": 5,"nutrition": 5,"price": price["food"]["meat"]},
            "grasses":{"taste": -4,"nutrition": 1, "price": price["food"]["grasses"]},
            "leaves":{"taste": -5, "nutrition": -2, "price": price["food"]["leaves"]},
            "fruit":{"taste": 2,"nutrition": 3, "price": price["food"]["fruit"]},
            "fish":{"taste": 4, "nutrition": 4, "price": price["food"]["fish"]} 
        },
        "lifespan":(250,300), #this is a tuple of min lifespan and max lifespan
        "popularity":90, #this should be a number between 80 and 100
        "size":2, #capacity of habitat is 12. This should be a 1, 2, 3, or 4
        "price": 2000, #between 1000 and 4000
    },
    "owl": { #FOREST
        "description":"Here is a description of an owl!",
        "weather_prefs":{"overcast":10,"sunny":0,"rainy": -4,"stormy": -2}, #number between -10 and 10
        "diet":{ #numbers between -5 and 5
            "meat":{"taste": 5,"nutrition": 5,"price": price["food"]["meat"]},
            "grasses":{"taste": -4,"nutrition": -3, "price": price["food"]["grasses"]},
            "leaves":{"taste": -4, "nutrition": -2, "price": price["food"]["leaves"]},
            "fruit":{"taste": 1,"nutrition": 1, "price": price["food"]["fruit"]},
            "fish":{"taste": 3, "nutrition": 3, "price": price["food"]["fish"]} 
        },
        "lifespan":(200,250), #this is a tuple of min lifespan and max lifespan
        "popularity":82, #this should be a number between 80 and 100
        "size":1, #capacity of habitat is 12. This should be a 2, 3, or 4
        "price": 1000, #between 1000 and 4000
    },
    "giraffe": { #SAVANNA
        "description":"Here is a description of a giraffe!",
        "weather_prefs":{"overcast":0,"sunny":10,"rainy": -6,"stormy": -10}, #number between -10 and 10
        "diet":{ #numbers between -5 and 5
            "meat":{"taste": -5,"nutrition": -5,"price": price["food"]["meat"]},
            "grasses":{"taste": 3,"nutrition": 1, "price": price["food"]["grasses"]},
            "leaves":{"taste": 5, "nutrition": 5, "price": price["food"]["leaves"]},
            "fruit":{"taste": 2,"nutrition": 3, "price": price["food"]["fruit"]},
            "fish":{"taste": -4, "nutrition": -4, "price": price["food"]["fish"]} 
        },
        "lifespan":(1200,1300), #this is a tuple of min lifespan and max lifespan
        "popularity":95, #this should be a number between 80 and 100
        "size":4, #capacity of habitat is 12. This should be a 2, 3, or 4
        "price": 4000, #between 1000 and 4000
    },
    "lion": { #SAVANNA
        "description":"Here is a description of a lion!",
        "weather_prefs":{"overcast":0,"sunny":4,"rainy": -4,"stormy": -6}, #number between -10 and 10
        "diet":{ #numbers between -5 and 5
            "meat":{"taste": 5,"nutrition": 5,"price": price["food"]["meat"]},
            "grasses":{"taste": -3,"nutrition": 1, "price": price["food"]["grasses"]},
            "leaves":{"taste": -5, "nutrition": -5, "price": price["food"]["leaves"]},
            "fruit":{"taste": 0,"nutrition": 2, "price": price["food"]["fruit"]},
            "fish":{"taste": 3, "nutrition": 4, "price": price["food"]["fish"]} 
        },
        "lifespan":(500,700), #this is a tuple of min lifespan and max lifespan
        "popularity":98, #this should be a number between 80 and 100
        "size":3, #capacity of habitat is 12. This should be a 2, 3, or 4
        "price": 4000, #between 1000 and 4000
    },
    "rhino": { #SAVANA
        "description":"Here is a description of a rhino!",
        "weather_prefs":{"overcast":0,"sunny":8,"rainy": -4,"stormy": -6}, #number between -10 and 10
        "diet":{ #numbers between -5 and 5
            "meat":{"taste": -3,"nutrition": -4,"price": price["food"]["meat"]},
            "grasses":{"taste": 4,"nutrition": 5, "price": price["food"]["grasses"]},
            "leaves":{"taste": 1, "nutrition": 1, "price": price["food"]["leaves"]},
            "fruit":{"taste": 2,"nutrition": 3, "price": price["food"]["fruit"]},
            "fish":{"taste": -3, "nutrition": -4, "price": price["food"]["fish"]} 
        },
        "lifespan":(2000,2500), #this is a tuple of min lifespan and max lifespan
        "popularity":92, #this should be a number between 80 and 100
        "size":3, #capacity of habitat is 12. This should be a 2, 3, or 4
        "price": 4000, #between 1000 and 4000
    },
    "african_elephant": { #SAVANNA
        "description":"Here is a description of an African elephant!",
        "weather_prefs":{"overcast":0,"sunny":10,"rainy": -4,"stormy": -6}, #number between -10 and 10
        "diet":{ #numbers between -5 and 5
            "meat":{"taste": -5,"nutrition": 0,"price": price["food"]["meat"]},
            "grasses":{"taste": 4,"nutrition": 5, "price": price["food"]["grasses"]},
            "leaves":{"taste": 4, "nutrition": 4, "price": price["food"]["leaves"]},
            "fruit":{"taste": 5,"nutrition": 3, "price": price["food"]["fruit"]},
            "fish":{"taste": 0, "nutrition": 2, "price": price["food"]["fish"]} 
        },
        "lifespan":(3000,3500), #this is a tuple of min lifespan and max lifespan
        "popularity":90, #this should be a number between 80 and 100
        "size":4, #capacity of habitat is 12. This should be a 2, 3, or 4
        "price": 4000, #between 1000 and 4000
    },
    "polar_bear": { #ARCTIC
        "description":"Here is a description of a polar bear!",
        "weather_prefs":{"overcast":5,"sunny":-7,"rainy": 5,"stormy": 3}, #number between -10 and 10
        "diet":{ #numbers between -5 and 5
            "meat":{"taste": 5,"nutrition": 5,"price": price["food"]["meat"]},
            "grasses":{"taste": -4,"nutrition": -2, "price": price["food"]["grasses"]},
            "leaves":{"taste": -5, "nutrition": -2, "price": price["food"]["leaves"]},
            "fruit":{"taste": 2,"nutrition": 3, "price": price["food"]["fruit"]},
            "fish":{"taste": 5, "nutrition": 5, "price": price["food"]["fish"]} 
        },
        "lifespan":(1200,1300), #this is a tuple of min lifespan and max lifespan
        "popularity":100, #this should be a number between 80 and 100
        "size":4, #capacity of habitat is 12. This should be a 2, 3, or 4
        "price": 4000, #between 1000 and 4000
    },
    "arctic_fox": { #ARCTIC
        "description":"Here is a description of an arctic fox!",
        "weather_prefs":{"overcast":6,"sunny":0,"rainy": -4,"stormy": -2}, #number between -10 and 10
        "diet":{ #numbers between -5 and 5
            "meat":{"taste": 4,"nutrition": 5,"price": price["food"]["meat"]},
            "grasses":{"taste": -4,"nutrition": 0, "price": price["food"]["grasses"]},
            "leaves":{"taste": -4, "nutrition": -2, "price": price["food"]["leaves"]},
            "fruit":{"taste": 4,"nutrition": 4, "price": price["food"]["fruit"]},
            "fish":{"taste": 4, "nutrition": 5, "price": price["food"]["fish"]} 
        },
        "lifespan":(200,250), #this is a tuple of min lifespan and max lifespan
        "popularity":87, #this should be a number between 80 and 100
        "size":2, #capacity of habitat is 12. This should be a 2, 3, or 4
        "price": 1200, #between 1000 and 4000
    },
    "penguin": { #ARCTIC
        "description":"Here is a description of a penguin!",
        "weather_prefs":{"overcast":8,"sunny":2,"rainy": 6,"stormy": -3}, #number between -10 and 10
        "diet":{ #numbers between -5 and 5
            "meat":{"taste": 2,"nutrition": 4,"price": price["food"]["meat"]},
            "grasses":{"taste": -4,"nutrition": -3, "price": price["food"]["grasses"]},
            "leaves":{"taste": -5, "nutrition": -5, "price": price["food"]["leaves"]},
            "fruit":{"taste": 2,"nutrition": 3, "price": price["food"]["fruit"]},
            "fish":{"taste": 5, "nutrition": 5, "price": price["food"]["fish"]} 
        },
        "lifespan":(300,1000), #this is a tuple of min lifespan and max lifespan
        "popularity":90, #this should be a number between 80 and 100
        "size":1, #capacity of habitat is 12. This should be a 2, 3, or 4
        "price": 2000, #between 1000 and 4000
    },
    "tiger": { #JUNGLE
        "description":"Here is a description of a ferocious tiger!",
        "weather_prefs":{"overcast":0,"sunny":4,"rainy": -4,"stormy": -6}, #number between -10 and 10
        "diet":{ #numbers between -5 and 5
            "meat":{"taste": 5,"nutrition": 5,"price": price["food"]["meat"]},
            "grasses":{"taste": 1,"nutrition": 2, "price": price["food"]["grasses"]},
            "leaves":{"taste": -5, "nutrition": -3, "price": price["food"]["leaves"]},
            "fruit":{"taste": 2,"nutrition": 3, "price": price["food"]["fruit"]},
            "fish":{"taste": 3, "nutrition": 4, "price": price["food"]["fish"]} 
        },
        "lifespan":(800,900), #this is a tuple of min lifespan and max lifespan
        "popularity":94, #this should be a number between 80 and 100
        "size":3, #capacity of habitat is 12. This should be a 2, 3, or 4
        "price": 3200, #between 1000 and 4000
    },
    "orangutan": { #JUNGLE
        "description":"Here is a description of an orangutan!",
        "weather_prefs":{"overcast":4,"sunny":10,"rainy": -4,"stormy": -10}, #number between -10 and 10
        "diet":{ #numbers between -5 and 5
            "meat":{"taste": 4,"nutrition": 3,"price": price["food"]["meat"]},
            "grasses":{"taste": 0,"nutrition": 1, "price": price["food"]["grasses"]},
            "leaves":{"taste": 3, "nutrition": 4, "price": price["food"]["leaves"]},
            "fruit":{"taste": 5,"nutrition": 4, "price": price["food"]["fruit"]},
            "fish":{"taste": 4, "nutrition": 5, "price": price["food"]["fish"]} 
        },
        "lifespan":(1750,2250), #this is a tuple of min lifespan and max lifespan
        "popularity":92, #this should be a number between 80 and 100
        "size":3, #capacity of habitat is 12. This should be a 2, 3, or 4
        "price": 4000, #between 1000 and 4000
    },
    "fruit_bat": { #JUNGLE
        "description":"Here is a description of a fruit bat!",
        "weather_prefs":{"overcast":8,"sunny":6,"rainy": 0,"stormy": -10}, #number between -10 and 10
        "diet":{ #numbers between -5 and 5
            "meat":{"taste": 4,"nutrition": 5,"price": price["food"]["meat"]},
            "grasses":{"taste": -4,"nutrition": 0, "price": price["food"]["grasses"]},
            "leaves":{"taste": -5, "nutrition": -2, "price": price["food"]["leaves"]},
            "fruit":{"taste": 50,"nutrition": 3, "price": price["food"]["fruit"]},
            "fish":{"taste": 5, "nutrition": 4, "price": price["food"]["fish"]} 
        },
        "lifespan":(1000,1250), #this is a tuple of min lifespan and max lifespan
        "popularity":80, #this should be a number between 80 and 100
        "size":1, #capacity of habitat is 12. This should be a 2, 3, or 4
        "price": 2000, #between 1000 and 4000
    },
    "asian_elephant": { #JUNGLE
        "description":"Here is a description of an Asian elephant!",
        "weather_prefs":{"overcast":0,"sunny":4,"rainy": -4,"stormy": -6}, #number between -10 and 10
        "diet":{ #numbers between -5 and 5
            "meat":{"taste": -3,"nutrition": -5,"price": price["food"]["meat"]},
            "grasses":{"taste": 4,"nutrition": 4, "price": price["food"]["grasses"]},
            "leaves":{"taste": 5, "nutrition": 5, "price": price["food"]["leaves"]},
            "fruit":{"taste": 5,"nutrition": 3, "price": price["food"]["fruit"]},
            "fish":{"taste": -1, "nutrition": 3, "price": price["food"]["fish"]} 
        },
        "lifespan":(2400,2500), #this is a tuple of min lifespan and max lifespan
        "popularity":95, #this should be a number between 80 and 100
        "size":4, #capacity of habitat is 12. This should be a 2, 3, or 4
        "price": 3800, #between 1000 and 4000
    },
}
habitats = {
    "arctic":{
        "description": "Description of the artarctic",
        # "animals":[polar_bear, arctic_fox,]
        "price": 7000,
        "popularity": 70, #number between 50 and 100
        "capacity": 12, #how many animals will fit. I chose 12 because it has a lot of factors
    },
    "savanna":{
        "description": "Description of the artarctic",
        "price": 9000,
        "popularity": 90,
        "capacity": 12,
    },
    "forest":{
        "description": "Description of the artarctic",
        "price": 6000,
        "popularity": 60,
        "capacity": 12,
    },
    "jungle":{
        "description": "Description of the artarctic",
        "price": 8000,
        "popularity": 80,
        "capacity": 12,
    },
}

#ZOO MANAGER
class ZooManager(models.Manager):

    #CREATE NEW ZOO
    def create_zoo(self, owner, name):
        new_zoo = self.create(
            owner = owner,
            name = name,
            capacity = 6,
            weather = 2,
        )
        new_zoo.update_weather()
        return new_zoo

    def add_exhibit_validator(self, postData):
        pass

    #change_ticket_price_validator(self, postData)
        
## ZOO CLASS
class Zoo(models.Model):
    owner = models.ForeignKey(Users, related_name = "zoos")
    name = models.CharField(max_length=255)
    ticket_price = models.PositiveSmallIntegerField(default=5)
    tomorrows_ticket_price = models.PositiveSmallIntegerField(default=5)
    capacity = models.PositiveSmallIntegerField(choices=((4, 'small'),(6, 'medium'),(8, 'large')))
    weather = models.PositiveSmallIntegerField(choices=((1,'overcast'), (2,'sunny'),(3,'rainy'),(4,'stormy')))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ZooManager()
    #exhibits   

#ZOO METHODS
    def get_exhibits(self):
        exhibits = []
        for i in range(0, (self.capacity)):
            if self.exhibits.filter(location=(i+1)):  
                exhibits.append([i+1, self.exhibits.get(location=(i+1))])
            else:
                exhibits.append([i+1, "empty"])
        return exhibits

    def update_weather(self):
        weather = random.randint(1,4)
        self.weather = weather
        self.save()
        return self

    def zoo_popularity(self):
        exhibits = self.exhibit.all()
        total = 0
        for exhibit in exhibits:
            total = total +(exhibit.attraciveness()*100)
        return total/self.exhibit.count() #takeintoaccountticketprice

    #change_ticket_price(self, price)

    #ADD EXHIBIT TO ZOO
    def add_exhibit(self, climate, name, location):
        new_exhibit = Habitat.objects.create_habitat(self, climate, name, location)
        self.exhibits.add(new_exhibit)
        return self

    def advance_day(self):
        all_animals = self.exhibit.inhabitants.all()
        for animal in all_animals:
            animal.day_end()
        update_weather(self)
        for animal in all_animals:
            animal.day_start()
        # update_events(self)
        # update_ticket_price(self)
        daily_visitors = zoo_popularity(self) * 4
        return daily_visitors



##HABITAT MANAGER
class HabitatManager(models.Manager):

    #def animal_validator(self, postData):
    #CREATE NEW HABITAT
    def create_habitat(self, zoo, climate, name, location):
        price = habitats[climate]["price"]
        popularity = habitats[climate]["popularity"]
        capacity = habitats[climate]["capacity"]
        description = habitats[climate]["capacity"]
        new_habitat = self.create(
            name=name,
            climate= climate,
            price = price,
            capacity = capacity,
            description = description,
            zoo = zoo,
            location = location,
            popularity = popularity,
        )
        return new_habitat



## HABITAT CLASS
class Habitat(models.Model):
    name = models.CharField(max_length=255)
    climate = models.CharField(max_length = 55, choices=(('arctic', 'arctic'), ('savanna','savanna'),('forest', 'forest'), ('jungle','jungle')))
    price = models.PositiveSmallIntegerField() #is this necessary as an attribute? Probably not.
    popularity = models.PositiveSmallIntegerField()
    capacity = models.PositiveSmallIntegerField()
    description = models.TextField()
    zoo = models.ForeignKey(Zoo, related_name="exhibits")
    location = models.PositiveSmallIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = HabitatManager()
    #inhabitants

#HABITAT METHODS
    def attractiveness(self, inhabitants, climate):
        #based on:
        habitats[climate]["popularity"]
        self.inhabitants.attractiveness
        return attractiveness

#ADD ANIMAL TO HABITAT
    def add_animal(self, breed, name):
        num_animals = self.inhabitants.count()
        if num_animals < self.capacity:
            new_animal = Animal.objects.create_animal(self, breed, name)
            new_animal.location = (num_animals +1)
            self.inhabitants.add(new_animal)
        else:
            #message the user "You cannot!"
            pass


#### ANIMAL MANAGER
class AnimalManager(models.Manager):
    
    ## CREATE NEW ANIMAL
    def create_animal(self, habitat, breed, name):
        health = random.randint(60,95)
        happiness = random.randint(60,95)
        animal_prefs = animals[breed] #a dictionary of animal prefs
        min = animal_prefs["lifespan"][0]
        max = animal_prefs["lifespan"][1]
        lifespan = random.randint(min, max)
        age = random.randint(1,(lifespan//2))
        description = animals[breed]["description"]
        new_animal = self.create(
            age = age,
            name = name,
            health= health,
            happiness = happiness,
            habitat = habitat,
            breed = breed,
            lifespan = lifespan,
            popularity = animals[breed]["popularity"],
            size = animals[breed]["size"]
        )
        return new_animal


#### ANIMAL CLASS
class Animal(models.Model):
    age = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=255) #entered by user
    health = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
    happiness = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
    breed = models.CharField(max_length=55, choices=(
        ('grizzly_bear','grizzly_bear'),
        ('wolf','wolf'),
        ('owl','owl'),
        ('giraffe','giraffe'),
        ('lion','lion'),
        ('rhino','rhino'),
        ('african_elephant','african_elephant'),
        ('polar_bear','polar_bear'),
        ('arctic_fox','arctic_fox'),
        ('penguin','penguin'),
        ('tiger','tiger'),
        ('orangutan','orangutan'),
        ('fruit_bat','fruit_bat'),
        ('asian_elephant','asian_elephant'),
    ))
    lifespan =  models.PositiveSmallIntegerField()
    popularity = models.PositiveSmallIntegerField()
    size = models.PositiveSmallIntegerField()
    habitat = models.ForeignKey(Habitat, related_name = "inhabitants")
    location = models.PositiveSmallIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AnimalManager()

## ANIMAL METHODS
    def attractiveness(self):
        attractiveness = int((self.health + self.happiness)/2)*(self.popularity/100)
        return attractiveness # a number between 0 and 100

#DAY POST
    def day_start(self):
        self.happiness = self.happiness + animals[self.breed]["weather_prefs"][self.habitat.zoo.weather]
        return self

    def day_end(self): #animal.advance_day
        self.happiness = self.happiness - animals[self.breed]["weather_prefs"][self.habitat.zoo.weather]
        return self

#FEED POST
    def feed(self, food):
        meal = animals[self.breed]["diet"][food]
        self.happiness = self.happiness + meal["taste"]
        self.health = self.health + meal["nutrition"]
        self.habitat.zoo.owner.money = self.habitat.zoo.owner.money - meal[price]
        return self