from django.db import models
from django.conf import settings
# Create your models here.

def login_thumbmail_path(instance, filename):
    return f'doctor/{instance.id}/thumbnail/{filename}'

def edit_thumbmail_path(instance, filename):
    return f'profile/{instance.id}/thumbnail/{filename}'

class Login(models.Model):
    name = models.CharField(max_length=100)
    spec = models.CharField(max_length=20) 
    address = models.CharField(max_length=50)
    experience = models.CharField(max_length=3000)
    phone_no = models.CharField(max_length=13) 
    email = models.EmailField(max_length=50) 
    desc = models.CharField(max_length=2500)
    thumbnail = models.FileField(upload_to=login_thumbmail_path, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def get_thumbnail_url(self):
        if self.thumbnail and hasattr(self.thumbnail, 'url'):
            return self.thumbnail.url
        else:
            return settings.STATIC_URL + 'accounts/icon/google.png'

class Profile(models.Model):
    name = models.CharField(max_length=100)
    hos_name = models.CharField(max_length=100)
    spec = models.CharField(max_length=20) 
    address = models.CharField(max_length=50)
    experience = models.CharField(max_length=3000)
    phone_no = models.CharField(max_length=13) 
    email = models.EmailField(max_length=50) 
    fee = models.CharField(max_length=50)
    time = models.CharField(max_length=250)
    thumbnail = models.FileField(upload_to=edit_thumbmail_path, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def get_thumbnail_url(self):
        if self.thumbnail and hasattr(self.thumbnail, 'url'):
            return self.thumbnail.url
        else:
            return settings.STATIC_URL + 'accounts/icon/google.png'
# Create your models here.
