from cffi import FFI

ffi = FFI()

lib = ffi.dlopen('./hello.so')
print('Loaded lib {0}'.format(lib))

# Describe the data type and function prototype to cffi.
ffi.cdef("""
int _main(int argc, char * argv[]);
""")

# Interesting variation: passing invalid arguments to add_data will trigger
# a cffi type-checking exception.

a = [ffi.new("char[]", bytes('./hello.so', 'ascii')),\
     ffi.new("char[]", bytes('you', 'ascii'))]
a = ffi.new("char *[]", a)
#print(a)
#print(ffi.unpack(b[0], 4))
#print(dir(a))
#print(dir(b))
ret = lib._main(2, a)
print(ret)
