import random
colors = ['r', 'g', 'b', 'p', 'y', 'c']
picked = [{place: random.choice(colors) for place in range(1, 5)}]

print(picked)
def kirmizi(liste1, liste2):
    eslesme_sayaci = 0
    for kutuphane1, kutuphane2 in zip(liste1, liste2):
            for anahtar, deger1 in kutuphane1.items():
                if anahtar in kutuphane2 and kutuphane2[anahtar] == deger1:
                    eslesme_sayaci += 1
    return eslesme_sayaci

def beyaz(liste1, liste2):
    all = ''.join(sorted([f"{value}" for key, value in liste1[0].items()]))
    search = ''.join(sorted([f"{value}" for key, value in liste2[0].items()]))
    white = 0
    for i in search:
        if i in all:
            white += 1
    return white


for _ in range(13):
    user_input = input("(R)ed, (G)reen, (B)lue, (P)ruple, (Y)ellow, (C)yan, renkleri içinden lütfen sadece 4 rengin baş harfini girin: ").lower()
    user_colors = {place: color for place, color in enumerate(user_input, 1)}
    matching_count = kirmizi(picked, [user_colors])
    matching_count_2 = beyaz(picked, [user_colors])
    if(picked == [user_colors]):
        print("Bildiniz !!!")
        break 
    elif(matching_count != 0 | matching_count_2 != 0):
        print("{} yeri doğru tahmin ettiniz, {} yeri yanlış ancak tahimin içinde".format(matching_count, matching_count_2), [user_colors])
    else:
        print("Hiç bilemediniz", [user_colors])