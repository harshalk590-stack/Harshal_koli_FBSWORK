#Write a program to input any alphabet and check whether it is vowel or consonant.

#Take input alphabet

ch = input("Enter Single alphabet :")
ch = ch.lower()

if ch.isalpha() and len(ch) == 1:
    if ch in ['a', 'e', 'i', 'o', 'u']:
        print(ch, "is a Vowel")
    else:
        print(ch, "is a Consonant")
else:
    print("Invalid input! Please enter a single alphabet.")
