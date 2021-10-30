from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ImageDraw
from django.dispatch import receiver
from django.db.models.signals import post_save



class Room(models.Model):
    capacity = 0
    name = models.CharField("roomname", max_length = 120)
    chatter = models.CharField("roomname", max_length = 120)
    messages = models.TextField(blank= True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User,related_name='userprofile', on_delete=models.CASCADE) #lilly_note
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    age = models.CharField(max_length=3)
    age_range = models.CharField(max_length=10, default=0000000000)
    match_radius = models.CharField(max_length=7, default=0000000)
    bio = models.TextField()
    image = models.ImageField(default='images/signup.jpg', upload_to='static/hunny_app/profile_pics')

#lilly_note
    matches = models.ManyToManyField(User, related_name='matches', blank=True)
    who_like_me = models.ManyToManyField(User, related_name='who_like_me', blank=True)
    current_check = models.IntegerField(default=0)
    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def next_check(self):
        super().save()
        self.current_check = "dosomethinghere"
        return self.current_check

    def get_all_matches(self):
        return self.matches.all()

    def get_matches_count(self):
        return self.matches.all().count()

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



