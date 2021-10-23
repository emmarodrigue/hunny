from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ImageDraw

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    age = models.CharField(max_length=3)
    age_range = models.CharField(max_length=10, default=0000000000)
    match_radius = models.CharField(max_length=7, default=0000000)
    bio = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='static/profile_pics')

    def __str__(self):
        return self.user.username

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 90 or img.width > 90:
            output_size = (90, 90)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Room(models.Model):
    capacity = 0
    name = models.CharField("roomname", max_length = 120)
    chatter = models.CharField("roomname", max_length = 120)
    messages = models.TextField(blank= True)

    def __str__(self):
        return self.name
