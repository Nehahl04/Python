#if condition: executes only one condt. at a time
#1ST PROGRAM 
a=int(input("Enter your age:"))
print("your age is:",a)
if(a>18):
    print("you can drive")
    print("yes")
else:
    print("you can not drive")
    print("No")
print("yay!!")#this will print whether a>18 or not it's not a part of else  

#2ND PROGRAM

duoprize="400"
budget="500"
if(duoprize <= budget):
    print("Add 2 duos to the cart.")
else:
    print("Don't add duos to the cart.")
    
#3RD PROGRAM
num=int(input("Enter the number:"))
if (num<0):
    print("Number is negative.")
elif(num == 0):
    print("Number is zero.")
elif(num == 100):
    print("Number is greater")
else:
    print("Number is positive.")
print("code is completed")  

