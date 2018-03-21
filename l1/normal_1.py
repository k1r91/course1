x = input("Input positive integer: ")

try:
    check = int(x)
    if check < 0:
        print("X must be a positive! Exiting...")
    else:
        max_d = 0
        for i in range(len(x)):
            digit = int(x[i])
            if digit > max_d:
                max_d = digit
        print("Max digit in x is:", max_d)
except ValueError:
    print("X must be a positive integer! Exiting...")