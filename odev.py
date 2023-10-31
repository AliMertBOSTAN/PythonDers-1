while True:
    a = input(" Toplama için t'ye \n Çarpma için c'ye \n Çıkarma için ç'ye \n Bölme için b'ye \n Mod için m'ye basınız \n Üstel için u'ya basınız \n Çıkış için q basın \n").lower()
    def sayıSec():
        sayi1 = int(input("ilk Sayıyı girin"))
        sayi2 = int(input("ikinci Sayıyı girin"))
        return sayi1, sayi2 
    
    if a == "q":
        print("Çıkılıyor")
        break
    elif a == "t":
        sayi1, sayi2 = sayıSec()
        print(" {} + {} = {}".format(sayi1, sayi2, sayi1 + sayi2))
    elif a == "c": 
        sayi1, sayi2 = sayıSec()
        print(" {} x {} = {}".format(sayi1, sayi2, sayi1 * sayi2))
    elif a == "ç":
        sayi1, sayi2 = sayıSec()
        print(" {} - {} = {}".format(sayi1, sayi2, sayi1 - sayi2))
    elif a == "b":
        sayi1, sayi2 = sayıSec()
        print(" {} / {} = {}".format(sayi1, sayi2, sayi1 / sayi2))
    elif a == "m":
        sayi1, sayi2 = sayıSec()
        print(" {} mod ({}) = {}".format(sayi1, sayi2, sayi1 % sayi2))
    elif a == "u":
        sayi1, sayi2 = sayıSec()
        print(" {} ^ {} = {}".format(sayi1, sayi2, sayi1 ** sayi2))
    else:
        print("hatalı girdi yaptınız")
