"""
Hello firstname lastname! You just delved into python.

Function Description

Complete the print_full_name function in the editor below.

print_full_name has the following parameters:

string first: the first name
string last: the last name
Prints

string: 'Hello firstname lastname ! You just delved into python' where  and  are replaced with  and .
Input Format

The first line contains the first name, and the second line contains the last name.
"""
#code-

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")
#EOC

"""Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function."""

#code-
def is_leap(year):
    leap = False
    if((year%4==0 and year%100!=0) or year%400==0):
        return True
    else:  
        return leap

year = int(input())
print(is_leap(year))


#EOC
