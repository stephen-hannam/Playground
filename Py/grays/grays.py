# Python3 program to generate n-bit Gray codes
import math as mt

def rl(l,n):
    return l[-n:] + l[:-n]

def rr(l,n):
    return l[n:] + l[:n]

# This function generates all n bit Gray
# codes and prints the generated codes
def generateGrayarr(n):

    # base case
    if (n <= 0):
        return

    # 'arr' will store all generated codes
    arr = list()

    # start with one-bit pattern
    arr.append("0")
    arr.append("1")

    # Every iteration of this loop generates
    # 2*i codes from previously generated i codes.
    i = 2
    j = 0
    while(True):

        if i >= 1 << n:
            break

        # Enter the prviously generated codes
        # again in arr[] in reverse order.
        # Nor arr[] has double number of codes.
        for j in range(i - 1, -1, -1):
            arr.append(arr[j])

        # append 0 to the first half
        for j in range(i):
            arr[j] = "0" + arr[j]

        # append 1 to the second half
        for j in range(i, 2 * i):
            arr[j] = "1" + arr[j]
        i = i << 1

    return arr

finl = []

finl.append(generateGrayarr(4))
finl.append(rr(generateGrayarr(4),1))
finl.append(rr(generateGrayarr(4),2))
finl.append(rr(generateGrayarr(4),3))

for l0,l1,l2,l3 in zip(finl[0],finl[1],finl[2],finl[3]):
    print("{0} {1} {2} {3}".format(l0,l1,l2,l3))


