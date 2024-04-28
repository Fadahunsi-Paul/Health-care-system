# from .model.patient import Patients
from datetime import datetime

GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
]

def patient_age(birth_year, birth_month, birth_day):
    today = datetime.today()
    birth_date = datetime(birth_year, birth_month, birth_day)
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# def main():
#     try:
#         birth_day = int(input("Enter your birth day (1-31): "))
#         birth_month = int(input("Enter your birth month (1-12): "))
#         birth_year = int(input("Enter your birth year: "))

#         age = patient_age(birth_day, birth_month, birth_year)
#         if age < 0:
#             print("Invalid birth date!")
#         else:
#             print("Your age is:", age)
#     except ValueError:
#         print("Invalid input! Please enter valid numbers.")

# if __name__ == "__main__":
#     main()
