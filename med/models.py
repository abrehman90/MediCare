from django.db import models

# Create your model


class Addres(models.Model):
    name = models.CharField(max_length=100,verbose_name='Name')
    email = models.EmailField(max_length=100,verbose_name='Email')
    address = models.CharField(max_length=100,verbose_name='Address')
    country = models.CharField(max_length=100,verbose_name="Country Name")
    medicine = models.CharField(max_length=100,verbose_name="Medicine Name")
    phone = models.IntegerField(verbose_name='Phone Number')
    zipcode = models.IntegerField(verbose_name='Zip Code')

    def __str__(self):
        return self.name


class CardDetail(models.Model):
    cardname = models.CharField(max_length=100,verbose_name='Card Holder Name')
    cardnumber = models.IntegerField(verbose_name='Credit Card Number')
    month = models.IntegerField(verbose_name='Exp Month')
    year = models.IntegerField(verbose_name='Exp Year')
    civ = models.IntegerField(verbose_name='CVV')

    def __str__(self):
        return self.cardname


class Contact(models.Model):
    name = models.CharField(max_length=100,verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Message')

    def __str__(self):
        return self.name