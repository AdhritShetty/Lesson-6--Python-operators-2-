height=float(input("enter your height in here{in m}:"))
weight=float(input("enter your height in here{in kg}"))

BMI=weight/height**2
print("your BMI is:",BMI)
if BMI<=18.4:
    print("You are underweight")
elif BMI<=24.9:
    print("You are healthy")
elif BMI<=29.9:
    print("you are over weight")
elif BMI<=34.9:
    print("you are severly over weight")
else:
    print("it is invalid")