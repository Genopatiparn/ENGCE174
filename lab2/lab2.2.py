def print_spaces(n):
    if n > 0:
        print(" ", end=" ")
        print_spaces(n - 1)

def print_stars(n):
    if n > 0:
        print("*", end=" ")
        print_stars(n - 1)

def numpat(n, i=1):
    if i <= n:
        print_stars(i)
        print("")
        numpat(n, i + 1)

def numpatR(n):
    if n > 0:
        print_stars(n)
        print("")
        numpatR(n - 1)

def pyramid(n, i=0):
    if i <= n:
        print(' ' * (n - i) + '* ' * (i))
        pyramid(n, i + 1)

def pyramidR(n, i):
    if i > 0:
        print_spaces(n-i)
        print_stars((2 * i) - 1)
        print("")
        pyramidR(n, i - 1)

def numpatright(n, i=1):
    if i <= n:
        print_spaces(n - i)
        print_stars(i)
        print("")
        numpatright(n, i + 1)


x = int(input('จำนวนที่ต้องการ:'))
numpat(x)
print('-----------------------')
numpatR(x)
print('-----------------------')
pyramid(x)
print('-----------------------')
pyramidR(x,x)
print('-----------------------')
numpatright(x)