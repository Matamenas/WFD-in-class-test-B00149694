from django.db import models


class Car(models.Model):
    car_ID = models.IntegerField()
    serial_number = models.CharField(max_length=23)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    year = models.IntegerField()
    isforSale = models.BooleanField(default=True)

class Customer(models.Model):
    customer_ID = models.IntegerField()
    lastName = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postcode = models.CharField(max_length=50)


class ServiceTicket(models.Model):
    service_ticket_ID = models.IntegerField()
    service_ticket_number = models.CharField(max_length=50)
    car_ID = models.ForeignKey(Car, on_delete=models.CASCADE)
    Customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_received = models.DateField()
    comments = models.TextField()
    date_returned_to_customer = models.DateField()

class SalesPerson(models.Model):
    SalesPerson_ID = models.IntegerField()
    lastName = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)

class SalesInvoice(models.Model):
    invoice_ID = models.IntegerField()
    invoice_number = models.CharField(max_length=50)
    date = models.DateField()
    Car_ID = models.ForeignKey(Car, on_delete=models.CASCADE)
    Customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    SalesPerson_ID = models.ForeignKey(SalesPerson, on_delete=models.CASCADE)

class Mechanic(models.Model):
    mechanic_ID = models.IntegerField()
    lastName = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)

class Service(models.Model):
    service_ID = models.IntegerField()
    service_name = models.CharField(max_length=50)
    hourly_rate = models.FloatField()

class ServiceMechanic:
    service_mechanic_ID = models.IntegerField()
    mechanic_ID = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    service_ticket_ID = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    service_ID = models.ForeignKey(Service, on_delete=models.CASCADE)
    hours = models.TimeField()
    comment = models.TextField()
    rate = models.FloatField()

class Parts:
    parts_ID = models.IntegerField()
    part_number = models.CharField(max_length=50)
    description = models.TextField()
    purchase_price = models.FloatField()
    retail_price = models.FloatField()

class PartsUsed:
    parts_used_ID = models.IntegerField()
    parts_ID = models.ForeignKey(Parts, on_delete=models.CASCADE)
    service_ticket_ID = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    numberUsed = models.IntegerField()
    price = models.FloatField()






