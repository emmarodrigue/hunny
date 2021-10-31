from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ImageDraw
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime



class Room(models.Model):
    capacity = 0
    name = models.CharField("roomname", max_length = 120)
    chatter = models.CharField("roomname", max_length = 120)
    messages = models.TextField(blank= True)

    def __str__(self):
        return self.name


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

    user = models.OneToOneField(User,related_name='userprofile', on_delete=models.CASCADE) #lilly_note
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, null=True, blank=True)
    birthday = models.DateField(default=None, blank=True, null=True)
    bio = models.TextField()
    image = models.ImageField(default='images/signup.jpg', upload_to='static/hunny_app/profile_pics')
 # user's preferences
    gender_preference = models.CharField(max_length=100, choices=PREFERRED_GENDER_CHOICES, null=True, blank=True)
    children_preference = models.CharField(max_length=100, choices=CHILDREN_CHOICES, null=True, blank=True)
    relationship_preference = models.CharField(max_length=100, choices=RELATIONSHIP_CHOICES, null=True, blank=True)
    age_range = models.CharField(max_length=100, null=True, blank=True)
    match_radius = models.CharField(max_length=100, help_text='miles', blank=True)
    objects = models.Manager()
#lilly_note
    matches = models.ManyToManyField(User, related_name='matches', blank=True)
    who_like_me = models.ManyToManyField(User, related_name='who_like_me', blank=True)
    current_check = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        # img = Image.open(self.image.path)
        # if img.height > 300 or img.width > 300:
            # output_size = (300,300)
            # img.thumbnail(output_size)
            # img.save(self.image.path)

    def next_check(self):
        super().save()
        self.current_check = "dosomethinghere"
        return self.current_check

    def get_all_matches(self):
        return self.matches.all()

    def get_matches_count(self):
        return self.matches.all().count()

    @property
    def age(self):
        return 30

#lilly_note
@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.userprofile.save()



STATUS_CHOICES = (('match2', 'match2'), ('match2', 'match2'),)

class MatchRequest(models.Model):
    sender = models.ForeignKey(Profile, related_name="sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(Profile, related_name="receiver", on_delete=models.CASCADE)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"



