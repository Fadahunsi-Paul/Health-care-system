from django.urls import path
from .import views

app_name = "care"

urlpatterns = [
    path('', views.home, name="home"), 
    path('doctor/',views.doctor, name='doctor-page'),
    path('add-doctor/',views.add_doctor,name='add-doctor'),
    path('update_doctor/<int:pk>/',views.update_doctor,name='update_doctor'), 
    path('delete_doctor/<int:pk>/',views.delete_doctor,name='delete-doctor'),
]
