"""
Chef and Instant Noodles
Chef has invented 1-minute Instant Noodles. As the name suggests, each packet takes exactly 1 minute to cook.
Chef's restaurant has X stoves and only 1 packet can be cooked in a single stove at any minute.
How many customers can Chef serve in Y minutes if each customer orders exactly 1 packet of noodles?
"""

a,b=map(int,input().split())

c=a*b

print(c)



"""
Positive and Negative
Write a program to check whether a number given as user input is positive, negative, or zero.

"""
a=int(input())
if(a>0):
    print("Positive")
elif(a<0):
    print("Negative")
else:
    print("Zero")
