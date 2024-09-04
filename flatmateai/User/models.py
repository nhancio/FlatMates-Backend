from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):

    GENDER_CHOICE =(('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'))
    FOOD_CHOICE = (("Veg","Veg"),("Non-Veg","Non-Veg"))

    phone_number = models.CharField(max_length=100,primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, blank=False)
    age = models.PositiveIntegerField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    food_choice = models.CharField(max_length=100, blank=True, choices=FOOD_CHOICE)  # Can be refined with more specific choices if needed
    drinking = models.BooleanField(default=False)
    smoking = models.BooleanField(default=False)
    pet = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}'s profile"


class RoomDetails(models.Model):

    ROOM_TYPE = (("1RK","1RK"),("1BHK","1BHK"),("2BHK","2BHK"),("3BHK","3BHK"))
    BUILDING_TYPE = (("Individual","Individula"), ("Apartment","Apartment"), ("Villa","Villa"))

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='RoomDetails')
    #phone_number = models.CharField(max_length=100,primary_key=True)
    location = models.CharField(max_length=100)
    rent = models.PositiveBigIntegerField()
    room_type = models.CharField(max_length=100, choices=ROOM_TYPE)
    building_type = models.CharField(max_length=100, choices=BUILDING_TYPE)
