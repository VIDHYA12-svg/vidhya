from django.db import models

class Admin(models.Model):

       username = models.CharField(max_length=30,unique=True)
       password = models.CharField(max_length=30)

class Merchant(models.Model):
    idno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    contantno = models.IntegerField()
    email_id = models.EmailField(unique=True)
    password = models.CharField(max_length=30)

class Product(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.FloatField()
    quantity = models.IntegerField()
