a = float(input('Input a: '))
b = float(input('Input b: '))
c = float(input('Input c: '))

D = b ** 2 - 4 * a * c
print(D)

if D > 0:
    x1 = (-b + D * 0.5) / (2 * a)
    x2 = (-b - D * 0.5) / (2 * a)
    print(f"x1={x1}, x2={x2}")
elif D == 0:
    x1 = (-b + D * 0.5) / 2 * a
    print(f"x1={x1}")
else:
    print("The equation has no roots")