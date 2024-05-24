from django import forms
from care_app.model.doctor import Doctors
from care_app.model.department import Department

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