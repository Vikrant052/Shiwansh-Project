from django.db import models
from django.contrib.auth.hashers import make_password

class Registration(models.Model):
  Admin = 'Admin'
  Staff = 'Staff'
  Student = 'Student'
  Role_choice = (
        (Admin, 'Admin'),
        (Staff,'Staff'),
        (Student, 'Student')
    )
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length=100,unique= True)
  birth_date = models.DateField()
  role  = models.CharField(max_length=100,choices=Role_choice)
  password = models.CharField(max_length=200)
  confirm_password = models.CharField(max_length=200)
  
  
  def save(self, *args, **kwargs):
    if self.pk is None:  
        self.password = make_password(self.password)
    super().save(*args, **kwargs)

def __str__(self):
    return self.name
  
def __str__(self):
    return self.role


class Standard(models.Model):
    id = models.AutoField(primary_key=True)
    StandardName = models.CharField(max_length=50)
    
class Division(models.Model):
    id =models.AutoField(primary_key=True)
    DivisionName = models.CharField(max_length=10)
    seat = models.IntegerField()
    standard = models.ForeignKey(Standard,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.DivisionName
    
    
class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    mobile = models.CharField(max_length=30)
    Qualification = models.CharField(max_length=15)
    forkey = models.ForeignKey(Registration,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.mobile