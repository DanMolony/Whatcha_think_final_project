from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class FilmPoster(models.Model):
    poster = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="images/" )

    def __str__(self):
        return f'{self.poster.username} Film'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

