from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    tel_name = models.CharField(max_length=45)
    email_name = models.CharField(max_length=45)
    address_name = models.CharField(max_length=45)
    
    def __str__(self):
        return self.first_name

    