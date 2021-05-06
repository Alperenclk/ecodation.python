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



