from django import forms
from clinicadmin.models import Doctor,MyUser,Appointment



class AddDoctorForm(forms.ModelForm):
        class Meta:
            model = Doctor
            fields = ['name','age','address','specialization']
            widgets={
                'name':forms.TextInput(attrs={"class":"form-control"}),
                'age': forms.NumberInput(attrs={"class": "form-control"}),
                'address': forms.Textarea(attrs={"class": "form-control"}),
                'specialization': forms.TextInput(attrs={"class": "form-control"}),
            }

