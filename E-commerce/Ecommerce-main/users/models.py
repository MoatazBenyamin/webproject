from django.contrib.auth.models import User
from django.db import models

class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(default='default.png',
                              upload_to='profile_images')

    def __str__(self):
        return '%s' % self.user.username

User.userprofile = property(lambda u:Userprofile.objects.get_or_create(user=u)[0])


