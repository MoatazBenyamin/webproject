from users import views
from django.urls import path, include
from users.views import signup , myaccount

urlpatterns = [
    path( 'signup/' , signup , name='signup'),
    path('myaccount/', myaccount, name='myaccount'),
]