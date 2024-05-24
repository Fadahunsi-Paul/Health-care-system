from datetime import datetime

GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
]

STATUS_CHOICES = {
        'Pending':'Pending',
        'In Progress':'In Progress',
        'Completed':'Completed'
}

DOC_STATUS = {
        'Available' : 'Available',
        'Unavailable': 'Unavailable'
}
# def patient_age(birth_year, birth_month, birth_day):
#     today = datetime.today()
#     birth_date = datetime(birth_year, birth_month, birth_day)
#     age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
#     return age

