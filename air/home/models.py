from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class airlines(models.Model):
    Airline_id = models.IntegerField(primary_key=True, serialize=True)
    name = models.CharField(max_length=50)
    afrom = models.CharField(max_length=15)
    ato = models.CharField(max_length=15)
    time= models.DateField(default=timezone.now())

    def __str__(self):
        return self.name


class User(models.Model):
    User_id = models.CharField(max_length=12, primary_key=True, serialize=True)
    Name = models.CharField(max_length=30)
    phone_no = models.BigIntegerField(unique=True)

    def __str__(self):
        return self.Name


class bookticket(models.Model):
    transaction_id = models.AutoField(primary_key=True, serialize=True)
    User_id = models.CharField(max_length=12)
    Airline_id = models.CharField(max_length=5)
    issue_date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.User_id
