# region 072/ dir
"""
# Imports the math module
import math            
#Sets everything to a list of math module
math_dir = dir(math)# 
print(math_dir)

"""

# endregion

# region 081/ .join
"""
list_of_colors = ['Red', 'White', 'Black']  
colors = "/".join(list_of_colors)
print("Colors:",colors)
"""
# endregion

# region 084/ .count
"""
string = "Alperen celik seni seviyorum."
x = input("Give a specific character\t:")
a=0
for i in string:
    if x==i:
        a+=1
print(f"{x} is have {a} times.  ")
"""
"""
string = "Alperen celik seni seviyorum."
x = input("Give a specific character\t:")
print("result is:\t",string.count(x))
"""

# endregion

# region 085/ ord  ASCII
"""
print(ord("A"))
"""

# endregion

# region 088/ %%%%%
"""
x = 20 ;y = 30
print("%d+%d=%d"%(x,y,x+y))
"""
# endregion

# region 094/ byte 0<x<128
"""
x =b'Alperen'
print(list(x))
"""

# endregion

# region 095/ try excep finally
"""
str = "s123"

try:
     i= float(str)

except (ValueError,TypeError):
    
    print("not numaric")
finally:
    print("Hello")
"""


# endregion

# region 098/ systm time
"""
import time

print(time.ctime())
"""
# endregion

# region 102/ .split
"""
f_path = "Alperen.py"
f_name = f_path.split(".")
print("File name is:",f_name[0])
print("File type is:."+f_name[1])
"""
# endregion

# region 112/ del
"""
color = ["Red", "Black", "Green", "White", "Orange"]
del color[0]
print(color)
"""
# endregion

# region 113/ try except isinstance raise
"""
x = input("give a number")

if not isinstance(x,int):
    raise ValueError("Error!! THIS INPUT İS NOT A NUMBER!")
"""
"""

try:
    a = int(input("Input a number: "))
    
except ValueError:
    print("TypeError!! THIS INPUT İS NOT A NUMBER! ")

"""
# endregion

