a = 5j

print(a)
print(type(a))

for i in range(16): # for each şekilde çalışır
    print(f"{f'{i:d}':>2} : {f'{i:b}':>5} : {f'{i:X}':>2}") # f formatlamak için kullanılır i: (d = decimal, b = binary, X = hexadecimal)( > sola yaslamak için sonrasında gelen sayı kaç basamak sonra yazmaya başlayacağı ( < sağ, ^ oratla))

import decimal

a = decimal.Decimal('0.0000001')
print(type(a), a)
float(a)
print(type(a), a)

a = 3 
c = a + 1 , a - 1
print(type(c))

print('hello')
print("hell'o") # içinde tırnak kullanabiliyorum
print("""hel\nlo""") # içinde hem iki tırnağı kulanabilirsin hem \n gibi enter, \t tab gibi şeyleri kullanabilirim

s = "hello"
a, b, c, d, e = s
print(a)
print(e)

_, b, c, d, e = s # gereksiz tanımlamadan kaçındık _ bu işe yaradı

print("test" * 5) # stringler çarpılabiliyor

a = 1234.567
b = 45.67834
c = 45.67834
d = (a + b) + c
e = a + (b + c)
print(d) # 1325.9236799999999
print(e) # 1325.92368

# % artık değeri verir
# // bölümü verir

print(int(False)) # 0
print(int(True)) # 1
print(not 0) # True
print(not 1) # False

print("""
             \\\\\\/// \n
           |  *   * | \n
           |        | \n
           |  ----  | \n
               /\\    \n""") # ödev

age = input("yaşınızı sayı olarak girin :\t")
print("emekli olmaya", 65 - int(age), "yıl var")

# mojo araştır - öğren