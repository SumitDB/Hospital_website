from django.db import models

# Create your models here.
class User(models.Model):
    Name=models.CharField(max_length=70)
    Email=models.EmailField()
    Mobile_no=models.IntegerField()
    Password=models.CharField(max_length=10)

class Customer(models.Model):
    Treatment_Choices = (
        ('Injection','Injection'),('Medicines/Capsules','Medicines/Capsules'),('Syrup' , 'Syrup'),('Tube','Tube')
        )
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
    genral_exams = models.CharField(max_length=100)  
    treatment_type_1 = models.CharField(max_length=100, choices=Treatment_Choices,null=True)
    treatment_name_1 = models.CharField(max_length=100,null=True)
    units_1 = models.IntegerField(null=True)
    details_1 = models.CharField(max_length=90)
    treatment_type_2 = models.CharField(max_length=100, choices=Treatment_Choices,null=True)
    treatment_name_2 = models.CharField(max_length=100,null=True)
    units_2 = models.IntegerField(null=True)
    details_2 = models.CharField(max_length=90,null=True)
    treatment_type_3 = models.CharField(max_length=100, choices=Treatment_Choices,null=True)
    treatment_name_3 = models.CharField(max_length=100,null=True)
    units_3 = models.IntegerField(null=True)
    details_3 = models.CharField(max_length=90,null=True)
    treatment_type_4 = models.CharField(max_length=100, choices=Treatment_Choices,null=True)
    treatment_name_4 = models.CharField(max_length=100,null=True)
    units_4 = models.IntegerField(null=True)
    details_4 = models.CharField(max_length=90,null=True)
    treatment_type_5 = models.CharField(max_length=100, choices=Treatment_Choices,null=True)
    treatment_name_5 = models.CharField(max_length=100,null=True)
    units_5 = models.IntegerField(null=True)
    details_5 = models.CharField(max_length=90,null=True)
    treatment_type_6 = models.CharField(max_length=100, choices=Treatment_Choices,null=True)
    treatment_name_6 = models.CharField(max_length=100,null=True)
    units_6 = models.IntegerField(null=True)
    details_6 = models.CharField(max_length=90,null=True)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name