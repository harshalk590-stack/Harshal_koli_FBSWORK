# Convert the time entered in hh,min and sec into seconds.

#take ipuut hour, min, second
hour = int(input('Enter the hour'))
min = int(input('Enter the min'))
sec = int(input('Enter the sec'))

#operation on the task
#1 hour = 3600 seconds
#1 minute = 60 seconds
sum = hour*3600 + min*60 + sec
print('Hour, minute, Seconds is : ', sum)

