from ders7 import pi
import ders7 # python bütün importları bytcode olarak tutuyor eğer module içinde değişiklik yaparasak değişiklik gözükmeyecek zorla güncellememiz gerekecektir
import importlib # bu kütüphane bu tarz imporları yenilemek için kullanılan bir kütüphane

print(pi)
print(ders7.area(2))

import os
print(os.getcwd())
dir(ders7)
print(ders7.__doc__)
print(ders7.__name__)

####################################### Hata kontrolü #####################################

try: # bu kod bloğunu dener eğer belirlenen hata çıkarsa
    print(int(input("Sayı gir")))
except ValueError: # bu kod bloğuna girer # KeyError, NameError, TypeError, OverflowError, ZeroDivisionError gibi bir çok hata mesajı mevcut
    print("value error hatası")

