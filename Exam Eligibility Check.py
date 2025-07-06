medical_cause = input("do you have medical cause Y or N ")
attendance = int(input("enter attendence of the student "))
if medical_cause == 'y':
    print("you are allowed")
else:
    if attendance >= 75 :
     print("you are allowed")
    else: 
       print("you are not allowed")