from datetime import *
from random import choice
from django.conf import settings
from django.http import  JsonResponse
from .models import Countries, Airlines, CustomerService, Test, Customers, Flights, Tickets 
from rest_framework.decorators import api_view,permission_classes
from .Serializers import AirlinesSerializer,CountriesSerializer,CustomersSerializer,FlightsSerializer,TicketsSerializer,UserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.contrib.auth.hashers import make_password, check_password
from django.core import mail
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# CUSTOM TOKEN
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        token['is_staff']=user.is_staff
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
            return JsonResponse({'Error': 'This User Is Not In The System!'})
        randompwd = ''.join([choice('1234567890qwertyuiopasdfghjklzxcvbnm') for i in range(8)])
        user.password = make_password(randompwd)
        user.save()
        connection = mail.get_connection()
        SendEmail =mail.EmailMessage(
                    'FORGOT PASSWORD',
                    f'Hi there {user.name},  \n We heard that you`ve misplaced your password :) \n your new password: {randompwd}',
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    connection=connection,
                )  
        SendEmail.send()
        connection.close()        
        return JsonResponse({'message': 'Chek your Email!'})
        
          

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
        return JsonResponse({'message':'User Is Already In The System!'})
    except:
        pass     
    if r.data['staff_requested'] == 'True':
        # subject = 'Staff Status request'
        # html_message = render_to_string('mail_template.html', {'first_name':r.data['first_name'],'last_name':r.data['first_name'],'email':r.data['email']})
        # plain_message = strip_tags(html_message)
        # from_email = settings.DEFAULT_FROM_EMAIL
        # to = 'kolimoli9@gmail.com' 
        # mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
        pass   
    User.objects.create(username=r.data['username'],password=make_password(r.data['password']),email=r.data['email'],is_staff = r.data['is_staff'],first_name=r.data['first_name'],last_name=r.data['last_name'])
    return JsonResponse({'CREATED':'Welcome!\n U can Login Now !'})

@api_view(['GET','DELETE','PUT'])
@permission_classes([IsAuthenticated])
def users(request,id=-1):
    if request.method == 'GET': 
        if int(id) > -1: 
            users= User.objects.get(id = id)
            user = {
                "username":users.username,
                "email":users.email,
                "is_staff":users.is_staff
            }
            return JsonResponse(user, safe=False)
        else: 
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return JsonResponse(serializer.data,safe=False) 
    
    if request.method == 'DELETE': 
        temp= User.objects.get(id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})
    
    if request.method == 'PUT': 
        temp=User.objects.get(id = id)
        try:
            temp.username =request.data['username']
        except:
            pass
        try:
            temp.password =request.data['password'] 
        except:
            pass
        try:
            temp.email =request.data['email']
        except:
            pass
        try:
            temp._group =request.data['role']
        except:
            pass    
        temp.save()
        return JsonResponse({'PUT': id,'name':temp.username})
###########
#CUSTOMERS#
###########
@api_view(['POST','DELETE'])
@permission_classes([IsAuthenticated])
def customers(request,id=-1):
    if request.method == 'POST': 
        first_name =request.data['first_name']
        last_name =request.data['last_name']
        adress =request.data['adress']
        phone = request.data['phone']
        try:
           credit_num =request.data['credit_num']
        except:
            credit_num=0000
        try:   
           user_id = request.data['user_id']
        except:
            return  JsonResponse({'POST':"NotRegisterd."}) 
        Customers.objects.create(first_name=first_name,last_name=last_name,adress=adress,phone = phone,credit_num=credit_num,user=user_id)
        return JsonResponse({'POST':"CREATED"})
    
    if request.method == 'DELETE': 
        temp= Customers.objects.get(id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})


@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated,IsAdminUser])
def getupdatecustomers(request,id=-1):
    if request.method == 'GET':    
        if int(id) > -1: 
            if int(id)> Customers.objects.count(): return JsonResponse({"out of bounds array":str(id)})
            customers= Customers.objects.filter(id = id).values()
            return JsonResponse(list(customers), safe=False)
        else: 
            customers = Customers.objects.all()
            serializer = CustomersSerializer(customers, many=True)
            return JsonResponse(serializer.data,safe=False) #return array as json response

    if request.method == 'PUT': 
        temp=Customers.objects.get(id = id)
        try:
            temp.first_name =request.data['first_name']
            temp.save()
        except:
            pass
        try:
            temp.last_name =request.data['last_name']
            temp.save()
        except:
            pass
        try:
            temp.adress =request.data['adress']
            temp.save()
        except:
            pass
        try:
            temp.phone= request.data['phone']
            temp.save()
        except:
            pass
        try:
            temp.credit_num =request.data['credit_num']
            temp.save()
        except:
            pass
        return JsonResponse({'PUT': id,'name':(temp.first_name,temp.last_name)})


#########
#FLIGHTS#
#########
@api_view(['POST','DELETE','PUT'])
@permission_classes([IsAuthenticated])
def flights(request,id=-1):
    user = request.data['user']
    if user._group == 'airline':
        if request.method == 'POST': 
            airlineID =Airlines.objects.get(id=request.data['airlineID_id']) 
            origin_country =Countries.objects.get(id=request.data['origin_country_id'])
            destenation_country =Countries.objects.get(id=request.data['destenation_country_id'])
            dep_time =request.data['dep_time']
            arrival_time =request.data['arrival_time']
            tickets_left = request.data['tickets_left']
            Flights.objects.create(airlineID_id=airlineID.id,origin_country_id=origin_country.id,destenation_country_id=destenation_country.id,dep_time=dep_time,arrival_time=arrival_time,tickets_left=tickets_left)
            return JsonResponse({'POST':f"CREATED: {origin_country}>>{destenation_country}||{tickets_left}"})
        
        if request.method == 'DELETE': 
            temp= Flights.objects.get(id = id)
            temp.delete()
            return JsonResponse({'DELETE': id})
        
        if request.method == 'PUT': 
            temp=Flights.objects.get(id = id)
            try:
                temp.origin_country =request.data['origin_country']
            except:
                pass 
            try:  
                temp.destenation_country =request.data['destenation_country']
            except:
                pass
            try:    
                temp.dep_time =request.data['dep_time']
            except:
                pass
            try:    
                temp.arrival_time =request.data['arrival_time']
            except:
                pass
            try:    
                temp.tickets_left = request.data['tickets_left']
            except:
                pass
            temp.save()    
            return JsonResponse({'PUT': id,'name':f'{temp.origin_country}>>{temp.destenation_country}||{temp.tickets_left}'})
    else:
        return JsonResponse({'action_denied':'this user does not have permmission to do this.'})

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
        flight_id = request.data['flight_id']
        customer = Customers.objects.get(id=request.data['customer_id'])
        flightT = Flights.objects.get(id=flight_id)
        flightT.tickets_left-=1
        print('The Flight with changed tickets: ', flightT)
        flightT.save()
        Tickets.objects.create(flight=flight_id, customer=customer.id)
        return JsonResponse({'TicketCreated':f'{customer.id},{flight_id}'})    

    if request.method == 'PUT': 
        temp=Tickets.objects.get(id = id)
        FID = temp.flight_id_id
        try:
            temp.id =request.data['id']
        except:
            pass 
        try:  
            temp.flight_id_id =request.data['flight_id']
            Oflight =Flights.objects.get(id=FID)
            Oflight.tickets_left+=1
            Oflight.save()
            Nflight = Flights.objects.get(id=request.data['flight_id'])
            Nflight.tickets_left-=1
            Nflight.save()
        except:
            pass
        try:  
            temp.customer_id_id =request.data['customer_id']
        except:
            pass
        temp.save()    
        return JsonResponse({'PUT': id, 'New Data':f'{temp.id},{temp.flight_id_id},{temp.customer_id_id}'})






