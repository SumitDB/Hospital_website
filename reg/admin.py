from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','age','gender','email', 'mobile','address','city','complaints','pulse','blood_pressure',"temprature",
        'blood_suger_level','genral_exams','treatment_type_1','treatment_name_1','units_1','details_2','treatment_type_2','treatment_name_2','units_2','details_2',
        'treatment_type_3','treatment_name_3','units_3','details_3','treatment_type_4','treatment_name_4','units_4','details_4','treatment_type_5','treatment_name_5','units_5','details_5',
        'treatment_type_6','treatment_name_6','units_6','details_6','total_fees')
