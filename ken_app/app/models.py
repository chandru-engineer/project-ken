from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime


class OrderModel(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50)
    customer_id = models.CharField(max_length=5)
    phone_number = PhoneNumberField()
    delivery_date = models.DateField() ## dd/mm/yyyy
    current_date = models.CharField(max_length=20)
    delivery_time = models.TimeField(auto_now_add=False, blank=False) #'hh:mm'
    order_date_time = models.DateTimeField(default = datetime.now(), blank = True)
    address = models.CharField(max_length=100)
    chicken_kg = models.CharField(max_length=10)
    chicken_category = models.CharField(max_length=20)
    chicken_citting = models.CharField(max_length=20)
    mutton_kg = models.CharField(max_length=20)
    mutton_category = models.CharField(max_length=20)
    mutton_cutting = models.CharField(max_length=20)
    status = models.BooleanField()
    delivered = models.BooleanField()
    amount = models.IntegerField()
    review = models.CharField(max_length=200)


    def __str__(self):
        return self.customer_name

    



