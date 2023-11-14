# comprehensions
import types

a_list = [1, '4', 9, 'a', 0, 4]
squared_ints = [e**2 for e in a_list if type(e) == types.IntType]
print(squared_ints)

x = [1,2,3,4]

# bu
x_squared = []
for item in x:
    x_squared.append(item * item)
# bunun aynısı
x_squared = [ item * item for item in x]

[x ** 2 for x in range(10)] # bana birden ona kadar olan sayıların karasini tutan liste oluşturdu

res = []
for x in [ 0, 1, 2]:
    for y in [100, 200, 300]:
        res.append(x + y)

res = [x+y for x in [0, 1, 2] for y in [100, 200, 300]]

# [expression for target1 in iterable1 if condition1
#             for target2 in iterable2 if condition2
#             for target3 in iterable3 if condition3 ...]

[x + y for x in 'spam' if x in 'sm' for y in 'SPAM' if y in ('P', 'A')]

#sadece liste değil dict'te oluşturabiliriz

x = [1, 2, 3, 4]
x_squared_dict = {item: item * item for item in x}
print(x_squared_dict)

sentance = 'awzsexdrcftvgybhunjmköl gasvdvhbasjnkmdlş ahshbdjklş'

vowels = 'aeiıoöuü' # sesli harfleri buldu ve cümleden çıkardı
nonvowels = ''.join([l for l in sentance if not l in vowels])
print(nonvowels)

# collection = [ d if condition(d) else modify(d) for d in data_set ]

print(sum([x**3 for x in range(10000)])) # tek satırda 1 den 10 000'e kadar olan sayıların toplamını yazan program

employees = {
    'alice': 100000,
    'bob': 12332,
    'ali mert': 100000000,
    'carol': 1230421,
    'who': 1233
}

gainers = [(k, v) for (k, v) in employees.items() if v > 100000]
print(gainers)

#"lkaskdjakjfşa sdllkF".strip() dediğimizde zaman strip paramatresine ne verirsek onları çıkartıyor boş verirsek boşlukları çıkartıyor

column_names = ['name', 'salary', 'job']
db_rows = [
    ('Alice', 180000, 'data scientist'),
    ('Bob', 99000, 'mid-level manager'),
    ('Frank', 87000, 'CEO'),
    ('Ali Mert', 10000000, 'student')
]

db = [dict(zip(column_names, row)) for row in db_rows]
print(db)

unsorted = [33, 2, 32, 2352, 351, 1, 24123, 0, 414151, 2421, 5314, 6454, 3423, 19]
q = lambda L: q([x for x in L[1:] if x <= L[0]]) + [L[0]] + q([x for x in L if x > L[0]]) if L else []
print(q(unsorted))


# for e in it:
#     func(e)
#
# ikiside aynı işi yapıyor
#
# map(func, it)

def square(x):
    return x**2

squares = map(square, range(10))
print (*squares)

squares = map(lambda x: x**2, range(10)) # lambda anonim fonksiyondur adı yoktur.
print (*squares) # sqares bir obje olarak dönüyor ancak başına yıldız çağırarak tekrar çağırabilir hala getiriyoruz

f = [0,1,1,2,3,5,8,13,21,34,55]
odd_numbers = list(filter(lambda x: x % 2, f)) # filter(Bool, list) olarak çalışıyor
print(odd_numbers)
# [1, 1, 3, 5, 13, 21, 55]
even_numbers = list(filter(lambda x: x % 2 == 0, f))
print(even_numbers)
# [0, 2, 8, 34]
even_numbers = list(filter(lambda x: not (x % 2), f))
print(even_numbers)
# [0, 2, 8, 34]
even_numbers = list(filter(lambda x: x % 2 - 1, f))
print(even_numbers)
# [0, 2, 8, 34]

a, b, *c = "X...Y" # sen ilk ilsini ata kalanları c'ye ata dedik yıldız ortaya gelirse ilk ve sonu ata kalanları ortaya at demiş oluyoruz
print(c)

flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for i in range(len(flavor_list)):
    print(f'{i + 1}: {flavor_list[i]}')
for i, flavor in enumerate(flavor_list):
    print(f'{i + 1}: {flavor}')
for i, flavor in enumerate(flavor_list, 1):
    print(f'{i}: {flavor}')