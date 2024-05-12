from django import forms
from .model.appointment import Appointment
from .model.department import Department
from .model.doctor import Doctors
from .model.patient import Patients

class DoctorForm(forms.ModelForm):
    first_name = forms.CharField(required=True,
    widget = forms.TextInput(
        attrs={
            'placeholder':'Enter First name',
            'class':'form-control'
        }
    ))
    last_name= forms.CharField(required=True,
    widget = forms.TextInput(
        attrs={
            'placeholder':'Enter Second name',
            'class':'form-control'
        }
    ))
    email = forms.EmailField(required=True,
    widget = forms.TextInput(
        attrs={
            'placeholder':'Enter Email',
            'class':'form-control'
        }
    ))
    date_of_birth = forms.DateField(required=True,
    widget = forms.DateInput(
        attrs={
            'class':'form-control', 
            'type': 'date'
        }
    )) 
    
    gender=forms.RadioSelect() 

    doctor_id= forms.CharField(required=True,
    widget = forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))

    specialty=forms.ModelChoiceField(
    queryset=Department.objects.all(),
    required=True,
    widget= forms.Select(
        attrs={
            'class':'form-control'
        }
    ))
    phone_number = forms.CharField(required=True,
    widget = forms.TextInput(
        attrs={
            "placeholder":'Enter phone number',
            'class':'form-control'
        }
    ))
    image = forms.ImageField(required=True,
    widget=forms.ClearableFileInput(
        attrs={
            'class':'form-control'
        }
    ))

    class Meta:
        model = Doctors
        fields = "__all__"

class PatientForm(forms.ModelForm):
    first_name = forms.CharField(required=True,
    widget = forms.TextInput(
        attrs={
            'placeholder':'Enter First name',
            'class':'form-control'
        }
    ))
    second_name= forms.CharField(required=True,
    widget = forms.TextInput(
        attrs={
            'placeholder':'Enter Second name',
            'class':'form-control'
        }
    ))
    email = forms.EmailField(required=True,
    widget = forms.TextInput(
        attrs={
            'placeholder':'Enter Email',
            'class':'form-control'
        }
    ))
    date_of_birth = forms.DateField(required=True,
    widget = forms.DateInput(
        attrs={
            'class':'form-control', 
            'type': 'date'
        }
    )) 
    
    gender=forms.RadioSelect() 

    address=forms.CharField(
    required=True,
    widget= forms.TextInput(
        attrs={
            'placeholder':'Address here',
            'class':'form-control'
        }
    ))

    phone_number = forms.CharField(required=True,
    widget = forms.TextInput(
        attrs={
            "placeholder":'Enter phone number',
            'class':'form-control'
        }
    ))
    image = forms.ImageField(required=True,
    widget=forms.ClearableFileInput(
        attrs={
            'class':'form-control'
        }
    ))

    class Meta:
        model = Patients
        fields = "__all__"
        
class AppointmentForm(forms.ModelForm):
    appointment_id = forms.CharField(required=True,
    widget = forms.TextInput(
        attrs={
            'placeholder':'Enter Id',
            'class':'form-control'
        }
    ))
    doctor=forms.ModelChoiceField(
    queryset=Doctors.objects.all(),
    required=True,
    widget= forms.Select(
        attrs={
            'class':'form-control'
        }
    ))
    phone_number= forms.CharField(required=True,
    widget = forms.TextInput(
        attrs={
            'placeholder':' Phone number',
            'class':'form-control'
        }
    ))
    date = forms.DateField(required=True,
    widget = forms.DateInput(
        attrs={
            'class':'form-control', 
            'type': 'date'
        }
    ))
    patient=forms.ModelChoiceField(
    queryset=Patients.objects.all(),
    required=True,
    widget= forms.Select(
        attrs={
            'class':'form-control'
        }
    ))
    department_of_appointment=forms.ModelChoiceField(
    queryset=Department.objects.all(),
    required=True,
    widget= forms.Select(
        attrs={
            'class':'form-control'
        }
    ))  
    reason = forms.CharField(required=True,
    widget = forms.Textarea(
        attrs={
            'class':'form-control', 
        }
    ))
    time = forms.TimeField(required=True,
    widget = forms.TimeInput(
        attrs={
            'class':'form-control', 
            'type': 'time'
        }
    ))
    status=forms.Select(
    # required=True,
    )


    class Meta:
        model = Appointment
        fields = "__all__"
        