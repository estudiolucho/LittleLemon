from django.db import models

# Create your models here.
class Menu(models.Model):
   f_name= models.CharField(max_length= 30)
   f_price= models.DecimalField(max_digits=10,decimal_places=2)
   f_inventory= models.IntegerField()
   def __str__(self):
      #return self.f_name
      return f'{self.title}:{str(self.price)}'
class Booking(models.Model):
   f_name = models.CharField(max_length=255)    
   f_no_of_guest = models.SmallIntegerField()
   f_bookingdate=models.DateTimeField()

   def __str__(self):
      return self.f_name + ' ' + self.f_no_of_guest
