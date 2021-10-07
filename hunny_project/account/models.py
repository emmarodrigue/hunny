from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ImageDraw

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    age = models.CharField(max_length=3)
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