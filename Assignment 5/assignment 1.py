#1. Write a program to prompt user to enter userid and password. If Id and
#password is incorrect give him chance to re-enter the credentials. Let him try 3
#times. After that program to terminate.

correct_id= 'harshal'
correct_pass = '123456'

attempts = 3

for i in range(attempts):
    user_id = input("Enter User ID: ")
    password = input("Enter Password: ")

    if user_id == correct_id and password == correct_pass:
        print("Login Successful!")
        break
    else:
        print("Incorrect ID or Password")
        print("Remaining attempts:", attempts - i - 1)
else:
    print("Too many wrong attempts. Program terminated.")



