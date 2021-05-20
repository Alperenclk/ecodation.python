# Python basic (Part -I) [150 exercises with solution]
# https://www.w3resource.com/python-exercises/python-basic-exercises.php#EDITOR

# region 021/ even or odd
"""
x = int(input("give a number\t:"))

if x%2 == 0:
    print(f"this number is even.\t{x}")

else:
    print(f"this number is odd.\t{x}")    
"""
# endregion

# region 022/ .count a number
"""
def find(x):
    count = 0
    for i in x:
        if i == 4:
            count+=1
    return count

print(find([1, 4, 6, 7, 4]))
print(find([1, 4, 6, 4, 7, 4]))
"""
"""
x=[1, 4, 6, 4, 7, 4]   # python guzelligi :))
print(x.count(4))
"""
# endregion

# region 023/ string
"""
def fonk(st): 
    empty = " "
    n = int(input("enter copies value\t:"))
    for i in range(n):
        empty = empty + st[:2]

    return empty
print(fonk("Alperen"))
"""
# endregion

# region 024/ vowel
"""
def check(str):

    vowel = ["a","A","e","E","i","I","o","O","u","U"]

    for i in vowel:
        if i == str:
            
            return  "this letter is a vowel"
print(check("a"))
"""
"""                                          #** Python guzelligi :))
def is_vowel(char):
    wovel = "aeiouAEIOU"
    return char in wovel

print(is_vowel("A"))
print(is_vowel("a"))
print(is_vowel("k"))
"""
# endregion

# region 025/ check
"""
def check(x,y): 
    return y in x

print(check([1, 5, 8, 3], -1))
"""
# endregion

# region 026/  histogram
"""
def histogram(x):
    y ="*"
    for i in range(len(x)):
        print(y*x[i])

histogram([2, 3, 6, 5,15])
"""
# endregion

# region 027/
"""
def concatenate(liste):
    st = ""
    for i in liste:
        st += str(i)
    return st
print(concatenate(["a",2,5,6,"A"]))
"""
# endregion

# region 028/ break
"""
numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 743, 527
]

for i in numbers:
    if i ==237:
        break;
    if i % 2 == 0:                
        print(i)
"""  
# endregion

# region 029/  .difference
"""
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))

"""
# endregion

# region 031/ the greatest common divisor
"""
def gcm(x,y)  :
    sayi = 1
    for i in range(1,14):

        if x%i==0 and y%i==0:
            print(i)
            x /=i
            y /=i
            sayi *=i
    return sayi
print(gcm(20,30))
"""
# endregion

# region 032/ the least cammon multiple 
"""
def lcm(x,y):

    if x > y:
        z = x
    else:
        z = y 
    
    while(1):
        if z%x==0 and z%y==0:
            print(z)
            break
        z+=1

print(lcm(8,9))         
"""
# endregion

# region 035/ equal
"""
def orn(x,y):

    if x == y or (x+y==5) or abs(x-y)==5:
        return  True

print(orn(5,10))
"""
# endregion

# region 036/ isinstance and raise
"""
def add_numbers(a, b):
    if not isinstance(a,int) and isinstance(b,int):
        raise TypeError("Input must be integers")

    return a + b

print(add_numbers("a",6))
"""
# endregion

# region 041/ "os" check whether a file exists   
"""

open("abc.text","w")
print(os.path.isfile("abc.text"))
"""
"""
import os
print("Current file name:",os.path.realpath(__file__))
""" 
# endregion

# region 043/to get OS name, platform and release information
"""
import platform
import os
print(os.name)
print(platform.system())
print(platform.release())
"""

# endregion

# region 060/ calculate the hypotenuse
"""
from math import sqrt
a = int(input("Give a long side\t:"))
b = int(input("Give a short side\t:"))

c = sqrt(a**2+b**2)
print(f"hypotenuse is\t:{c}")
"""
# endregion

# region 069/ sort number without conditional statements
"""
a = int(input("Give a number\t:"))
b = int(input("Give a number\t:"))
c = int(input("Give a number\t:"))

a1 = max(a,b,c)
a3 = min(a,b,c)
a2 = (a+b+c)-a1-a3
print("These numbers order is\t:",a1,a2,a3)
"""
# endregion







