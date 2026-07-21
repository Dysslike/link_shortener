from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# allow users to be able to create an account, storing Username, Name, Email, Birth date,
# Password, and it will also store the link that they want to shorten and connect it through a
# shortened version of the link, logs when they added, logs how many has visited the link,

class Link(models.Model):
    link_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_url = models.URLField(max_length=255)
    short_url = models.URLField(max_length=255,unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    visits = models.BigIntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.short_url