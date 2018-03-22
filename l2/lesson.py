print(1 > 0 == True)

a = 25
b = 'asdfgh'
c = 44
d = [33, 55, 66, 77]
tup = (a ,b ,c, d)
print(tup)
b = 'ASD'
a = 44
d.append(1025)
print(tup)


for i, val in enumerate(tup, 1):
    if type(val) == str:
        val = ''.join([val[0].upper(), val[1:]])  # Capitalize first letter
    print('{}. {}'.format(i, val))