import random
a = input("ведите нижнюю границу: ")
b = input("Введите верхнюю границу: ")

if a.isdigit() or b.isdigit():
    l = random.randrange(int(a), int(b))
    print(l)
else:
    m = random.randrange(ord(a), ord(b))
    print(chr(m))
