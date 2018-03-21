x = 0
while x != 'exit':
    x = input("Input integer or 'exit' to exit from program: ")
    if x == 'exit':
        print("Goodbye!")
    else:
        try:
            check_integer = int(x)
        except ValueError:
            print("You haven't input integer!")
            continue
        for i in range(len(x)):
            print(x[i])