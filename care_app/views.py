from django.shortcuts import render,redirect,get_object_or_404
from .model.appointment import Appointment
from .model.department import Department
from .model.doctor import Doctors
from .model.patient import Patients
from .forms import DoctorForm,PatientForm,AppointmentForm
from django.contrib import messages

# Create your views here.


def home(request):
    total_doctors = Doctors.objects.count()
    total_patients = Patients.objects.count()
    doctors = Doctors.objects.all()
    context = {
        'total_doctors':total_doctors,
        'doctors':doctors,
        'total_patients':total_patients,
    }
    return render(request, 'main/index.html',context) 

def doctor_profile(request,pk):
    profile = Doctors.objects.get(id=pk)
    context = {
        'profile':profile,
    }
    return render(request,'main/profile.html',context)

def doctor(request):
    doctors = Doctors.objects.all()
    context = {
        'doctors':doctors,
        }
    return render(request,'main/doctors.html',context)


def add_doctor(request):
    form = DoctorForm()
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save() 
            return redirect ('care:doctor-page')   
    else:
        form=DoctorForm() 
    context = {'form':form}
    return render(request,'main/add-doctor.html',context)

def update_doctor(request, pk):
    doctor = Doctors.objects.get(id=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Doctor Updated Successfully')
            return redirect('care:doctor-page') 
        else:
            messages.error(request, 'Correct the Errors below') 
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'main/edit-doctor.html',{'form':form})  

def delete_doctor(request, pk):
    delete = get_object_or_404(Doctors, id=pk)
    if request.method == 'POST':
        delete.delete() 
        return redirect('care:doctor-page')
    return render(request, 'main/delete-doctor.html', {'delete': delete})

def patients(request):
    patients = Patients.objects.all()
    context = {'patients':patients}
    return render(request,'main/patients.html',context)

def add_patients(request):
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('care:patients-page')
    else:
        form=PatientForm()
    return render(request,'main/add-patient.html',{'form':form})

def update_patients(request,pk):
    patient = Patients.objects.get(id=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request,'Patient updated Successfully')
            return redirect('care:patients-page')
        else:
            messages.error(request, 'Correct the Errors below') 
    else:
        form = PatientForm(instance=patient)
    return render(request, 'main/edit-patient.html',{'form':form})

def delete_patients(request,pk):
    delete = get_object_or_404(Patients, id=pk)
    if request.method == 'POST':
        delete.delete() 
        return redirect('care:patients-page')
    return render(request, 'main/delete-patient.html', {'delete': delete})
    
def appointment(request):
    appointment = Appointment.objects.all()
    context = {
        'appointment':appointment,
    }
    return render(request,'main/appointments.html',context)

def add_appointment(request):
    form = AppointmentForm()
    if request.method == "POST":
        form = AppointmentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Appointment created Successfully')
            return redirect('care:appointment-page')
        else:
            messages.error(request, "Correct the errors below")
    else:
        form = AppointmentForm()
    return render(request,'main/add-appointment.html',{'form':form}) 

def update_appointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request,'Appointment updated Successfully')
            return redirect('care:appointment-page')
        else:
            messages.error(request, 'Correct the Errors below') 
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'main/edit-appointment.html',{'form':form})

def delete_appointment(request, pk):
    delete = get_object_or_404(Appointment, id=pk)
    if request.method == "POST":
        delete.delete()
        return redirect("care:appontment-page")
    return render (request, 'main/delete-appointment.html', {'delete':delete})

