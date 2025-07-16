for i in range(11):
    print("3 X", i, "=",3*i)
    if (i==6):
     break #breaks the loop at given conition
print("left the loop")    

for i in range(11):
    print("3 X", i, "=",3*i)
    if (i==9):
        print("skip the iteration")
        continue#skips the particular iteration

for i in range(1,50,1):
    print(i,end=" ")
    if(i==25):
        break
    else:
        print("MI")

        
for i in [2,4,6,8,10]:
    if(i%2):
     continue
    print(i)
        
    
    
