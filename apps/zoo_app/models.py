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
events:{
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
        owner.money -= 35000
        owner.save()
        return new_zoo

    def add_exhibit_validator(self, postData):
        pass

    #change_ticket_price_validator(self, postData):
        
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

    def get_random_animal(self):
            all_animals = []
            count = 0
            all_exhibits = self.exhibits.all()
            for exhibit in all_exhibits:
                all_inhabitants=exhibit.inhabitants.all()
                for inhabitant in all_inhabitants:
                    all_animals.append(inhabitant)
                    count = count + 1
            index = random.randint(0,count-1)
            random_animal = all_animals[index]
            return random_animal

    # def event_resolutions(self):
    #     all_events = self.events.all()
    #     messages=[]
    #     for event in all_events:
    #         if event.resolution_day == self.user.day:
    #             event.resolve()
    #     return messages

    def zoo_popularity(self):
        if self.exhibits.count() == 0:
            return 0
        else:
            exhibits = self.exhibits.all()
            total = 0
            for exhibit in exhibits:
                total = total + exhibit.attractiveness()
            total = total//self.exhibits.count()
            total = total * (-3*self.ticket_price+115)//100
            if total<0:
                total=0
            return total  #total = number between 0 and 100

    def change_ticket_price(self, price):
        self.tomorrows_ticket_price = price
        self.save()
        return self
    
    def average_happiness(self):
        exhibits = self.exhibits.all()
        num_animals = 0
        total_happiness = 0
        for exhibit in exhibits:
            num_animals = num_animals + exhibit.inhabitants.count()
            all_animals = exhibit.inhabitants.all()
            for animal in all_animals:
                total_happiness = total_happiness+animal.happiness
        if num_animals==0:
            average_happiness=0
        else:
            average_happiness = total_happiness//num_animals
        return average_happiness
 
    def average_health(self):
        exhibits = self.exhibits.all()
        num_animals = 0
        total_health = 0
        for exhibit in exhibits:
            num_animals = num_animals + exhibit.inhabitants.count()
            all_animals = exhibit.inhabitants.all()
            for animal in all_animals:
                total_health = total_health+animal.health
        if num_animals==0:
            average_health=0
        else:
            average_health = total_health//num_animals
        return average_health
        
    #ADD EXHIBIT TO ZOO
    def add_exhibit(self, climate, name, location):
        # if self.owner.moeny>habitats[climate]["price"]
        new_exhibit = Habitat.objects.create_habitat(self, climate, name, location)
        self.exhibits.add(new_exhibit)
        self.owner.money = self.owner.money - habitats[climate]["price"]
        self.owner.save()
        return new_exhibit

    def advance_day(self):
        all_exhibits = self.exhibits.all()
        for exhibit in all_exhibits:
            for animal in exhibit.inhabitants.all():
                animal.day_end()
                animal.save()
        self.update_weather()
        self.save()
        count = 0
        messages = []
        for exhibit in all_exhibits:
            for animal in exhibit.inhabitants.all():
                animal.day_start()
                animal.age = animal.age+1
                animal.save()
                death = death_check(animal)
                if death != False:
                    messages.append(death)
                count = count + 1
        # for event in self.run_events()
        #     messages.append(event)
        # self.event_resolutions()
        messages.append("The average happiness of your animals is " + str(self.average_happiness())+".")
        messages.append("The average health of your animals is " + str(self.average_health())+".")
        factor = (self.average_happiness())*(self.average_health())//100
        daily_visitors = self.zoo_popularity() *factor *count//self.exhibits.count()
        return {"daily_visitors": daily_visitors, "weather": self.get_weather_display(), "messages":messages}

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
    def attractiveness(self):
        attractiveness = habitats[self.climate]["popularity"]
        if self.inhabitants.count()==0:
            return 0
        else:
            animals = self.inhabitants.all()
            total = 0
            for animal in animals:
                total=total + animal.attractiveness()
            total = total//self.inhabitants.count()
            total = total*attractiveness/100
            return attractiveness #returns a 1-100 number

    def how_full(self):
        all_animals = self.inhabitants.all()
        fullness = 0
        for inhabitant in all_animals:
            fullness = fullness + inhabitant.size
        return fullness

#ADD ANIMAL TO HABITAT
    def add_animal(self, breed, name):
        num_animals = self.inhabitants.count()
        occupants = self.inhabitants.all()
        how_full = 0
        for animal in occupants:
            how_full = how_full + animal.size
        if animals[breed]["size"] <= (self.capacity-how_full):
            new_animal = Animal.objects.create_animal(self, breed, name)
            self.zoo.owner.money = self.zoo.owner.money - animals[breed]["price"]
            self.zoo.owner.save()
            new_animal.location = (num_animals +1)
            self.inhabitants.add(new_animal)
            return self
        else:
            return False


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
        ('grizzly_bear','Grizzly Bear'),
        ('wolf','Wolf'),
        ('owl','Owl'),
        ('giraffe','Giraffe'),
        ('lion','Lion'),
        ('rhino','Rhino'),
        ('african_elephant','African Elephant'),
        ('polar_bear','Polar Bear'),
        ('arctic_fox','Arctic Fox'),
        ('penguin','Penguin'),
        ('tiger','Tiger'),
        ('orangutan','Orangutan'),
        ('fruit_bat','Fruit Bat'),
        ('asian_elephant','Asian Elephant'),
    ))
    lifespan =  models.PositiveSmallIntegerField()
    popularity = models.PositiveSmallIntegerField()
    size = models.PositiveSmallIntegerField()
    habitat = models.ManyToManyField(Habitat, related_name = "inhabitants")
    location = models.PositiveSmallIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AnimalManager()

## ANIMAL METHODS
    def attractiveness(self):
        attractiveness = int((self.health + self.happiness)/2)*(self.popularity/100)
        return attractiveness # a number between 0 and 100
    
    def death_check(self):
        if self.age>=self.lifespan:
            dead = self.die()
            message = "Your "+ str(dead[0]) + " "+str(dead[1])+" has died of old age."
            return message
        elif self.health == 0:
            dead = self.die()
            message = "Your "+ str(dead[0]) + " "+str(dead[1])+" has died of malnutrition."
            return message
        elif self.happiness == 0:
            dead = self.die()
            message = "Your "+ str(dead[0]) + " "+str(dead[1])+" has died of sadness."
            return message
        else:
            return False

    def die(self):
        death = [self.breed, self.name]
        self.delete()
        return death
    
    def display_age(self):
        return self.age//50

#DAY POST
    def day_start(self):
        self.happiness = self.happiness + animals[self.breed]["weather_prefs"][self.habitat.zoo.get_weather_display()]
        self.health = self.health - random.randint(2,5)
        self.happiness = self.happiness - random.randint(2,5)
        self.validate_health().validate_happiness()
        self.save()
        return self

    def day_end(self): #animal.advance_day
        self.happiness = self.happiness - animals[self.breed]["weather_prefs"][self.habitat.zoo.get_weather_display()]
        self.validate_health().validate_happiness()
        self.save()
        return self

    def validate_health(self):
        if self.health>100:
            self.health=100
        if self.health<0:
            self.health=0
        self.save()
        return self

    def validate_happiness(self):
        if self.happiness>100:
            self.happiness=100
        if self.happiness<0:
            self.happiness=0
        self.save()
        return self

#FEED POST
    def feed(self, food):
        meal = animals[self.breed]["diet"][food]
        self.happiness = self.happiness + meal["taste"]
        self.health = self.health + meal["nutrition"]
        self.validate_health().validate_happiness()
        self.save()
        self.habitat.zoo.owner.money = self.habitat.zoo.owner.money - meal["price"]
        self.habitat.zoo.owner.save()
        death = self.death_check()
        if death == False:
            return self.feed_message(food, meal["taste"], meal["nutrition"])
        else:
            return death

    def feed_message(self, food, taste, nutrition):
        pet = self.get_breed_display()
        message = ""
        if taste ==5:
            message = "Your "+pet +" loves " +food+ "!"
        if taste ==4:
            message = "Your "+pet +" really likes " +food+ "."
        if taste ==3:
            message = "Your "+pet +" likes " +food+ "."
        if taste ==2:
            message = "Your "+pet +" is ok with " +food+ "."
        if taste ==1:
            message = "Your "+pet +" tolerates " +food+ "."
        if taste ==0:
            message = "Your "+pet +" doesn't prefer " +food+ "."
        if taste ==-1:
            message = "Your "+pet +" dislikes " +food+ "."
        if taste ==-2:
            message = "Your "+pet +" dislikes " +food+ "."
        if taste ==-3:
            message = "Your "+pet +" really dislikes " +food+ "."
        if taste ==-4:
            message = "Your "+pet +" really dislikes " +food+ "."
        if taste ==-5:
            message = "Your "+pet +" hates " +food+ "!"

        if nutrition ==5:
            message = message + " It keeps them extremely healthy!"
        if nutrition ==3 or nutrition == 4:
            message = message + " It's good for their health."
        if nutrition ==1 or nutrition ==2:
            message = message + " It is a little healthy for them."
        if nutrition ==0:
            message = message + " It's had no effect on their health."
        if nutrition ==-1 or nutrition ==-2:
            message = message + " It's not very good for them."
        if nutrition ==-3 or nutrition ==-4:
            message = message + " It's upset their stomach.:("
        if nutrition ==-5:
            message = message + " It has made them sick!"
        return message

    def description(self):
        description = animals[self.breed]["description"]
        return description

###EVENTS

class EventManager(models.Manager):
    pass

class Event(models.Model):
    zoo = models.ForeignKey(Zoo, related_name="events")
    name =  models.CharField(max_length=255)
    day = models.PositiveSmallIntegerField(null=True)
    resolution_day = models.PositiveSmallIntegerField(null=True)
    exhibits = models.ManyToManyField(Habitat, related_name = "events")
    affected_animals = models.ManyToManyField(Animal, related_name = "events")
    event_data1 = models.PositiveSmallIntegerField(null=True)
    event_data2 = models.PositiveSmallIntegerField(null=True)
    event_data3 = models.PositiveSmallIntegerField(null=True)
    event_message = models.TextField()
    resolution_message = models.TextField()
    objects = EventManager()

    def escapee(self, zoo): #removes an animal from the zoo and stores it to add later
        escapee = zoo.get_random_animal()
        ###fix resoluation_day
        resolution_day = 3
        event_message = "Your "+ escapee.breed +", "+escapee.name +", has escaped from the zoo!!"
        resolution_message = "Your "+ escapee.breed +", "+escapee.name +", has been found and returned to the zoo."
        Event.objects.create(
            zoo = zoo,
            name = escapee.breed+ " Escape!",
            day = zoo.owner.day,
            resolution_day = resolution_day,
            affected_animals = escapee,
            event_message = event_message,
            resolution_message = resolution_message
        )
        escapee.habitat.remove()
        return self

    def resolve(self):
        all_events = self.zoo.events.all()
        messages=[]
        for event in all_events:
            if self.resolution_day == self.zoo.user.day:
                self.resolve()


    # def run_events(self)
        #break out - ticket sales got down and an animal gets deleted
            #maybe the animal gets found
         #--need to store name of event
        # all_animals=
        #escapee = 
        #all the animals got a cold - animals are less healthy
        #school field trip day - more ticket sales
        #the zoo recived an anonymous donation from a mysterious benefactor
        #an animal birth!
        #fish is on sale today
        #shortage of fish
        #a visitor was eaten yesterday by a certain animal - that animals happiness goes to max, but ticket sales plummet for a day

    # def run_event_resolutions(self):
