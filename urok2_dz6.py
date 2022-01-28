#6
B = []
A = ['название', 'цена', 'количество', 'ед']
print("Введите характеристики для 3 единиц оборудования: ")
x = ''
for i in range(3):
    d = {A[c]:input(A[c]) for c in range(len(A))}
    x = (i+1, d)
    B.append(x)
    x = ''

print(B)

A = ['название', 'цена', 'количество', 'ед']
B = [(1, {'название': 'компьютер', 'цена': '20000', 'количество': '5', 'ед': 'шт.'}),
     (2, {'название': 'принтер', 'цена': '6000', 'количество': '2', 'ед': 'шт.'}),
     (3, {'название': 'сканер', 'цена': '2000', 'количество': '7', 'ед': 'шт.'})]
# print(len(A), len(B))
d = {}
for j in range(4):
    list_for_dict = []
    for i in range(3):
        elBl = B[i]
        count = 0
        for ji in range(len(list_for_dict)):
            if elBl[1][A[j]] == list_for_dict[ji]:
                count = 1
        if count == 0:
            list_for_dict.append(elBl[1][A[j]])
    d[A[j]] = list_for_dict

print(d)
