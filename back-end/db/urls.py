from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
     TokenRefreshView,
)
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import MyTokenObtainPairView, contact

urlpatterns = [
    #UTILS
    path('contact/',views.contact),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('forgot_password/',views.forgot_password),
    #TESTS
    
    #C R U D
    path('users/',views.users,name="users"),
    path('register/',views.addusers,name="addusers"),
    path('users/<int:id>',views.users,name="usersID"),
    
    path('customers/',views.customers,name='customers'),
    path('customers/get-update/',views.getCustomers,name='customersaddupdate'),
    path('customers/get-update/<int:id>',views.getCustomers,name='IDaddupdate'),
    path('customers/<int:id>',views.customers,name='customersID'),
    
    path('getflights/',views.getflights,name='getflights'),
    path('flights/',views.flights,name='flights'),
    path('flights/<int:id>',views.flights,name='flightsID'),
    
    path('tickets/',views.tickets,name='tickets'),
    path('tickets/<int:id>',views.tickets,name='ticketsID'),
    path('MyTicket/<int:id>',views.prettyticket)
]

