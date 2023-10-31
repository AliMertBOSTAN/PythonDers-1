x = 'span'
y = 19
z = ['spannn']

print(x,y,z)
print(x,y,z, sep=', ,') # aralarına ayırmak için belirlediğim , , ekledi
print(x,y,z, end=' ..\n') # satır sonlarında ne yapacağını söyleriz
print(x,y,z, sep=',' ,end=' ..\n') # aynı anda ikisi birden kullanılabilir
# print(x,y,z, file=open('data.txt', 'w')) # dosyanın içine yazdırmak için

import os, sys

print('my os.getcwd', os.getcwd()) # show my cwd execution dir
print('my sys.path', sys.path[:6]) # show first 6 import paths

# temp = sys.stdout # kaybedersek tekrar buna eşitleyerek kurtarmak için
# sys.stdout = open('data.txt', 'w') # standart out'u data.txt dosyası olarak değiştirir

a = "aaaaa" + "aaaa"
print(a)
a = "bbbb"*3
print(a)
a = "asdaasdass"[0]
print(a)
a = "asdasfszz"[-1]
print(a)
a = "assadsdas"[1:3]
print(a)
a = len("adasişdlasşl")
print(a)
a = "abc" < "cba"
print(a)
a = "e" in "hello"
print(a)

def square(x):
    """Square fonksiyonu bir argüman alır ve karesini geri döndürür""" # fonksiyon tanımladıktan sonra 3 tırnak ile fonksiyonun açıklaması yazılabilir
    return x * x 
    
print(square(3) + square(9))

a = square