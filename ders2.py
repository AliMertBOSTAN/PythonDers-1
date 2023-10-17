door = True
closed = True
locked = True
if door is closed:
    if door is locked:
        print("unlock door")
    print("open door")
print("walk ")

age = 13 
if age <= 13:
    print(" çocuksun")
elif age > 13 and age < 20:
    print("gençsin")
else:
    print("yaşlısın")

hidden_number = 29

your_guess = int(input("tahmininizi girin"))
if your_guess == hidden_number:
    print("bildin")
elif your_guess < hidden_number:
    print("tahminin gizli sayıdan küçük")
else:
    print("tahminin gizli sayıdan büyük")

# turtle ile gülen yüz yap - ödev

# for variableName in groupOFValues:

for x in range(6): # range(9,19) gibi özel aralıkta verilebilir, range(1,100, 2) gibi 2 artışlı da verilebilir, range(5,0, -1) gibi negatif sayma işlemeleride yapılabilir
    print(x)

for harfler in " ali mert": # string'de verilebilir
    print(harfler)

sum = 0 
for i in range(1,11):
    sum = sum + (i ** 2)
print("1 den 10 a kadar sayıların karesinin toplamı = ", sum)

for _ in range(10): # tekrar değeri önemli değilse _ verierek gereksiz ram kullanımından kaçabiliriz
    pass # pass işlemi null operation olarak geçiyor boş bir adım olarak tanımlanabilir
    continue  # başa dönecek    
    break # döngüyü bitirecek

# while expression

while message != 'quit' # sadece değeri kontrol ediyor
while message is not 'quit' # aynı obje mi diye bakıyor

# python [-5, 256] ya kadar olan tam sayıları önceden kendisi memory'e kayıt eder ancak sonraki sayıları biz kendimiz obje olarak ekleriz
print('{} + {} = {}'.format(2,3,'five'))
print('{1} + {0} = {2}'.format(2,3,'five'))
print('{n1} + {n2} = {n3}'.format(n1=2,n2=3,n3='five'))

# a in 'alimert'
#  True dönecektir