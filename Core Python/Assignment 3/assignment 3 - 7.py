#Write a program to check if user has entered correct userid and password.

correct_userid = "harshal"
corrent_password = "123"

#Take input userid Or Password
userid = input('Enter the UserId : ')
password = input('Enter the password :')

if(correct_userid == userid and corrent_password == password):
    print("Login Successful!")
else:
    print("Invalid User ID or Password.")
    
    



