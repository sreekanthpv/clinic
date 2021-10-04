from django.shortcuts import render
from clinicadmin.models import Doctor,MyUser,Appointment
from django.views.generic import TemplateView
from django.views.generic import CreateView
from clinicadmin.forms import AddDoctorForm
from django.urls import reverse_lazy


class AddDoctorView(CreateView):
    model = Doctor
    form_class = AddDoctorForm
    template_name = "clinicadmin/addoctor.html"
    success_url = reverse_lazy("addoctor")
    # context={}
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["doctors"]=self.model.objects.all()
        return context

    





