from django.urls import path , include
from . import views

urlpatterns = [

  path("drugHomePage/", views.drugHome, name='drugHome'),
  path('patient_details/', views.patientDetail, name="details"),

]