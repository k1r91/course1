a = input("Введите а: ")
b = input("Введите b: ")

a, b = b, a

print("a = ", a, " b = ", b)

z = b
b = a
a = z

print("a = ", a, " b = ", b)