from django.db import models


class Company(models.Model):
    content = models.TextField()


    class Meta:
        db_table = 'company'


class Contacts(models.Model):
    address = models.TextField()
    email = models.CharField(max_length=50)
    telephones = models.CharField(max_length=200)


    class Meta:
        db_table = 'contacts'


class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    status = models.BooleanField(default=False)
    img_url = models.CharField(max_length=255)


    class Meta:
        db_table = 'products'


class Sertify(models.Model):
    content = models.TextField()
    img_url = models.CharField(max_length=255)


    class Meta:
        db_table = 'sertify'

