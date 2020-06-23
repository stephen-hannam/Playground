import sys

def reverseBits(n):
    result = 0
    for i in range(96):
        result <<= 1
        result |= n & 1
        n >>= 1
    return result

fwd_hex = sys.argv[1]
fwd_int = int(fwd_hex, 16)

rev_int = reverseBits(fwd_int)
rev_hex = hex(rev_int)

print(rev_hex)
