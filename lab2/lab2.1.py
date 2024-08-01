n = int(input("จำนวนที่ต้องการ : "))

for x in range(1, n + 1):
    for y in range(x):
        print("*", end="")
    print()

print("-----------------")

for x in range(n, 0, -1):
    for y in range(x):
        print("*", end="")
    print()

print("-----------------")

for i in range(n):
    print(' ' * (n - i - 1) + '*' * (i * 2 + 1))

print("-----------------")

for i in range(n):
    print(' ' * i + '*' * ((n - i) * 2 - 1))

print("-----------------")

for x in range(1, n + 1):
    for y in range(n - x):
        print(" ", end="")
    for y in range(1, x + 1):
        print("*", end="")
    print()
