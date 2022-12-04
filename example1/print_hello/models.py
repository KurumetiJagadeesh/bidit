from django.db import models

# Create your models here.

class Destination(models.Model):
    name =models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc= models.TextField()
    price=models.IntegerField()
    ptype=models.CharField(max_length=50)
    specications=models.TextField()

class product1Bidding(models.Model):
    username = models.CharField(max_length=100)
    rating=models.IntegerField()
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
    bprice = models.IntegerField()

class product2Bidding(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
    bprice = models.IntegerField()

class product3Bidding(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
    bprice = models.IntegerField()

class product4Bidding(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
    bprice = models.IntegerField()

class product5Bidding(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
    bprice = models.IntegerField()

class product6Bidding(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
    bprice = models.IntegerField()

class product7Bidding(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
    bprice = models.IntegerField()

