name = input("Введите имя: ")
print("Привет", name)
print("Стороны:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a + b > c and a + c > b and b + c > a:
    print("treugolnic")
else:
    print("kate")