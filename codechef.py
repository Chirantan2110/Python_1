"""
Chef and Instant Noodles
Chef has invented 1-minute Instant Noodles. As the name suggests, each packet takes exactly 1 minute to cook.
Chef's restaurant has X stoves and only 1 packet can be cooked in a single stove at any minute.
How many customers can Chef serve in Y minutes if each customer orders exactly 1 packet of noodles?
"""
#code-
a,b=map(int,input().split())

c=a*b

print(c)
#EOC
"""
How to accept multiple integers on separate lines
"""
#CODE-
A, B = map(int,input().split())
C, D, E = map(int, input().split())
F, G, H, I = map(int,input().split())
print(A, B, C, D, E, F, G, H, I)

#EOC
"""
Positive and Negative
Write a program to check whether a number given as user input is positive, negative, or zero.
"""
#code-
a=int(input())
if(a>0):
    print("Positive")
elif(a<0):
    print("Negative")
else:
    print("Zero")
#EOC

""""
Grades of Student
Write a program to print the grades of a student based on the marks he/she has obtained provided as input. The student is graded A if marks are greater than 90, B if marks are greater than 70, C if greater than or equal to 40, else F.
"""
#code-
x=int(input())
if(x>90):
    print("A")
elif(x>70):
    print("B")
elif(x>=40):
    print("C")
else:
    print("F")
    #EOC

"""Oneful Pairs
Chef defines a pair of positive integers 
(a,b) to be a 
Oneful Pair
Oneful Pair, if (a+b+(a*b)=111."""
#code-
a,b = map(int,input().split())
if(a+b+(a*b)==111):
    print("Yes")
else:
    print("No")
#EOC

"""
Print Squares
Write a program that utilizes a while loop to print the squares of numbers from 1 to N.
"""
#code-
num = int(input())
i=1
while(i<=num):
    print(i**2,end=" ")
    i=i+1
#EOC
"""
Print factorial
Write a program that uses a while loop to find the factorial of a given number.
"""
#code-
n=int(input())
fact=1
i=1
while(i<=n):
    fact=fact*i
    i=i+1
print(fact)  
#EOC

"""
Count Vowels
Write a program that uses a while loop to find no. of vowels in given input string of lowercase latin letters.

Note: Vowels in lowercase latin letters are: a, e, i, o and u.

"""
#code-
str1=input()
s=str1.lower()
#print(s)
f1=s.count("a")
f2=s.count("e")
f3=s.count("i")
f4=s.count("o")
f5=s.count("u")
v=f1+f2+f3+f4+f5
print(v)
#EOC
"""
Water Consumption
Recently, Chef visited his doctor. The doctor advised Chef to drink at least 2000 ml of water each day.Chef drank X ml of water today. Determine if Chef followed the doctor's advice or not.
"""
#CODE-
t = int(input())
for i in range(0,t):
    x =  int(input())
    if(x>=2000):
        print("Yes")
    else:
        print("No")

#EOF

"""
Given an array of ints length 3, return the sum of all the elements.
"""
#code-
def sum3(nums):
  sum=0
  for i in nums:
    sum+=i
  return sum  
    #EOC

















