from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ImageDraw
from datetime import datetime

# print all users in DB cmd line
all_users = User.objects.values()
print(all_users)
print(all_users[0]['username'])

class Profile(models.Model):
    # gender choices
    GENDER_CHOICES = [
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Nonbinary', 'Nonbinary')
    ]
    # gender preference choices
    PREFERRED_GENDER_CHOICES = [
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('No Preference', 'No Preference')
    ]
    # children preference choices
    CHILDREN_CHOICES = [
        ('Children are a dealbreaker', 'Children are a dealbreaker'),
        ('Looking for children in the future', 'Looking for children in the future'),
        ('Prefer someone with children', 'Prefer someone with children'),
        ('No Preference', 'No Preference')
    ]
    # relationship type choices
    RELATIONSHIP_CHOICES = [
        ('Casual Dating', 'Casual Dating'),
        ('Serious Relationship', 'Serious Relationship'),
        ('Dating', 'Dating'),
        ('No Preference', 'No Preference')
    ]
    # user's public profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, null=True, blank=True)
    birthday = models.DateField(default=None, blank=True, null=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(default='default.jpg', upload_to='static/profile_pics', blank=True)

    # user's preferences
    gender_preference = models.CharField(max_length=100, choices=PREFERRED_GENDER_CHOICES, null=True, blank=True)
    children_preference = models.CharField(max_length=100, choices=CHILDREN_CHOICES, null=True, blank=True)
    relationship_preference = models.CharField(max_length=100, choices=RELATIONSHIP_CHOICES, null=True, blank=True)
    age_range = models.CharField(max_length=100, null=True, blank=True)
    match_radius = models.CharField(max_length=100, help_text='miles', blank=True)

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