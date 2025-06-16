height = int(input("enter height in cm"))
weight = int(input("enter weight in kg"))
bmi = weight/(height/100)**2
print("your bmi is ", bmi)
if bmi <= 19:
    print("your under weight")
elif bmi <= 25:
    print("your healthy")
elif bmi <= 30:
    print("you are over weight")
else : 
    print ("you are obese")