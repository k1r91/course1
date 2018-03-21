import math
import cmath

print("Solve a quadratic equation a*x^2 + b*x + c")
a = input("Input a: ")
b = input("Input b: ")
c = input("Input c: ")
try:
    a = int(a)
    b = int(b)
    c = int(c)
except ValueError:
    print("Coefficients a, b and c must be an integer! Exiting...")
    exit()

is_complex = False
try:
    discriminant = math.sqrt(b**2 - 4*a*c)
except ValueError:
    is_complex = True
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    # print("Equation has no roots.")
    # exit()

r1 = (-b+discriminant) / (2*a)
r2 = (-b-discriminant) / (2*a)

if is_complex:
    print("It has complex roots:")
if r1 == r2:
    print("Root = {}".format(r1))
else:
    print("Root1 = {}, Root2 = {}".format(r1, r2))