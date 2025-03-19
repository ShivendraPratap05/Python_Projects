# Coading and decoding of the programm from :--
# English -------->  Secret Code (vice versa)...

#Encding 
import random
String="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
rr=random.sample(String,4)
bb="".join(rr)

x=input("Encode or Decode ??")
match x:
    case "Encode":
        Name=input("Enter the Name::")
        print("YOur name is::", Name)
        
        if(len(Name)<=4):
            print("  ")
            print("Secret Code is ::",Name[::-1])
        else:
            x=Name[0:4:]
            y=Name[4:]
            new=y+x
            new1=new+bb
            print(" ")
            print("Your Secret Code is::",new1)

#Decoding:---

    case "Decode":
        Name=input("Enter the Secret Code::")
        print("YOur Coded Name is::",Name)

        if(len(Name)<=4):
            print(" ")
            print("Your Name is::",Name[::-1])
        else:
            x=Name[:-4]
            #print(x)
            y=x[-4:]
            #print(y)
            z=x[:-4]
            #print(z)
            new=y+z
            print(" ")
            print("YOur Name is::",new)
    case _:
        print("Please Select 'Encode' or 'Decode'")
print(" ")                        
print("Code COmpleted successfully................THANK YOU")