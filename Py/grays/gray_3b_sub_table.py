def dec2gray(b, n=0):
    """Convert Binary to Gray codeword and return it."""
    #b = int(b, 2) # convert to int
    b ^= (b >> 1)
    a = list(str(bin(b))[2:])
    if n > len(a):
        a = [0]*(n - len(a)) + a
    # bin(n) returns n's binary representation with a '0b' prefixed
    # the slice operation is to remove the prefix
    return [int(x) for x in a]

#BASE=4
#
#X = range(2**BASE)
#Y = range(2**BASE)
#
#for x in X:
#    row = []
#    for y in Y:
#        a = (x - y) % 2**BASE
#        row.append(dec2gray(a, BASE))
#    print(row)
#    print()

print(dec2gray(10,4))
print(dec2gray(3,4))
print(dec2gray(7,4))
