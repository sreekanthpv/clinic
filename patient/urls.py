from django.urls import path
from patient import views

urlpatterns = [
    path('accounts/signup', views.patientregistration, name="patientregistration"),
    path('accounts/signin',views.siginin,name="signin"),
    path('home',views.home,name="home"),


]
