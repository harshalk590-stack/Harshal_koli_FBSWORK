gender = input("Enter Gender (M/F)")
age = int(input("Enter age :"))

if(gender == "M"):
    if(age >= 21):
        print("Eligibal for marriage. ")
    else:
        print("Pehle padh lo bhai")

else:
    if(age >= 18):
        print("Eligibal for marriage.")
    else:
        print("pehle padh le behen. ")

