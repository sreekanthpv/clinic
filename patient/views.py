from django.shortcuts import render,redirect
from patient import forms
from django.contrib import messages
from django.contrib.auth import login,authenticate
from django.views.generic import CreateView
from clinicadmin.models import Doctor,Appointment,MyUser



def patientregistration(request):

    form=forms.PatientRegistrationForm()
    context={"form":form}
    if request.method=="POST":
        form=forms.PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success=(request,"registration succesfull")
            return redirect("signin")
    return render(request,"patient/patientregistration.html",context)



def siginin(request):
    form=forms.SignInForm()
    context={"form":form}
    if request.method=="POST":
        form=forms.SignInForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            user=authenticate(request,email=email,password=password)
            if user:
                login(request,user)
                return redirect("home")
            else:
                messages.error(request,"login failed")
                return redirect("signin")
    return render(request,"patient/login.html",context)


# class AddDoctor(CreateView):
#     model = Do


def home(request):
    return render(request,"patient/home.html")


