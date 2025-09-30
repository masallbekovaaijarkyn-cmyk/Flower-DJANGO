from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        blank=True,
        upload_to='profile_pics'
                               )
    bio = models.TextField(
        blank=True,
        null=True,
        verbose_name="О себе",
    )
    def __str__(self):
        return self.user.username

