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

    path('appointment/',views.appointment,name='appointment-page'),
    path('add_appointment/',views.add_appointment,name='add-appointment'),
    path('update_appointment/<int:pk>/',views.update_appointment,name='update-appointment'),
    path('delete_appointment/<int:pk>/',views.delete_appointment,name='delete-appointment'),

    path('schedule/',views.schedule,name='schedule-page'),
    path('add_schedule/',views.add_schedule,name='add-schedule'),
    path('update_schedule/<int:pk>/',views.update_schedule,name='update-schedule'),
    path('delete_schedule/<int:pk>/',views.delete_schedule,name='delete-schedule'),

    path('department/',views.department,name='department-page'),
]
