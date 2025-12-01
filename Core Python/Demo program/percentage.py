perc = int(input("Enter Percentage "))
if(perc < 35):
    print("Failed")

else:
    if(perc >70):
        if(perc > 80):
            if(perc > 90):
                print("A")
            else:
                print("B")
        else:
            print("C")
    else:
        print("D")


