from datetime import *
from random import choice
from django.conf import settings
from django.http import  JsonResponse
from .models import Countries, Airlines, CustomerService, PermissionRequests, Test, Customers, Flights, Tickets 
from rest_framework.decorators import api_view,permission_classes
from .Serializers import AirlinesSerializer,CountriesSerializer,CustomersSerializer,FlightsSerializer,TicketsSerializer,UserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.contrib.auth.hashers import make_password, check_password
from django.core import mail
from django.contrib.auth.models import User
from .utils import GETS







# CUSTOM TOKEN
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        token['is_staff']=user.is_staff
        token['first_name'] = user.first_name
        token['last_name']=user.last_name
        if user.is_staff:
            try:airline = Airlines.objects.get(user=user.id);token['airline'] = airline.airline_name
            except:pass
        if user.is_superuser:token['is_admin'] = user.is_superuser     
        return token
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



# CONTACT US
@api_view(['POST'])
def contact(r):
    EMAIL =r.data['EMAIL']
    connection = mail.get_connection()
    SendEmail1 =mail.EmailMessage(
                f'Subject >> {r.data["SUBJECT"]}|| From User: {r.data["NAME"]}',
                f'Message: \n {r.data["MESSAGE"]}',
                settings.DEFAULT_FROM_EMAIL,
                ['kolimoli9@gmail.com'],
                connection=connection,)  
    SendEmail1.send()
    SendEmail2 =mail.EmailMessage(
                f'Thank You For Reacing Out!',
                f'Hello {r.data["NAME"]} , \n We received your message and we are attending to it \n RIGHT NOW ! \n We`ll get back to you shortly, thank you for the wait. \n -The Milky Way- corp',
                settings.DEFAULT_FROM_EMAIL,
                [EMAIL],
                connection=connection,)  
    SendEmail2.send()
    connection.close()
    CustomerService.objects.create(_from=EMAIL ,_about= r.data["SUBJECT"],_content=r.data["MESSAGE"] ,_received= datetime.now(),_reply_sent= datetime.now())
    return JsonResponse({'message': 'Thank u for contacting us \n We will get back to you as soon as possible!'},safe=False)        



# FORGOT PASSWORD
@api_view(['POST'])
def forgot_password(r):
    if r.method == 'POST':
        email = r.data['email']
        try:
            user = User.objects.get(email=email)
        except:
            return JsonResponse({'message': 'Error 404 ,This User Is Not In The System!'})
        randompwd = ''.join([choice('1234567890qwertyuiopasdfghjklzxcvbnm') for i in range(8)])
        user.password = make_password(randompwd)
        user.save()
        connection = mail.get_connection()
        SendEmail =mail.EmailMessage(
                    'FORGOT PASSWORD',
                    f'Hi there {user.first_name},  \n We heard that you`ve misplaced your password :) \n your new password: {randompwd}',
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    connection=connection,
                )  
        SendEmail.send()
        connection.close()        
        return JsonResponse({'message': 'Check your Email!'})
        
          

##################################################
############# C.R.U.D ############################
##################################################
#######
#USERS#
#######
@api_view(['POST'])
def addusers(r):
    try:
        User.objects.get(email=r.data['email'])
        return JsonResponse({'message':'User Is Already In The System!'},safe=False)
    except:
        pass    
    newUser = User.objects.create(username=r.data['username'],password=make_password(r.data['password']),email=r.data['email'],is_staff = r.data['is_staff'],first_name=r.data['first_name'],last_name=r.data['last_name'])
    try:
        staffRequest = r.data['staff_requested']
        if staffRequest:
            PermissionRequests.objects.create(_user_id =newUser.id,_first_name=newUser.first_name,_last_name =newUser.last_name ,_email =newUser.email ,_permission_requested = True,_permission_denied = 0) 
            connection = mail.get_connection()
            SendEmail =mail.EmailMessage(
                    'PERMISSION REQUEST',
                    f'User  {newUser.first_name} {newUser.last_name}  has requested AirlineUser permissions. \n To grant/deny it, please login in https://tmw-my-server.azurewebsites.net/login \n User email for further inquiries: {newUser.email}',
                    settings.DEFAULT_FROM_EMAIL,
                    ['kolimoli9@gmail.com'],
                    connection=connection,
                )  
            SendEmail.send()
            connection.close()
    except:pass        
    return JsonResponse({'message':'Welcome!\n U Can Login Now!'},safe=False)

@api_view(['GET','DELETE','PUT'])
@permission_classes([IsAuthenticated,IsAdminUser])
def users(request,id=-1):
    if request.method == 'GET': 
        if int(id) > -1: 
            user= User.objects.get(id = id)
            return JsonResponse(list(user), safe=False)
        else: 
            sUsers = []
            users = User.objects.all()
            for u in users:
                user = {
                    "id":u.id,
                    "username":u.username,
                    "first_name":u.first_name,
                    "last_name":u.last_name,
                    "email":u.email,
                    "is_staff":u.is_staff,
                    "is_superuser":u.is_superuser}
                try:airline=Airlines.objects.get(user=u.id);user['airline'] = airline.airline_name
                except:pass
                sUsers.append(user)          
            return JsonResponse(sUsers,safe=False) 
    
    if request.method == 'DELETE': 
        temp= User.objects.get(id = id)
        temp.delete()
        return JsonResponse({'message':'User Deleted Successfuly !'})
    
    if request.method == 'PUT': 
        temp=User.objects.get(id = id)
        try:
            UserName = request.data['username']
            if UserName != '':
              temp.username = UserName
        except:pass
        try:
            EmailUser = request.data['email']
            if EmailUser!='':
                temp.email =EmailUser
        except:pass
        try:temp.is_staff =request.data['is_staff']
        except:pass
        try:temp.is_superuser =request.data['is_superuser']
        except:pass
        temp.save()
        try:
            airlineName = request.data['airline_name']
            airline = Airlines.objects.get(airline_name = airlineName)
            oau = User.objects.get(id=airline.user.id);oau.is_staff = False;oau.save()
            airline.user = temp
            airline.save() 
            
        except:pass    
        return JsonResponse({'message': f'{temp.username} - Changes Saved !'})

###########
#CUSTOMERS#
###########
@api_view(['POST','DELETE'])
def customers(request,id=-1):
    if request.method == 'POST': 
        first_name =request.data['first_name']
        last_name =request.data['last_name']
        adress =request.data['adress']
        phone = request.data['phone']
        try:credit_num =request.data['credit_num']
        except:credit_num=0000
        try:user = User.objects.get(id=request.data['user_id'])
        except:return  JsonResponse({'message':"Not Registerd."})
        try:chekCustomer=Customers.objects.get(user= id);return JsonResponse({'message':"Already A Customer"})
        except:Customers.objects.create(first_name=first_name,last_name=last_name,adress=adress,phone = phone,credit_num=credit_num,user=user)
        return JsonResponse({'message':"CREATED"})
    
    if request.method == 'DELETE': 
        temp= Customers.objects.get(id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})


@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def getCustomers(request,id=-1):
    if request.method == 'GET':    
        if int(id) > -1:
            customer=GETS.customer_by_user(id) 
            return JsonResponse(customer,safe=False)
        else: 
            customers = Customers.objects.all()
            serializer = CustomersSerializer(customers, many=True)
            return JsonResponse(serializer.data,safe=False) #return array as json response

    if request.method == 'PUT': 
        temp=Customers.objects.get(id = id)
        try:temp.first_name =request.data['first_name'];temp.save()
        except:pass
        try:temp.last_name =request.data['last_name'];temp.save()
        except:pass
        try:temp.adress =request.data['adress'];temp.save()
        except:pass
        try:temp.phone= request.data['phone'];temp.save()
        except:pass
        try:temp.credit_num =request.data['credit_num'];temp.save()
        except:pass
        return JsonResponse({'PUT': id,'name':(temp.first_name,temp.last_name)})


#########
#FLIGHTS#
#########
@api_view(['POST','DELETE','PUT'])
@permission_classes([IsAuthenticated])
def flights(request,id=-1):
        if request.method == 'POST': 
            airlineID =Airlines.objects.get(airline_name=request.data['airline']) 
            origin_country =Countries.objects.get(country_name=request.data['origin_country'])
            destenation_country =Countries.objects.get(country_name=request.data['destenation_country'])
            dep_time =request.data['dep_time']
            arrival_time =request.data['arrival_time']
            tickets = request.data['tickets']
            try:
                Flights.objects.create(airlineID_id=airlineID.id,origin_country=origin_country,destenation_country=destenation_country,dep_time=dep_time,arrival_time=arrival_time,tickets_left=tickets)
                return JsonResponse({'message':"Flight Has Been Added !"})
            except:
              return JsonResponse({'message':"Faild To Add Flight" },safe=False)           
        
        if request.method == 'DELETE': 
            temp= Flights.objects.get(id = id)
            temp.delete()
            return JsonResponse({'DELETE': id})
        
        if request.method == 'PUT': 
            try:temp=Flights.objects.get(id = id) 
            except:return JsonResponse({'message':'Error'})
            try:temp.origin_country =request.data['origin_country']
            except:pass 
            try:temp.destenation_country =request.data['destenation_country']
            except:pass
            try:
                departure = request.data['dep_time']
                if departure =='':
                  pass
                else:
                    temp.dep_time =departure
            except:pass
            try:
                arrival = request.data['arrival_time']
                if arrival =='':
                  pass
                else:
                    temp.arrival_time =arrival
            except:pass
            try:temp.tickets_left = request.data['tickets']
            except:pass
            temp.save()    
            return JsonResponse({'message':'Changes Saved!'})


@api_view(['GET'])
def getflights(request,id=-1):
    if request.method == 'GET':    
        if int(id) > -1: 
            if int(id)> Flights.objects.count(): return JsonResponse({"out of bounds array":str(id)})
            flights= Flights.objects.filter(id = id).values()
            return JsonResponse(list(flights), safe=False)
        else:
            flights=[]
            FLIGHTS = Flights.objects.all()
            for obj in FLIGHTS:
                _id = obj.id
                airline = Airlines.objects.get(airline_name=obj.airlineID)
                countryFrom = Countries.objects.get(country_name=obj.origin_country)
                countryToo = Countries.objects.get(country_name=obj.destenation_country)
                dep =str(obj.dep_time)
                dep_time = dep[10: ]
                dep_date = dep[0:10]
                arrival = str(obj.arrival_time)
                arrival_time = arrival[10: ]
                arrival_date = arrival[0:10]
                tck = obj.tickets_left
                flight = {
                    "id" : _id,
                    "airline" : airline.airline_name,
                    "from" : countryFrom.country_name,
                    "too" : countryToo.country_name,
                    "dep_date" : dep_date,
                    "dep_time" : dep_time,
                    "arrival_date" : arrival_date,
                    "arrival_time" : arrival_time,
                    "tickets" : tck}
                flights.append(flight)    
            
            return JsonResponse(flights,safe=False)

#########
#TICKETS#
#########
@api_view(['GET','POST','DELETE','PUT'])
@permission_classes([IsAuthenticated])
def tickets(request,id=-1):
    if request.method == 'GET':    
        if int(id) > -1: 
            if int(id)> Tickets.objects.count(): return JsonResponse({"out of bounds array":str(id)})
            tickets= Tickets.objects.filter(id = id).values()
            return JsonResponse(list(tickets), safe=False)
        
        else: 
            tickets = Tickets.objects.all()
            serializer = TicketsSerializer(tickets, many=True)
            return JsonResponse(serializer.data,safe=False)
    if request.method == 'DELETE': 
        temp= Tickets.objects.get(id = id)
        temp.delete()
        return JsonResponse({'DELETE':f'ticketID: {id}'})
    
    if request.method == 'POST': 
        try:customer = Customers.objects.get(id=request.data['customer_id'])
        except:return JsonResponse({'message':'Customer Info is not in the system \n OR \nSomthing else went wrong, try again later.'})  
        flight = Flights.objects.get(id=request.data['flight_id'])
        if flight.tickets_left == 0:return JsonResponse({'message':'This flights is SOLD OUT on tickets!'})
        flight.tickets_left-=1
        flight.save()
        Tickets.objects.create(flight=flight, customer=customer)
        return JsonResponse({'message':'CREATED'},safe=False)    

    if request.method == 'PUT': 
        temp=Tickets.objects.get(id = id)
        try:  
            temp.flight =request.data['flight_id']
            flight =Flights.objects.get(id=request.data['flight_id'])
            flight.tickets_left+=1
            flight.save()
            Nflight = Flights.objects.get(id=temp.flight)
            Nflight.tickets_left-=1
            Nflight.save()
        except:
            pass
        try:  
            temp.customer =request.data['customer_id']
        except:
            pass
        temp.save()    
        return JsonResponse({'PUT': id, 'Ticket New Data':f'{temp.id},{temp.flight},{temp.customer}'})
@api_view(['GET','DELETE'])
@permission_classes([IsAuthenticated])
def customerTickets(r, id=-1):
    if r.method == 'GET':    
        if int(id) > -1:
            myTickets = []
            customer = Customers.objects.get(id=id) 
            tickets= Tickets.objects.filter(customer = id)
            for ticket in tickets:
                flight = Flights.objects.get(id=ticket.flight)
                customerCredit = str(customer.credit_num)
                credit = customerCredit[6: ]
                pt = {
                    'name':f'{customer.first_name}-{customer.last_name}',
                    'flight':f'Flight number {flight.id} to :{flight.origin_country} from :{flight.destenation_country}',
                    'departure':f'Departure at {flight.dep_time}',
                    'arrival':f'Arrival at {flight.arrival_time}',
                    'credit':f'**** **** *** {credit}'
                }
                myTickets.append(pt)        
            return JsonResponse(tickets, safe=False)
        else:
            return JsonResponse({'message':'No ID Was Provided'})
    if r.method == 'DELETE':
        temp = Tickets.objects.get(customer=id)
        temp.delete()
        return JsonResponse({'message':'DELETED'}) 

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def prettyticket(req,id):
    newTickets = []
    customer = Customers.objects.get(id=id)
    tickets = Tickets.objects.filter(customer=customer.id).values()
    for ticket in tickets:
        flight = Flights.objects.get(id=ticket['flight_id'])
        newTicket = {
            'id':ticket['id'],
            'name':customer.first_name,
            'departure':str(flight.origin_country),
            'landing' :str(flight.destenation_country),
            'time': f'dep :{flight.dep_time} > arv :{flight.arrival_time}'
        }
        newTickets.append(newTicket)

    return JsonResponse({"tickets":newTickets},safe=False)               