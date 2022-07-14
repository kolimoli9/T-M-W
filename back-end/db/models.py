from datetime import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# DB Tables

class Countries(models.Model):
    country_name = models.CharField(max_length=200)
    flag = models.ImageField(upload_to='media/', height_field=None, width_field=None, max_length=100)
    def __str__(self):
        return self.country_name

class Airlines(models.Model):
    country_id = models.ForeignKey(Countries, on_delete=models.CASCADE)
    airline_name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.airline_name
        
class Customers(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    adress = models.CharField(max_length=10)
    phone = models.IntegerField(default=10)
    credit_num= models.IntegerField(default=16)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.first_name

class Flights(models.Model):
        airlineID= models.ForeignKey(Airlines, on_delete=models.CASCADE)
        origin_country = models.ForeignKey(Countries,related_name= "country" ,on_delete=models.CASCADE)
        destenation_country = models.ForeignKey(Countries,related_name="destenation"  ,on_delete=models.CASCADE)
        dep_time = models.DateTimeField('Departure Time')
        arrival_time = models.DateTimeField('Arrival Time')
        tickets_left= models.IntegerField(default=50)
        def __str__(self):
            flight_name = str(self.origin_country)+'=>'+str(self.destenation_country)+f'({self.dep_time})'
            return flight_name

class Tickets(models.Model):
        flight = models.ForeignKey(Flights, on_delete=models.CASCADE)
        customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
        created = models.DateTimeField(auto_now=True)
        def __str__(self):
            ticket =  str(self.customer_id) +'>>'+'Flight: ' + str(self.flight_id)
            return ticket

class CustomerService(models.Model):
    _from = models.CharField(max_length=20)
    _about = models.TextField(default='')
    _content = models.TextField(default='')
    _received = models.DateTimeField(auto_now=True)
    _reply_sent = models.DateTimeField()








class Test(models.Model):
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=20)        


