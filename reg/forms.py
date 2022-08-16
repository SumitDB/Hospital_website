from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Customer


class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password(again)',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', ]
        labels = {'email': 'Email'}
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control '}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }
class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password2', ]
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }
class CustomerReg(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','age','gender','email', 'mobile','address','city','complaints','pulse','blood_pressure','temprature',
        'blood_suger_level','genral_exams']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.NumberInput(attrs={'class':'form-control'}),
            'gender': forms.Select(attrs={'class':'form-control'}), 
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'mobile': forms.NumberInput(attrs={'class':'form-control'}),
            'address': forms.Textarea(attrs={'class':'form-control',"rows":1, "cols":5}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'complaints': forms.Textarea(attrs={'class':'form-control',"rows":3, "cols":5}),
            'pulse': forms.TextInput(attrs={'class':'form-control'}),
            'blood_pressure': forms.TextInput(attrs={'class':'form-control'}),
            'temprature': forms.TextInput(attrs={'class':'form-control'}),
            'blood_suger_level': forms.TextInput(attrs={'class':'form-control'}),
            'genral_exams': forms.Textarea(attrs={'class':'form-control',"rows":3, "cols":5}),
            }

