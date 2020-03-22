from cffi import FFI

ffi = FFI()

lib = ffi.dlopen('./ravg.so')
print('Loaded lib {0}'.format(lib))

# Describe the data type and function prototype to cffi.
ffi.cdef("int main(int argc, char * argv[]);")

print('Calling ravg_main via cffi')
# Interesting variation: passing invalid arguments to add_data will trigger
# a cffi type-checking exception.
lib.main(4,[ffi.new("char[]", "localhost"),\
            ffi.new("char[]", "123456"),\
            ffi.new("char[]", "2458"),\
            ffi.new("char[]", "58")])
