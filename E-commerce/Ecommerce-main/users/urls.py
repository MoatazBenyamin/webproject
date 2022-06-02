from users import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users.views import signup , myaccount,profile_update,video
from django.contrib.auth import views


urlpatterns = [
    path( 'signup/' , signup , name='signup'),
    path('myaccount/', myaccount, name='myaccount'),
    path('review-watches/', video, name='review'),
    path('profile/update/', profile_update,
         name='user-profile-update'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)