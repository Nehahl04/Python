#Time module program
print("code 1")

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
print("\n")




print("Code 2")

import time
t = time.strftime('%H:%M:%S')
# hour = int(time.strftime('%H'))
hour = int(input("Enter hour:"))
print(hour)

if(hour>=0 and hour<12):
    print("Good Morning!!!")
elif(hour>=12 and hour<17):
    print("Good Evening!!!")
if(hour>=17 and hour<0):
    print("Good Night!!!")


