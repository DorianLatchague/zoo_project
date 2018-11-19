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
            "fruit":{"taste": 50,"nutrition": 3, "price": price["food"]["fruit"]},
            "fish":{"taste": 5, "nutrition": 4, "price": price["food"]["fish"]} 
        },
        "lifespan":(20,25), #this is a tuple of min lifespan and max lifespan
        "popularity":95, #this should be a float between .8 and 1 (.8, .85, .9, .95, 1)
        "size":4, #capacity of habitat is 12. This should be a 2, 3, or 4
        "price": 3600, #between 1000 and 4000
    },
    "wolves": { #FOREST
        "description":"Here is a description of a grizzly bear!",
        "weather_prefs":{"overcast":0,"sunny":4,"rainy": -4,"stormy": -6}, #number between -10 and 10
        "diet":{ #numbers between -5 and 5
            "meat":{"taste": 4,"nutrition": 5,"price": price["food"]["meat"]},
            "grasses":{"taste": -4,"nutrition": 0, "price": price["food"]["grasses"]},
            "leaves":{"taste": -5, "nutrition": -2, "price": price["food"]["leaves"]},
            "fruit":{"taste": 50,"nutrition": 3, "price": price["food"]["fruit"]},
            "fish":{"taste": 5, "nutrition": 4, "price": price["food"]["fish"]} 
        },
        "lifespan":(20,25), #this is a tuple of min lifespan and max lifespan
        "popularity":95, #this should be a float between .8 and 1 (.8, .85, .9, .95, 1)
        "size":4, #capacity of habitat is 12. This should be a 2, 3, or 4
        "price": 3600, #between 1000 and 4000
    },
    "owls": { #FOREST
        "description":"Here is a description of a grizzly bear!",
        "weather_prefs":{"overcast":0,"sunny":4,"rainy": -4,"stormy": -6}, #number between -10 and 10
        "diet":{ #numbers between -5 and 5
            "meat":{"taste": 4,"nutrition": 5,"price": price["food"]["meat"]},
            "grasses":{"taste": -4,"nutrition": 0, "price": price["food"]["grasses"]},
            "leaves":{"taste": -5, "nutrition": -2, "price": price["food"]["leaves"]},
            "fruit":{"taste": 50,"nutrition": 3, "price": price["food"]["fruit"]},
            "fish":{"taste": 5, "nutrition": 4, "price": price["food"]["fish"]} 
        },
        "lifespan":(20,25), #this is a tuple of min lifespan and max lifespan
        "popularity":95, #this should be a float between .8 and 1 (.8, .85, .9, .95, 1)
        "size":4, #capacity of habitat is 12. This should be a 2, 3, or 4
        "price": 3600, #between 1000 and 4000
    },
    "giraffe": { #SAVANNA
        "description":"Here is a description of a grizzly bear!",
        "weather_prefs":{"overcast":0,"sunny":4,"rainy": -4,"stormy": -6}, #number between -10 and 10
        "diet":{ #numbers between -5 and 5
            "meat":{"taste": 4,"nutrition": 5,"price": price["food"]["meat"]},
            "grasses":{"taste": -4,"nutrition": 0, "price": price["food"]["grasses"]},
            "leaves":{"taste": -5, "nutrition": -2, "price": price["food"]["leaves"]},
            "fruit":{"taste": 50,"nutrition": 3, "price": price["food"]["fruit"]},
            "fish":{"taste": 5, "nutrition": 4, "price": price["food"]["fish"]} 
        },
        "lifespan":(20,25), #this is a tuple of min lifespan and max lifespan
        "popularity":95, #this should be a float between .8 and 1 (.8, .85, .9, .95, 1)
        "size":4, #capacity of habitat is 12. This should be a 2, 3, or 4
        "price": 3600, #between 1000 and 4000
    },
    "lion": { #SAVANNA
        "description":"Here is a description of a grizzly bear!",
        "weather_prefs":{"overcast":0,"sunny":4,"rainy": -4,"stormy": -6}, #number between -10 and 10
        "diet":{ #numbers between -5 and 5
            "meat":{"taste": 4,"nutrition": 5,"price": price["food"]["meat"]},
            "grasses":{"taste": -4,"nutrition": 0, "price": price["food"]["grasses"]},
            "leaves":{"taste": -5, "nutrition": -2, "price": price["food"]["leaves"]},
            "fruit":{"taste": 50,"nutrition": 3, "price": price["food"]["fruit"]},
            "fish":{"taste": 5, "nutrition": 4, "price": price["food"]["fish"]} 
        },
        "lifespan":(20,25), #this is a tuple of min lifespan and max lifespan
        "popularity":95, #this should be a float between .8 and 1 (.8, .85, .9, .95, 1)
        "size":4, #capacity of habitat is 12. This should be a 2, 3, or 4
        "price": 3600, #between 1000 and 4000
    },
    "rhino": { #SAVANA
        "description":"Here is a description of a grizzly bear!",
        "weather_prefs":{"overcast":0,"sunny":4,"rainy": -4,"stormy": -6}, #number between -10 and 10
        "diet":{ #numbers between -5 and 5
            "meat":{"taste": 4,"nutrition": 5,"price": price["food"]["meat"]},
            "grasses":{"taste": -4,"nutrition": 0, "price": price["food"]["grasses"]},
            "leaves":{"taste": -5, "nutrition": -2, "price": price["food"]["leaves"]},
            "fruit":{"taste": 50,"nutrition": 3, "price": price["food"]["fruit"]},
            "fish":{"taste": 5, "nutrition": 4, "price": price["food"]["fish"]} 
        },
        "lifespan":(20,25), #this is a tuple of min lifespan and max lifespan
        "popularity":95, #this should be a float between .8 and 1 (.8, .85, .9, .95, 1)
        "size":4, #capacity of habitat is 12. This should be a 2, 3, or 4
        "price": 3600, #between 1000 and 4000
    },
    "african_elephant": { #SAVANNA
        "description":"Here is a description of a grizzly bear!",
        "weather_prefs":{"overcast":0,"sunny":4,"rainy": -4,"stormy": -6}, #number between -10 and 10
        "diet":{ #numbers between -5 and 5
            "meat":{"taste": 4,"nutrition": 5,"price": price["food"]["meat"]},
            "grasses":{"taste": -4,"nutrition": 0, "price": price["food"]["grasses"]},
            "leaves":{"taste": -5, "nutrition": -2, "price": price["food"]["leaves"]},
            "fruit":{"taste": 50,"nutrition": 3, "price": price["food"]["fruit"]},
            "fish":{"taste": 5, "nutrition": 4, "price": price["food"]["fish"]} 
        },
        "lifespan":(20,25), #this is a tuple of min lifespan and max lifespan
        "popularity":95, #this should be a float between .8 and 1 (.8, .85, .9, .95, 1)
        "size":4, #capacity of habitat is 12. This should be a 2, 3, or 4
        "price": 3600, #between 1000 and 4000
    },
    "polar_bear": { #ARCTIC
        "description":"Here is a description of a grizzly bear!",
        "weather_prefs":{"overcast":0,"sunny":4,"rainy": -4,"stormy": -6}, #number between -10 and 10
        "diet":{ #numbers between -5 and 5
            "meat":{"taste": 4,"nutrition": 5,"price": price["food"]["meat"]},
            "grasses":{"taste": -4,"nutrition": 0, "price": price["food"]["grasses"]},
            "leaves":{"taste": -5, "nutrition": -2, "price": price["food"]["leaves"]},
            "fruit":{"taste": 50,"nutrition": 3, "price": price["food"]["fruit"]},
            "fish":{"taste": 5, "nutrition": 4, "price": price["food"]["fish"]} 
        },
        "lifespan":(20,25), #this is a tuple of min lifespan and max lifespan
        "popularity":95, #this should be a float between .8 and 1 (.8, .85, .9, .95, 1)
        "size":4, #capacity of habitat is 12. This should be a 2, 3, or 4
        "price": 3600, #between 1000 and 4000
    },
    "arctic_fox": { #ARCTIC
        "description":"Here is a description of a grizzly bear!",
        "weather_prefs":{"overcast":0,"sunny":4,"rainy": -4,"stormy": -6}, #number between -10 and 10
        "diet":{ #numbers between -5 and 5
            "meat":{"taste": 4,"nutrition": 5,"price": price["food"]["meat"]},
            "grasses":{"taste": -4,"nutrition": 0, "price": price["food"]["grasses"]},
            "leaves":{"taste": -5, "nutrition": -2, "price": price["food"]["leaves"]},
            "fruit":{"taste": 50,"nutrition": 3, "price": price["food"]["fruit"]},
            "fish":{"taste": 5, "nutrition": 4, "price": price["food"]["fish"]} 
        },
        "lifespan":(20,25), #this is a tuple of min lifespan and max lifespan
        "popularity":95, #this should be a float between .8 and 1 (.8, .85, .9, .95, 1)
        "size":4, #capacity of habitat is 12. This should be a 2, 3, or 4
        "price": 3600, #between 1000 and 4000
    },
    "penguins": { #ARCTIC
        "description":"Here is a description of a grizzly bear!",
        "weather_prefs":{"overcast":0,"sunny":4,"rainy": -4,"stormy": -6}, #number between -10 and 10
        "diet":{ #numbers between -5 and 5
            "meat":{"taste": 4,"nutrition": 5,"price": price["food"]["meat"]},
            "grasses":{"taste": -4,"nutrition": 0, "price": price["food"]["grasses"]},
            "leaves":{"taste": -5, "nutrition": -2, "price": price["food"]["leaves"]},
            "fruit":{"taste": 50,"nutrition": 3, "price": price["food"]["fruit"]},
            "fish":{"taste": 5, "nutrition": 4, "price": price["food"]["fish"]} 
        },
        "lifespan":(20,25), #this is a tuple of min lifespan and max lifespan
        "popularity":95, #this should be a float between .8 and 1 (.8, .85, .9, .95, 1)
        "size":4, #capacity of habitat is 12. This should be a 2, 3, or 4
        "price": 3600, #between 1000 and 4000
    },
    "tiger": { #JUNGLE
        "description":"Here is a description of a grizzly bear!",
        "weather_prefs":{"overcast":0,"sunny":4,"rainy": -4,"stormy": -6}, #number between -10 and 10
        "diet":{ #numbers between -5 and 5
            "meat":{"taste": 4,"nutrition": 5,"price": price["food"]["meat"]},
            "grasses":{"taste": -4,"nutrition": 0, "price": price["food"]["grasses"]},
            "leaves":{"taste": -5, "nutrition": -2, "price": price["food"]["leaves"]},
            "fruit":{"taste": 50,"nutrition": 3, "price": price["food"]["fruit"]},
            "fish":{"taste": 5, "nutrition": 4, "price": price["food"]["fish"]} 
        },
        "lifespan":(20,25), #this is a tuple of min lifespan and max lifespan
        "popularity":95, #this should be a float between .8 and 1 (.8, .85, .9, .95, 1)
        "size":4, #capacity of habitat is 12. This should be a 2, 3, or 4
        "price": 3600, #between 1000 and 4000
    },
    "orangutan": { #JUNGLE
        "description":"Here is a description of a grizzly bear!",
        "weather_prefs":{"overcast":0,"sunny":4,"rainy": -4,"stormy": -6}, #number between -10 and 10
        "diet":{ #numbers between -5 and 5
            "meat":{"taste": 4,"nutrition": 5,"price": price["food"]["meat"]},
            "grasses":{"taste": -4,"nutrition": 0, "price": price["food"]["grasses"]},
            "leaves":{"taste": -5, "nutrition": -2, "price": price["food"]["leaves"]},
            "fruit":{"taste": 50,"nutrition": 3, "price": price["food"]["fruit"]},
            "fish":{"taste": 5, "nutrition": 4, "price": price["food"]["fish"]} 
        },
        "lifespan":(20,25), #this is a tuple of min lifespan and max lifespan
        "popularity":95, #this should be a float between .8 and 1 (.8, .85, .9, .95, 1)
        "size":4, #capacity of habitat is 12. This should be a 2, 3, or 4
        "price": 3600, #between 1000 and 4000
    },
    "fruit_bats": { #JUNGLE
        "description":"Here is a description of a grizzly bear!",
        "weather_prefs":{"overcast":0,"sunny":4,"rainy": -4,"stormy": -6}, #number between -10 and 10
        "diet":{ #numbers between -5 and 5
            "meat":{"taste": 4,"nutrition": 5,"price": price["food"]["meat"]},
            "grasses":{"taste": -4,"nutrition": 0, "price": price["food"]["grasses"]},
            "leaves":{"taste": -5, "nutrition": -2, "price": price["food"]["leaves"]},
            "fruit":{"taste": 50,"nutrition": 3, "price": price["food"]["fruit"]},
            "fish":{"taste": 5, "nutrition": 4, "price": price["food"]["fish"]} 
        },
        "lifespan":(20,25), #this is a tuple of min lifespan and max lifespan
        "popularity":95, #this should be a float between .8 and 1 (.8, .85, .9, .95, 1)
        "size":4, #capacity of habitat is 12. This should be a 2, 3, or 4
        "price": 3600, #between 1000 and 4000
    },
    "asian_elephant": { #JUNGLE
        "description":"Here is a description of a grizzly bear!",
        "weather_prefs":{"overcast":0,"sunny":4,"rainy": -4,"stormy": -6}, #number between -10 and 10
        "diet":{ #numbers between -5 and 5
            "meat":{"taste": 4,"nutrition": 5,"price": price["food"]["meat"]},
            "grasses":{"taste": -4,"nutrition": 0, "price": price["food"]["grasses"]},
            "leaves":{"taste": -5, "nutrition": -2, "price": price["food"]["leaves"]},
            "fruit":{"taste": 50,"nutrition": 3, "price": price["food"]["fruit"]},
            "fish":{"taste": 5, "nutrition": 4, "price": price["food"]["fish"]} 
        },
        "lifespan":(20,25), #this is a tuple of min lifespan and max lifespan
        "popularity":95, #this should be a float between .8 and 1 (.8, .85, .9, .95, 1)
        "size":4, #capacity of habitat is 12. This should be a 2, 3, or 4
        "price": 3600, #between 1000 and 4000
    },
}
habitats = {
    "arctic":{
        "description": "Description of the artarctic",
        "price": 7000,
        "popularity": 70, #a percentage?
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
            current_weather = 2,
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
            new_animal = Animal.objects.create(self, breed, name)
            new_animal.location = (num_animals +1)
            self.inhabitants.add(new_animal)
        else:
            #message the user "You cannot!"
            pass


#### ANIMAL MANAGER
class AnimalManager(models.Manager):
    
    ## CREATE NEW ANIMAL
    def create_animal(self, habitat, breed, name):
        health = set_health(self)
        happiness = set_happiness(self)
        lifespan = set_lifespan(self, breed)
        age = set_age(self, breed, lifespan)
        description = set_description(self, breed)
        new_animal = self.create(
            age = age,
            name = name,
            health= health,
            happiness = happiness,
            breed = breed,
            lifespan = lifespan,
            popularity = animals[breed]["popularity"],
            size = animals[breed]["size"]
        )
        new_animal.set_habitat(self, breed)
        return new_animal


#### ANIMAL CLASS
class Animal(models.Model):
    age = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=255) #entered by user
    health = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
    happiness = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
    breed = models.CharField(max_length=55, choices=(
        ('grizzly_bear','grizzly_bear'),
        ('wolves','wolves'),
        ('owls','owls'),
        ('giraffe','giraffe'),
        ('lion','lion'),
        ('rhino','rhino'),
        ('african_elephant','african_elephant'),
        ('polar_bear','polar_bear'),
        ('arctic_fox','arctic_fox'),
        ('penguins','penguins'),
        ('tiger','tiger'),
        ('orangutan','orangutan'),
        ('fruit_bats','fruit_bats'),
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
        
# ANIMAL INITAILIATIONS
    def set_age(self, breed, lifespan):
        age = random.randint(1,(lifespan/2))
        return age

    def set_health(self):
        health = random.randint(60,95)
        return health
    
    def set_happiness(self):
        happiness = random.randint(60,95)
        return happiness
    
    def set_habitat(self, habitat):
        self.habitat = habitat
        self.save()
        return self

    def set_lifespan(self, breed):
        animal_prefs = animal[breed] #a dictionary of animal prefs
        min = animal_prefs["lifespan"][0]
        max = animal_prefs["lifespan"][1]
        lifespan = random.randint(min, max)
        return lifespan

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