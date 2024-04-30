
from django.db import models
from django.contrib.auth.models import User

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    carbohydrates_total_g = models.FloatField()
    fat_total_g = models.FloatField()
    protein_g = models.FloatField()
    sodium_mg = models.FloatField()
    sugar_g = models.FloatField()

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    gender = models.CharField(max_length=10,default='male')
    age = models.IntegerField(default=18)

    def __str__(self):
        return self.user.username
