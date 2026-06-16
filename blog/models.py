from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey (User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title   



class WeatherData(models.Model):
    city = models.CharField(max_length= 100)
    temperature = models.FloatField()
    description = models.CharField (max_length= 200)
    fetched_at = models.DateTimeField (auto_now_add= True)
    
    
    def __str__(self):
        return f"{self.city} - {self.temperature}°C"