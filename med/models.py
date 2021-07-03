from django.db import models

# Create your model


class Buy(models.Model):
    name = models.CharField(max_length=100,verbose_name='Name')
    email = models.EmailField(max_length=100,verbose_name='Email')
    address = models.CharField(max_length=100,verbose_name='Address')
    country = models.CharField(max_length=100,verbose_name="Country Name")
    city = models.CharField(max_length=100,verbose_name="City Name")
    medicine = models.CharField(max_length=100,verbose_name="Medicine Name")
    medicinedate = models.CharField(max_length=100,verbose_name="Medicine Expiration Date")
    medicineqty = models.CharField(max_length=100,verbose_name="Medicine Quantity")
    medicinetype = models.CharField(max_length=100,verbose_name="Medicine Quantity Type")
    phone = models.CharField(max_length=100,verbose_name='Phone Number')
    zipcode = models.CharField(max_length=100,verbose_name='Zip Code')
    cardname = models.CharField(max_length=100,verbose_name='Card Holder Name')
    cardnumber = models.CharField(max_length=100,verbose_name='Credit Card Number')
    month = models.CharField(max_length=100,verbose_name='Exp Month')
    year = models.CharField(max_length=100,verbose_name='Exp Year')
    civ = models.CharField(max_length=100,verbose_name='CVV')

    def __str__(self):
        return self.name


class NGO(models.Model):
    name = models.CharField(max_length=100,verbose_name='Name')
    email = models.EmailField(max_length=100,verbose_name='Email')
    ngoname = models.CharField(max_length=100,verbose_name='NGO Name')
    ngonumber = models.CharField(max_length=100,verbose_name='NGO Number')
    address = models.CharField(max_length=100,verbose_name='Address')
    country = models.CharField(max_length=100,verbose_name="Country Name")
    city = models.CharField(max_length=100,verbose_name="City Name")
    medicine = models.CharField(max_length=100,verbose_name="Medicine Name")
    medicinedate = models.CharField(max_length=100,verbose_name="Medicine Expiration Date")
    medicineqty = models.CharField(max_length=100,verbose_name="Medicine Quantity")
    medicinetype = models.CharField(max_length=100,verbose_name="Medicine Quantity Type")
    phone = models.CharField(max_length=100,verbose_name='Phone Number')
    zipcode = models.CharField(max_length=100,verbose_name='Zip Code')
    cardname = models.CharField(max_length=100,verbose_name='Card Holder Name')
    cardnumber = models.CharField(max_length=100,verbose_name='Credit Card Number')
    month = models.CharField(max_length=100,verbose_name='Exp Month')
    year = models.CharField(max_length=100,verbose_name='Exp Year')
    civ = models.CharField(max_length=100,verbose_name='CVV')
    def __str__(self):
        return self.name


class CardDetail(models.Model):
    cardname = models.CharField(max_length=100,verbose_name='Card Holder Name')
    cardnumber = models.CharField(max_length=100,verbose_name='Credit Card Number')
    month = models.CharField(max_length=100,verbose_name='Exp Month')
    year = models.CharField(max_length=100,verbose_name='Exp Year')
    civ = models.CharField(max_length=100,verbose_name='CVV')

    def __str__(self):
        return self.cardname


class Contact(models.Model):
    name = models.CharField(max_length=100,verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Message')

    def __str__(self):
        return self.name