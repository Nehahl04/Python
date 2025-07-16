#string 
name= "python"

#siri = "She said ,Hi Neha"
name2="programming"

print("siri")

print("Hello,"+name )
#print siri
print(name[0])
print(name[4])
#print   (name[6]) throws an error

print("Lets use for loop in string\n")
for character in name:
    print(character)
    
for character in name2:
    print(character)
    #string slicing 
names="NehaAhlawat,Nikita"
print(names[0:4])
print(names[4:11])
#string length
fruit="Apple"
len1= len(fruit)
print("Apple is a",len1,"letter word.")

#string as an array
pie="ChocoPie"
plen=len(pie)
print(plen)
print(pie[:5])
print(pie[5:8])#including 5 but not 8 
print(pie[5:])
#negative slicing
print(pie[:-5])
print(pie[0:len(pie)-3])#len(pie)-3 = 5 = first five characters
print(pie[-4:8])#-4 from first -opie
print(pie[:-7])
print(pie[-6:8])
print(pie[-6:-3])#in negative slicing python automatically subtracts from len

nm="Harry"
print(nm[-4:-2])
len2=len(nm)
print(len2)

#STRING METHODS (strings are immutable)
str1="neha"
print(str1.upper()) #upper case 
str2="NEHA\nAHLAWAT"
print(str2.lower())#lower case

a="Python Programming"
print(a)
lenp= len(a)
print (lenp)

print(a.upper())
print(a.lower())

print(a.replace("Python" , "Pro"))#replace all occ. of str with another str

print(a.split(" "))#split str at specified instance and return the separated str as list itmes

#capitalize() turns first char to uppercase and rest other to lowercase
str1="neha"
CapStr1=str1.capitalize()
print(CapStr1)
str2="ahlawat"
CapStr2=str2.capitalize()
print(CapStr2)

blogheading="introduction to java"
print(blogheading.capitalize())

str1 = "Welcome to the console!!!"
print(str1.endswith("to"))
print(str1.endswith("!!!"))#tells whether str endswith it in boolean
print(str1.startswith("Wel"))
print(str1.endswith("to",4,10))#tells if 4-10 index endswith to in boolean
print(len(str1))
print((str1.center(50)))# center() align the str to center as per parameters given 

print(a.count("Python Programming"))#return no. of times given value has occured 

str3 = "nehanikita"
print(str3)
countStr = str3.count("a")
print(countStr)
print(str3.find("ni")) #find()search for first occ. of given value and returns the index where it is present in the str
print(str3.find("fe"))
#find() return -1 if occurence is not present in the str
print(str3.index("i")) #tells index of first occ.
print(str3.index("a")) #index method gives syntax error if not found 

str4="Weltopython13.3"
print(str4)
print(str4.isalnum()) #isalnum contains A-Z,a-z,0-9 and returns bool and don't contain space
print(str4.isalpha()) #isalpha contains A-Z,a-z doesn't contain 0-9 and returns bool
print(str3.isalpha())
print(str3.islower())#islower() and isupper() returns bool if str is lower or upper 
print(str3.isupper())
print(str4.isupper())#isupper() checks if all characters of str are uppercase

str4="Merry Christmas"
print(str4)
print(str4.isprintable())#gives true if str is printable and \n is not printable so it will return false 
str5="      " #spacebar using tab or spacebar
print(str5)
print(len(str5))
print(str5.isspace())#isspace returns true only if str contains spacebar

str6="World Wide Web"
print(str6)
print(str6.istitle())#istitle() returns true only if first letter of str is capitalize 
print(len(str6))
print(str6.swapcase())#swapcase  swaps upper and lower cases

str7="my name is neha ahlawat"
print(str7.title())
count.lines of code 







































































































































































      
    
    





