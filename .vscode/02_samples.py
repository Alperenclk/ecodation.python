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
