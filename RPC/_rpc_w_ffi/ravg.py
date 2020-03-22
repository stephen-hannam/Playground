from cffi import FFI

ffi = FFI()

lib = ffi.dlopen('./_ravg.so')
print('Loaded lib {0}'.format(lib))

# Describe the data type and function prototype to cffi.
ffi.cdef("int _main(int argc, char * argv[]);")

print('Calling ravg_main via cffi')
# Interesting variation: passing invalid arguments to add_data will trigger
# a cffi type-checking exception.
lib._main(5,[ffi.new("char[]", bytes("localhost", 'ascii')),\
             ffi.new("char[]", bytes("123456", 'ascii')),\
             ffi.new("char[]", bytes("2458", 'ascii')),\
             ffi.new("char[]", bytes("58", 'ascii'))])
