from django import forms
from care_app.model.doctor import Doctors
from care_app.model.schedule import Schedule

class ScheduleForm(forms.ModelForm):
    doctor_name = forms.ModelChoiceField(required=True,
        queryset=Doctors.objects.all(),
        required = True,
        widget=forms.Select(
            attrs={
                'class':'form-control'
            }
        ))

    days = forms.CharField(required=True,
        widget = forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    start_time = forms.TimeField(required=True,
        widget = forms.TimeInput(
            attrs={
                'class':'form-control',
                'type':'time'
            }
        )
    )

    end_time = forms.TimeField(required=True,
        widget=forms.TimeInput(
            attrs={
                'class':'form-control',
                'type':'time'
            }
        )
    )

    messaage = forms.CharField(required=True,
        widget=forms.Textarea(
            attrs={'class':'form-control'}
        )
    )

    status = forms.Select()

    class Meta:
        model = Schedule
        fields = '__all__'