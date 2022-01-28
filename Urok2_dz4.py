var = input("Введите текст с пробелами:  ")
word = []
number = 1
for element in range(var.count(' ') + 1):
    word = var.split()
    if len(str(word)) <= 10:
        print(f" {number} {word [element]}")
        number += 1
    else:
        print(f" {number} {word [element] [0:10]}")
        number += 1


