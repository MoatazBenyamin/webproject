from users import views
from django.urls import path, include
from users.views import signup , myaccount,profile_update
from django.contrib.auth import views


urlpatterns = [
    path( 'signup/' , signup , name='signup'),
    path('myaccount/', myaccount, name='myaccount'),
    path('profile/update/', profile_update,
         name='user-profile-update'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
]