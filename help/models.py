from __future__                              import unicode_literals
from django.utils.encoding                   import python_2_unicode_compatible
from django.db                               import models
from django.contrib.auth.models              import User
from django.utils import timezone
from django import forms

class Counter(models.Model):
    date = models.DateField(auto_now = True)
    count = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.date)

class Profile(models.Model):
    user      = models.OneToOneField(User)
    address   = models.CharField(max_length = 30)
    telephone = models.CharField(max_length = 30)
    image     = models.ImageField(upload_to = "images", blank = True)

    def __str__(self):
        return str(self.user)

@python_2_unicode_compatible
class Order(models.Model):
    profile    = models.ForeignKey(Profile)
    problem    = models.CharField(max_length=30)
    telephone  = models.CharField(max_length = 10)
    status     = models.BooleanField(default = True)
    pub_date   = models.DateTimeField('date published')

    def __str__(self):
        return self.telephone

class Comment(models.Model):
    comment_text = models.CharField(max_length = 30)
    order        = models.ForeignKey(Order)
