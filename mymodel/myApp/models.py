from email.policy import default
from django import forms
from django.db import models
from django import forms
from django.db.models import Model

import datetime


class Post(models.Model):
    # title=models.CharField(max_length=20)
    # text=models.TextField()

    # Auth_detail=models.TextField(null=True)
    # date=models.DateField(max_length=20, null=True)

    image = models.ImageField(upload_to = "images/",default="some string")
    # def __str__(self):
    #     return self.title
