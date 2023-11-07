a = []
a = [0,1,2]
a = ['aa', 'bbbbbbb']
a = [0, 1, 'aaa', [0, 'bbb']]
print(a[3][0])

my_list = ['aa','bbb']

list1 = my_list # orjinalini list 1'e atadık
list2 = my_list[:] # bir kopyasını oluşturduk

L = [1, 2, 3]
for element in L:
    print(element)

L.append("I am a string")
for element in L:
    print(element)

L1 = [1, 2, 3]
L2 = [0, 4, 8, 10]

print(L1 + L2)
print(L1 * 2)

L2.sort() # sıralıyor
L2.reverse() # tersine çeviriyor

L1.append(4) # sonuna 4 ekliyor
L1.pop() # sonuncuyu çıkartıyor
L1.insert(0, 0) # 0. indexe 0'ı ekliyor
L1.pop(0) # 0. indexi çıkardı
L1 = [0, 1, "aa", "abc"]
L1.remove("aa") # aa'yı bulup siliyor
del L1[2:] # 2. indexten sonrasını sildi
# python set komutu çalış
L1 = ['A', 'a', 'a', 'b', 'c', 'a', 'B']
print(L1.count('a')) # 3

def remove_dublicates(values):
    output = []
    seen = set()
    for value in values:
        if value not in seen:
            output.append(value)
            seen.add(value)
    
    return output

values = [5,5,1,1,2,3,4,4,5]

setvalue = set(values)
resault = list(setvalue)

print(resault)

print(set("aaa aaa a3aa aabaaaa aaa aaac aa aa".split())) # boşluğa göre ayırıp aynı olanları siliyor

a = [1, 2, 3, 4]
b = a

b[1] = 12312412
print(a) # a'yıda değiştirdik

eng2spn = dict()

eng2spn['one'] = 'uno'
eng2spn['two'] = 'duo'

len(eng2spn)

vals = eng2spn.values() # vals bir liste olarak oluştu içinde eng2spn içinde bulunan cevaplar var
kys = eng2spn.keys() # kys içinde eng2spn key'lerini tutyor
itms = eng2spn.items() # tuple olarak ikili ikili key-value olarak döndü

x = {0: 'zero', 1: 'one'}
y = x.copy()

z = {1: 'one', 2: 'two'}
x = {0: 'Zero', 1: 'One'}

x.update(z) # x'i z'ye göre update et demek
print(x)

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1

    return d


def reverse_lookup(d, v): # dictionary ve value'yu vermek zorundayız 
    for k in d:
        if d[k] == v:
            return k
    raise ValueError

# value yerine lambda ile fonksiyonda yazılabilir

name = [ 'deniz' ]
color = [ 'mavi' ]

d = dict(zip(name, color)) # ikiside aynı boyutlu ise onları birleştirdi ve dict yaptı

#tuple
t = 'a', 'b', 'c'
t = ('a', 'b', 'c')
t1 = 'a', 
t = tuple('string')
print(t[:2])
# tuple değiştirilemez

#tuple değil
t2 = ('a')