from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import SignUpForm , CustomerReg
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from reg.models import Customer


# Create your views here.
def Sign_up(request):
    if request.method == 'POST':
        fm= SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully !!!')
            fm.save()
    else:
        fm = SignUpForm()
    return render (request, 'reg/signup.html',{'form':fm})

#Login View
def User_login(request):
    if  not request.user.is_authenticated:
        if request.method == "POST":
            fm=AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request,'You have Logged in successfully !!')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request,'reg/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')
        
def User_profile(request):
    if request.user.is_authenticated:
        print('yes')
        if request.method == "POST":
            print('Yes')
            fmm = CustomerReg(request.POST)
            if fmm.is_valid():
                print('Yyes')
                nm = fmm.cleaned_data['name']
                ag = fmm.cleaned_data['age']
                ge = fmm.cleaned_data['gender']
                em = fmm.cleaned_data['email']
                mb = fmm.cleaned_data['mobile']
                ad = fmm.cleaned_data['address']
                com = fmm.cleaned_data['complaints']
                pl = fmm.cleaned_data['pulse']
                bp = fmm.cleaned_data['blood_pressure']
                bsl = fmm.cleaned_data['blood_suger_level']
                temp = fmm.cleaned_data['temprature']
                gex = fmm.cleaned_data['genral_exams']
                ct = fmm.cleaned_data['city']
                tt1 = fmm.cleaned_data['treatment_type_1']
                tn1 = fmm.cleaned_data['treatment_name_1']
                u1 = fmm.cleaned_data['units_1']
                d1 = fmm.cleaned_data['details_1']
                tt2 = fmm.cleaned_data['treatment_type_2']
                tn2 = fmm.cleaned_data['treatment_name_2']
                u2 = fmm.cleaned_data['units_2']
                d2 = fmm.cleaned_data['details_2']
                tt3 = fmm.cleaned_data['treatment_type_3']
                tn3 = fmm.cleaned_data['treatment_name_3']
                u3 = fmm.cleaned_data['units_3']
                d3 = fmm.cleaned_data['details_3']
                tt4 = fmm.cleaned_data['treatment_type_4']
                tn4 = fmm.cleaned_data['treatment_name_4']
                u4 = fmm.cleaned_data['units_4']
                d4 = fmm.cleaned_data['details_4']
                tt5 = fmm.cleaned_data['treatment_type_5']
                tn5 = fmm.cleaned_data['treatment_name_5']
                u5 = fmm.cleaned_data['units_5']
                d5 = fmm.cleaned_data['details_5']
                tt6 = fmm.cleaned_data['treatment_type_6']
                tn6 = fmm.cleaned_data['treatment_name_6']
                u6 = fmm.cleaned_data['units_6']
                d6 = fmm.cleaned_data['details_6']
                reg = Customer( name=nm, age=ag, gender=ge, email=em, mobile=mb, address=ad, complaints=com, pulse=pl, blood_pressure=bp,blood_suger_level=bsl,genral_exams=gex,city=ct,temprature=temp,treatment_type_1=tt1,treatment_name_1=tn1,units_1=u1,details_1=d1,treatment_type_2=tt2,treatment_name_2=tn2,units_2=u2,details_2=d2,treatment_type_3=tt3,treatment_name_3=tn3,units_3=u3,details_3=d3,treatment_type_4=tt4,treatment_name_4=tn4,units_4=u4,details_4=d4,treatment_type_5=tt5,treatment_name_5=tn5,units_5=u5,details_5=d5,treatment_type_6=tt6,treatment_name_6=tn6,units_6=u6,details_6=d6)
                reg.save()
                messages.success(request,'You have successfully added the customer !!')
                fmm = CustomerReg()
        else:
            fmm = CustomerReg()
        return render(request, 'reg/profile.html',{'name':request.user, 'formm':fmm})
    else:
        return HttpResponseRedirect('/login/')

def Customers(request):
    if request.user.is_authenticated:
        cust = Customer.objects.all()
        return render(request, 'reg/customer.html',{'name':request.user, 'stu':cust})
    else:
        return HttpResponseRedirect('/login/')

def User_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

# This function will delete
def Delete_data(request, id):
    if request.method == 'POST':
        pi = Customer.objects.get(pk=id)
        pi.delete()
        messages.success(request,'You have successfully deleted the customer !!')
        return HttpResponseRedirect('/customer/')

# This function will update
def Update_data(request, id):
    # context ={}
    # # fetch the object related to passed id
    # obj = get_object_or_404(Customer, id = id)
    # # pass the object as instance in form
    # formm = CustomerReg(request.POST or None, instance = obj)
    # # save the data from the form and
    # # redirect to detail_view
    # if formm.is_valid():
    #     formm.save()
    #     return HttpResponseRedirect("reg/updatecustomer.html/",{'id':id})
    # # add form dictionary to context
    # context["formm"] = formm
    # return render(request, "reg/updatecustomer.html", context)
    if request.method == 'POST':
        pi = Customer.objects.get(pk = id)
        fmm = CustomerReg(request.POST, instance=pi)
        if fmm.is_valid():
            fmm.save()
            messages.success(request,'You have successfully edited the customer !!')
            return render(request, 'reg/updatecustomer.html',{'formm':fmm, 'id':id})
        
def View_data(request,id):
    if request.user.is_authenticated:
        pi = Customer.objects.get(pk=id)
        fmm = CustomerReg(instance=pi)      
        return render(request, 'reg/updatecustomer.html',{'formm':fmm, 'id':id})
    else:
        return HttpResponseRedirect('/login/')


def Customers_all(request, id):
    if request.user.is_authenticated:
        pi = Customer.objects.get(pk=id)
        fmm = CustomerReg(instance=pi) 
        return render(request, 'reg/customer_all.html',{ 'formm':fmm})


        
    else:
        return HttpResponseRedirect('/login/')
