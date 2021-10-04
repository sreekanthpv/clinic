
from django import forms
from clinicadmin.models import MyUser
from django.contrib.auth.forms import UserCreationForm

class PatientRegistrationForm(UserCreationForm):

    class Meta:
        model=MyUser
        fields=["email","date_of_birth","phone"]
        widgets={
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "date_of_birth":forms.DateInput(attrs={"type":"date"}),
           "phone":forms.NumberInput(attrs={"class":"form-control"}),
        }



class SignInForm(forms.Form):
    email=forms.CharField(widget=(forms.EmailInput(attrs={"class":"form-control"})))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))