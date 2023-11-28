sayi = int(input("Bir sayı girin: "))

if sayi < 2:
    print(f"{sayi} asal bir sayı değildir.")
else:
    asal = True
    for i in range(2, int(sayi**0.5) + 1):
        if sayi % i == 0:
            asal = False
            break

    if asal:
        print(f"{sayi} asal bir sayıdır.")
    else:
        print(f"{sayi} asal bir sayı değildir.")
