from django.db import models
import datetime

from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    birth_date = models.DateField()
    following = models.ManyToManyField("users.User", related_name="follower")
    block = models.ManyToManyField("users.User", related_name="blocked")
    is_female = models.BooleanField(default=False)

    @property
    def age(self):
        return (datetime.date.today() - self.birth_date).days / 365.245


class UserProfile(models.Model):
    # avatar
    # header
    user = models.OneToOneField("users.User", on_delete=models.CASCADE, related_name="profile")
    nickname = models.CharField(max_length=64)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=32, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    is_private = models.BooleanField(default=False)






