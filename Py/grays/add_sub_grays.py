
def dec2bin(dec, n=0):
    a = list(str(bin(dec))[2:])
    if n > len(a):
        a = [0]*(n - len(a)) + a
    return [int(x) for x in a]

# for below len(a) == len(b)
def XOR(a, b, dec=False, n=0):
    r = []
    if dec:
        a = dec2bin(a, n)
        b = dec2bin(b, n)
    for x,y in zip(a,b):
        r.append(x ^ y)
    return r

def OR(a, b, dec=False, n=0):
    r = []
    if dec:
        a = dec2bin(a, n)
        b = dec2bin(b, n)
    for x,y in zip(a,b):
        r.append(x | y)
    return r

def AND(a, b, dec=False, n=0):
    r = []
    if dec:
        a = dec2bin(a, n)
        b = dec2bin(b, n)
    for x,y in zip(a,b):
        r.append(x & y)
    return r

def NEG(a, dec=False, n=0):
    r = []
    if dec:
        a = dec2bin(a, n)
    for x in a:
        r.append(1 if x == 0 else 0)
    return r

# a and b are lists of 1s and 0s, 2 long
def gray_add_2bit(x, y):
    c = y[0] ^ y[1]
    a = x[0] ^ y[1]
    b = x[1] ^ y[0]
    if c:
        tmp = a
        a = b
        b = tmp
    return [a,b]

def gray_subtract_2bit(x, y):
    y = [y[1], y[0]]
    c = y[0] ^ y[1]
    a = x[0] ^ y[1]
    b = x[1] ^ y[0]
    if c:
        tmp = a
        a = b
        b = tmp
    return [a,b]

X = [[0,0],[0,1],[1,1],[1,0]]
Y = [[0,0],[0,1],[1,1],[1,0]]

for x in X:
    row = []
    for y in Y:
        row.append(gray_add_2bit(x,y))
    print(row)

print()

for x in X:
    row = []
    for y in Y:
        row.append(gray_subtract_2bit(x,y))
    print(row)
