from allergies.models import Allergy
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ("restaurant", "Restaurant"),
        ("patient", "Patient"),

    ]
    allergies= models.ManyToManyField(Allergy)

    # Store user token after login that is currently stored in session

    role = models.CharField(choices= ROLE_CHOICES, max_length=255 , null = True)

class Restaurant(models.Model):
    name = models.CharField(max_length=255, null = True)
    location = models.CharField(max_length=255, null = True)
    description = models.CharField(max_length=500, null = True)
    phone_number= models.CharField(max_length=15 , null = True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'restaurant'}, null = True)
    def __str__(self):
        return self.name
class Menu_Section(models.Model):
    title = models.CharField(max_length=255 , null = True)
    def __str__(self):
        return self.title
class Menu(models.Model):
    name = models.CharField(max_length=255 , null = True)
    sections = models.ManyToManyField(Menu_Section)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus', null=True)
    def __str__(self):
        return self.name

class Food_Allergen(models.Model):
    ALLERGY_CHOICES = [
        ("milk", "Milk"),
        ("eggs", "Eggs"),
        ("shellfish", "Shellfish"),
        ("treenuts", "Treenuts"),
        ("peanuts", "Peanuts"),
        ("wheat", "Wheat"),
        ("soybeans", "Soybeans"),
        ("sesame", "Sesame"),
        ("fish", "Fish"),
        ("nuts", "Nuts")

    ]

    allergen = models.CharField(choices=ALLERGY_CHOICES, max_length=255, null=True)

    def __str__(self):
        return self.allergen

class Food(models.Model):
    name =  models.CharField(max_length=255 , null = True)
    allergies = models.ManyToManyField(Food_Allergen)
    section=models.ForeignKey(Menu_Section, on_delete=models.CASCADE, null = True)
    def __str__(self):
        return self.name
# Todo list: 7/26 - 8/16
# - complete allergy model :)
#      - more methods (urls/views) to manage allergies (editing/deleting) - only allergist - check session before doing operation
#                                                                                          - the users model can also have built-in methods that the allergy methods call/use themselves
# - complete users methods that will let them edit info on the edit page
#       - Store patient information in users model that people put themselves
# - Check out Postman application that is helpful when debugging methods
# - Restuarants model/ create,update,fetch, delete :)
# - Menu Section model, create, update, fetch, delete
# - restaurant id/ many to many field

