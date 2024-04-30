from datetime import datetime

GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
]

STATUS_CHOICES = {
        'Pending':'Pending',
        'In_Progress':'In Progress',
        'Completed':'Completed'
}

# def patient_age(birth_year, birth_month, birth_day):
#     today = datetime.today()
#     birth_date = datetime(birth_year, birth_month, birth_day)
#     age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
#     return age

