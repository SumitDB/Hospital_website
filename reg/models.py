from django.db import models

# Create your models here.
class User(models.Model):
    Name=models.CharField(max_length=70)
    Email=models.EmailField()
    Mobile_no=models.IntegerField()
    Password=models.CharField(max_length=10)

class Treatment(models.Model):
    Treatment_Choices = (
        ('Injection','Injection'),('Medicines/Capsules','Medicines/Capsules'),('Syrup' , 'Syrup'),('Injection','Injection'),('Tube','Tube')
        )
    
    treatment_type = models.CharField(max_length=100, choices=Treatment_Choices)
    treatment_name = models.CharField(max_length=100)
    units = models.IntegerField(null=True)
    details = models.CharField(max_length=90)
    class Meta:
        ordering = ['treatment_type']

    def __str__(self):
        return self.treatment_type


class Customer(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T', 'Transgender')
    )
    name = models.CharField(max_length=25,null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,null=True)
    email = models.EmailField(max_length=25,null=True)
    mobile = models.IntegerField(null=True)
    address = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=10,null=True)
    complaints = models.CharField(max_length=100,null=True)
    pulse = models.CharField(max_length=10,null=True)
    blood_pressure = models.CharField(max_length=10,null=True)
    temprature = models.CharField(max_length=10,null=True)
    blood_suger_level = models.CharField(max_length=10,null=True)
    genral_exams = models.CharField(max_length=100,null=True)  
    treatment = models.ForeignKey(Treatment, blank = True , null = True, on_delete = models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name