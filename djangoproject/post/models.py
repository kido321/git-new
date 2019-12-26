from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    name = models.CharField(max_length=25)
    price = models.FloatField(max_length=25)
    stock = models.IntegerField()
    image_url = models.CharField(max_length=1000)




class Offers(models.Model):
    discount= models.CharField(max_length=23)
    any_thing_to_say=models.CharField(max_length=34)

class Todo(models.Model):
    added_date=models.DateTimeField()
    added_text=models.CharField(max_length=50)

class user(models.Model):
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=1000)
class Fb(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

'''class Userpinfo(models.Model):

    user1=models.OneToOneField(User , on_delete=models.PROTECT)

    portfolio=models.CharField(blank=True)
    propic=models.ImageField(blank=True,upload_to='propic')

    def _str__(self):
        return self.user1.username'''


class Schools(models.Model):
    name = models.CharField(max_length=123)
    location = models.CharField(max_length=123)





