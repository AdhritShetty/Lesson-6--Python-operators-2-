letterornumber = input("enter the number or alphabet: ")
if letterornumber.isalpha():
    print("it is an alphabet")
elif letterornumber.isnumeric():
    print("it is a number")
else:
    print("it is invalid")