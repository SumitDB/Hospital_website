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
    name = models.CharField(max_length=25,blank=True,null=True)
    age = models.IntegerField(blank=True,null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,blank=True,null=True)
    email = models.EmailField(max_length=25,blank=True,null=True)
    mobile = models.IntegerField(blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    city = models.CharField(max_length=10,blank=True,null=True)
    complaints = models.CharField(max_length=100,blank=True,null=True)
    pulse = models.CharField(max_length=10,blank=True,null=True)
    blood_pressure = models.CharField(max_length=10,blank=True,null=True)
    temprature = models.CharField(max_length=10,blank=True,null=True)
    blood_suger_level = models.CharField(max_length=10,blank=True,null=True)
    genral_exams = models.CharField(max_length=100,null=True,blank=True)  
    treatment_type_1 = models.CharField(max_length=100, choices=Treatment_Choices,blank=True,null=True)
    treatment_name_1 = models.CharField(max_length=100,blank=True,null=True)
    units_1 = models.IntegerField(blank=True,null=True)
    details_1 = models.CharField(max_length=90,blank=True,null=True)
    treatment_type_2 = models.CharField(max_length=100, choices=Treatment_Choices,blank=True,null=True)
    treatment_name_2 = models.CharField(max_length=100,blank=True)
    units_2 = models.IntegerField(blank=True,null=True)
    details_2 = models.CharField(max_length=90,blank=True)
    treatment_type_3 = models.CharField(max_length=100, choices=Treatment_Choices,blank=True,null=True)
    treatment_name_3 = models.CharField(max_length=100,blank=True,null=True)
    units_3 = models.IntegerField(blank=True,null=True)
    details_3 = models.CharField(max_length=90,blank=True,null=True)
    treatment_type_4 = models.CharField(max_length=100, choices=Treatment_Choices,blank=True,null=True)
    treatment_name_4 = models.CharField(max_length=100,blank=True,null=True)
    units_4 = models.IntegerField(blank=True,null=True)
    details_4 = models.CharField(max_length=90,blank=True)
    treatment_type_5 = models.CharField(max_length=100, choices=Treatment_Choices,blank=True,null=True)
    treatment_name_5 = models.CharField(max_length=100,blank=True,null=True)
    units_5 = models.IntegerField(blank=True,null=True)
    details_5 = models.CharField(max_length=90,blank=True,null=True)
    treatment_type_6 = models.CharField(max_length=100, choices=Treatment_Choices,blank=True,null=True)
    treatment_name_6 = models.CharField(max_length=100,blank=True,null=True)
    units_6 = models.IntegerField(blank=True,null=True)
    details_6 = models.CharField(max_length=90,blank=True,null=True)
        
    class Meta:    
        ordering = ['name']

    def __str__(self):
        return self.name