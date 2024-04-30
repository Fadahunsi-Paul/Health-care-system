from django.urls import path
from .import views

app_name = "care"

urlpatterns = [
    path('', views.home, name="home"), 
    path('doctor/',views.doctor, name='doctor-page'),
    path('add-doctor/',views.add_doctor,name='add-doctor'),
    path('update_doctor/<int:pk>/',views.update_doctor,name='update_doctor'), 
    path('delete_doctor/<int:pk>/',views.delete_doctor,name='delete_doctor'),
    path('patients/',views.patients,name='patients-page'),
    path('add_patients/',views.add_patients,name='add-patients'),
    path('update_patients/<int:pk>/',views.update_patients,name='update-patient'),
    path('delete_patient/<int:pk>/',views.delete_patients,name='delete-patient'),
    path('doctor_profile/<int:pk>/',views.doctor_profile,name='doctor-profile'),
]
