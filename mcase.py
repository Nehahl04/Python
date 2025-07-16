x=int(input("Enter the value of x:"))
#x is the variable to match
match x:
    #if x is o
  case 0:
    print("x is zero")
    #case with if condition
  case 4:
    print("case is 4")
  case _ if x!=90:
    print(x, "is not 90")
  case _ if x!=80:
    print(x,"is not 80")
  case _: #default case will only be matched if others are not matched, it's basiclly just an else
        print(x)
        

