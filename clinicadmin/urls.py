from django.urls import path
from clinicadmin import views

urlpatterns=[

    path('doctors/add',views.AddDoctorView.as_view(),name='addoctor'),
]