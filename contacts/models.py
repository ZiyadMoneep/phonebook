from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class PhoneNumber(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    number = PhoneNumberField()

    def __str__(self):
        return f"{self.contact}"
