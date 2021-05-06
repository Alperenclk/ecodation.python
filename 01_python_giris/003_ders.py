# region round()
"""
kilo = 70
boy = 1.75
v_k_e = kilo/(boy**2)
print("vucut kitle indeksiniz:",round(v_k_e,2))
"""
"""
temp = str(input("okulunuz?"))
print(temp)
"""
# endregion

# region casting / replication / concatenation
"""
a = "a"
b = "b"
c = "c"

print(a+b+c)

print(a*5)
"""
# endregion

# region fstring / format
"""
a =int(input("bir rakam girin"))

print("{}'nin bir eksiği {}".format(a,a-1))

print(f"{a}'nin bir eksiği {a-1}")     # ÖNEMLİ
"""

# endregion

# region lab_uygulama

# **** uc tirnak kullanımı

print(""" uc tirnak 
    cok 
        rahat
        """)





# elektirk faturasi
"""
a_t = float(input("lutfen aylik elektrik tuketiminii giriniz(kWh)\t:"))
a_e_b = a_t * 0.39736
d_b = a_e_b * 0.2474
t_e_b = a_e_b + d_b
trt_payi = 3.97
enerji_fonu = 1.39
e_t_v = 9.92
kdv = (t_e_b + trt_payi + enerji_fonu + e_t_v)* 0.18
vergi_t = trt_payi + enerji_fonu + e_t_v + kdv
print("masallah\t:{}".format(vergi_t))

t_fatura = vergi_t + t_e_b

print(f"Faturanız\t:{t_fatura}")

"""

# endregion