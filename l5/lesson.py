import sys
import os
import mod3
from mod2 import *
from mod1 import *


x = 0
y = 0
for x in range(2), y in range(3):
    print('x =', x, 'y =', y)

# print(sys.path)
# mod1.go()
# mod2.go()
# mod3.mod3()
# implicit error
go()

for f in os.listdir('.'):
    if os.path.isfile(f):
        print(f, ' - file')

for f in os.scandir('.'):
    if f.is_file():
        print(f.path)

for dir_file in os.walk('../'):
    print(dir_file)

if len(sys.argv) > 1:
    print('Program arguments: ', sys.argv)
try:
    x = 13 / 0
    print(os.listdir('dir1'))
except ZeroDivisionError as e:
    print('Error: ', e)
    sys.exit()
else:
    print('Else exception handle block')
finally:
    print('Finally block')
    print(sys.argv)
print('after exception')

