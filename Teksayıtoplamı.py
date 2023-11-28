while True:
    try:
        a = int(input("\033[0;35;47m Sayı giriniz : "))
        toplam = 0
        for t in range(a):
            if(t % 2 == 1):
                toplam = t + toplam

        print(a," sayısına kadar olan tek sayılar toplamı : ",toplam)
        c = input("Çıkmak için C'ye basın. Yoksa enter'a basın : ").lower()
        if(c == 'c'):
            print("\033[0;35;47m yine gelin lütfen, sizi özleyeceğim <3 \n")
            break          
    except:
        print("Yanlış girdi yaptınız. Lütfen tam sayı giriniz.")    