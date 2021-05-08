# Python basic (Part -I) [150 exercises with solution]
# https://www.w3resource.com/python-exercises/python-basic-exercises.php#EDITOR

# region 001/escape character
"""
Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are

print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.")
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are")
"""
# endregion

# region 002/python version
"""
import sys
print("Python version:")
print(sys.version)
"""
# endregion

# region 003/current date
"""
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
"""
# endregion

# region 004/area of circle
"""
radius = float(input("give a radius"))
pi = 3.14
print("Area is:",pi*(radius**2))
"""
# math library
"""
from math import pi  
radius = float(input("give a radius"))
print("the area of the circle is:",pi*(radius**2))
"""
# endregion

# region 005/revers string
"""
name = str(input("your name:"))
surname = str(input("your surname:"))
print(surname, name)
"""
# endregion

# region 006/ comma separated
"""
values = input("give me numbers with comma separated:")
liste = values.split(",")
print(liste)
tuplee = tuple(liste)
print(tuplee)
"""
#endregion

# region 007/ 
"""
file_name = input("please give a file name\t:")
f_name = file_name.split(".")
print(f_name[-1])
"""
# endregion

# region 008/ list sample
"""
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0],color_list[-1])
"""
# endregion

# region 009/ extract with %i
"""
exam_st_date = (11,12,2014)
print("your exam date is\t:%i/%i/%i"%exam_st_date )
"""
# endregion

 #region 010/ simple calculation
"""
value = int(input("give a number\t:"))

print((value*100) + ((value*2)*10)+ (value*3))
"""
# endregion

#region 011/ __doc__
"""
print(list.__doc__)
"""
# endregion

#region 012/  calendar 
"""
import calendar 

y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))
"""
# endregion

# region 013/ uc tirnak

# endregion

# region 014/  from  datetime
"""
from  datetime import date 
l_date = date(2021,12,24)
f_date = date(2021, 5, 7)
delta = l_date - f_date
print(delta.days)
"""
# endregion

# region 015/ volume of a sphere 
"""
pi = 3.1415926535897931
r= 6.0
V= 4.0/3.0*pi* r**3
print('The volume of the sphere is: ',V)
"""
# endregion

# region 016/ if
"""
def difference(n):
	if n<=17:
		return (17-n)
	else:
		return (n-17)*2
	
print(difference(18))
print(difference(8))
"""
# endregion

# region 017/ number in range(100,2000)
"""
number = int(input("give a number\t:"))
print(number in range(100,2000))
"""
# endregion

# region 018/ 
"""
liste = input("give three numbers with comma separated \t:")
liste = liste.split(",")

if int(liste[0]) == int(liste[1]) == int(liste[2]):
	print(int(liste[0])**3)
else:
	print(int(liste[0]) +int(liste[1]) + int(liste[2]))
"""
# endregion

# region 019/ 
"""
new = input("give new string that start 'Is'\t:")

if new[:2] =="Is":
	print(new)

else:
	print("Is" + new )
"""
# endregion

# region 020/  copies of a given string
"""
def copies(n):
	new = input("give a string\t:")
	return new*n
print(copies(5))
"""
"""
def larger_string(str, n):
   result = ""
   for i in range(n):
      result = result + str
   return result
"""
# endregion






# endregion













