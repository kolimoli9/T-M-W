from django.contrib import admin
from .models import Countries, Airlines, CustomerService, Test,Customers, Flights, Tickets
# Register your models here.
admin.site.register(Countries)
admin.site.register(Airlines)
admin.site.register(Customers)
admin.site.register(Flights)
admin.site.register(Tickets)
admin.site.register(Test)
admin.site.register(CustomerService)
