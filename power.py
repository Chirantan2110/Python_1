#Develop a Python script that calculates and prints the result of raising a 
#user-input base to a user-input exponent without using the ** operator. 

a=int(input("enter the base"))
b=int(input("enter the exponent"))
p=1
for i in range(1,b+1):
    p=a*p
print(p)  