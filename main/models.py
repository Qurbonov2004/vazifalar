from django.db import models

class Mashgulot(models.Model):
    mashgulot_nomi = models.CharField(max_length=255)
    davomiyligi = models.CharField(max_length=25)
    boshlanish_vaqti = models.TimeField()
    tugash_vaqti = models.TimeField()
    # mashgulot_icon = models.ImageField()
    kuni = models.CharField(max_length=20)
    class Meta():
        verbose_name_plural="mashgulotlar"


class Teacher(models.Model):
    # image = models.ImageField()
    name = models.CharField(max_length=30)
    haqida = models.TextField()
    class Meta():
        verbose_name_plural="Oqituvchilar"

class Service(models.Model):
    # service_icon = models.ImageField()
    service_name = models.CharField(max_length=55)
    about_service = models.TextField()

    class Meta():
        
        verbose_name_plural="xizmatlar"

class Contact_Us(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(null=True)
    is_activate = models.BooleanField(default=True)
    class Meta():
        verbose_name_plural="biz bilan boglaning"
        

    
