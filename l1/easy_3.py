age = input("Input your age please: ")

try:
    age = int(age)
    if age >= 18:
        print("Access allowed!")
    else:
        print("Access denied!")
except ValueError:
    print("Age is a digit! Exiting...")
