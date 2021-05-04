
# region pirint

"""
print("alperen çelik")
print("kocatepe üni.")

print("alperen","<",3,"melike")
"""

"""
escape karakteri

print("alperen\nçelik\tmelike\ndilekçi")

print("\\")
print("\"")
print('Merhaba Ece\'nin dünyasi')

"""
"""
# end keywordu

print("Hayatta"," En","Hakiki")
print("Mürşit","İlimdir")
print("-----------------") 

print("Hayatta"," En","Hakiki",end="\n")
print("Mürşit","İlimdir")
print("-----------------")

"""
"""
# sep keywordu              ***sep ve end default olarak örneklerdeki gibidir.

print("Hayatta"," En","Hakiki","Mürşit","İlimdir")
print("-----------------")

print("Hayatta"," En","Hakiki","Mürşit","İlimdir",sep=" ")
print("-----------------")
"""
"""
#örnek 

print("ecodation","egitim","kurumlari",sep=">>",end=".")
"""
# endregion

# region örnek1
"""
print("Dunya'nin","en","guzel","sehri",sep="♥",end="→ISTANBUL")
print("\n----------------\n")
print("\"Ege\'nin\"",'"incisi"','"izmir"',sep="☼",end="!")
print("\n----------------\n")
"""
# endregion

# region type
"""
print(type("alperen"))
print(type(1876))
print(type(True))
print(type(3.14))
"""
# endregion

# region concat + swap
"""
okul_no = 214
ad = "Alperen"
soyad = "Celik"
sinav_notu = 100

print("okul numarasi",okul_no,"olan",ad,soyad,sinav_notu)

temp = okul_no
okul_no = sinav_notu
sinav_notu = temp

print("okul numarasi",okul_no,"olan",ad,soyad,sinav_notu)

a = 5 
b = 15
print("a:",a,"b:",b)
    
a,b = b,a     ### pythonun güzelliği :))
print("a:",a,"b:",b)
"""
# endregion


# region
"""
sayi = 471
birler = sayi % 10
onlar = sayi % 100
onlar = onlar//10
yuzler = sayi % 1000
yuzler = yuzler//100
sonuc = yuzler+onlar+birler
print(sonuc)
"""
"""
sayi = 471
birler = sayi % 10   
onlar = ((sayi % 100) -birler)/10
yuzler = ((sayi % 1000) -onlar)/100
print(yuzler)

"""
#endregion
