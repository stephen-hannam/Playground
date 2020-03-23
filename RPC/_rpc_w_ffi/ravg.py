from cffi import FFI

ffi = FFI()

lib = ffi.dlopen('./_ravg.so')
print('Loaded lib {0}'.format(lib))

# Describe the data type and function prototype to cffi.
ffi.cdef("int _main(int argc, char * argv[]);")

print('Calling ravg_main via cffi')
# Interesting variation: passing invalid arguments to add_data will trigger
# a cffi type-checking exception.

host = bytes("localhost", 'ascii')
num1 = bytes("12456", 'ascii')
num2 = bytes("1255", 'ascii')
num3 = bytes("126", 'ascii')

print([hex(hos) for hos in host])
print([hex(num) for num in num1])
print([hex(num) for num in num2])
print([hex(num) for num in num3])

name = ffi.new("char[]",bytes("_main", 'ascii'))
host = ffi.new("char[]",host)
num1 = ffi.new("char[]",num1)
num2 = ffi.new("char[]",num2)
num3 = ffi.new("char[]",num3)

print(name)
print(host)
print(num1)
print(num2)
print(num3)

argv = ffi.new("char *[]", [name, host, num1, num2, num3])

ret = lib._main(len(argv), argv)
print(ret)
