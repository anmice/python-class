# Student Admission Filter

# Ask for student's age
age = int(input("Enter the student's age: "))

# Check if the age is between 10 and 20
if 10 <= age <= 20:
    print("Admission granted! ✅")
else:
    print("Admission denied. Age must be between 10 and 20. ❌")
