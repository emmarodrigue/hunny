from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ImageDraw
from datetime import datetime

class Profile(models.Model):
    # gender choices
    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
        ('NB', 'Nonbinary')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, null=True)
    birthday = models.DateField(default=None, blank=True, null=True)
    bio = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='static/profile_pics')

    objects = models.Manager()

    def __str__(self):
        return self.user.username

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 90 or img.width > 90:
            output_size = (90, 90)
            img.thumbnail(output_size)
            img.save(self.image.path)

    @property
    def age(self):
        return int((datetime.now().date() - self.birthday).days / 365.25)

class Room(models.Model):
    capacity = 0
    name = models.CharField("roomname", max_length = 120)
    chatter = models.CharField("roomname", max_length = 120)
    messages = models.TextField(blank= True)

    def __str__(self):
        return self.name
