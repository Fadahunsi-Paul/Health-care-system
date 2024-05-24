from django import forms
from care_app.model.appointment import Appointment
from care_app.model.department import Department
from care_app.model.doctor import Doctors
from care_app.model.patient import Patients




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
        