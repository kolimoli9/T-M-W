from .models import Countries,Customers,CustomerService,Flights,Airlines,Tickets
from django.contrib.auth.models import User


class GETS:
    def __init__(self) -> None:
        pass
    
    def customer_by_user(id):
        try:
            user = User.objects.get(id=id)
            temp = Customers.objects.get(user=user)
            customer = {
                "id":temp.id,
                "first_name":temp.first_name,
                "last_name":temp.last_name,
                "adress":temp.adress,
                "credit":temp.credit_num,
                "phone":temp.phone,
                "user_id":temp.user.id
            }
            return customer
        except:
            return False    

    def airline_by_user(id):
        try:    
            user = User.objects.get(id=id)
            temp = Airlines.objects.get(user=user)
            airline ={
                "id": temp.id,
                "airline_name":temp.airline_name,
                "airline_user":temp.user
            } 
            return airline 
        except:
            return False    
    def ticket_by_user(id):
        try:
            user = User.objects.get(id=id)
            customer = Customers.objects.get(user=user)
            temp = Tickets.objects.get(customer = customer.id)
            ticket = {
                "id":temp.id,
                "customer_id":temp.customer,
                "flight_id":temp.flight
            }
            return ticket
        except:
            return False
    
    def flight_by_ticket(id):
        ticket = Tickets.objects.get(id=id)
        temp = Flights.objects.get(id=ticket.flight)
        dep =str(temp.dep_time)
        dep_time = dep[10: ]
        dep_date = dep[0:10]
        arrival = str(temp.arrival_time)
        arrival_time = arrival[10: ]
        arrival_date = arrival[0:10]
        flight = {
            "id":temp.id,
            "airline":temp.airlineID,
            "origin_country":temp.origin_country,
            "destenation_country":temp.destenation_country,
            "dep_time":dep_time,
            "dep_date":dep_date,
            "arrival_time":arrival_time,
            "arrival_date":arrival_date,
            "tickets_left":temp.tickets_left
        }    
        return flight 


class ALLS:
    def __init__(self) -> None:
        pass

    def tickets_by_customer(id):
        tickets = []
        all = Tickets.objects.all(customer=id)
        try:
            for one in all:
                ticket =  {
                    "id":one.id,
                    "customer_id":one.customer,
                    "flight_id":one.flight,
                    "created":one.created
                }
                tickets.append(ticket)
            return tickets    
        except:
            return False       
                         