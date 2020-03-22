from cffi import FFI

ffi = FFI()

lib = ffi.dlopen('./hello.so')
print('Loaded lib {0}'.format(lib))

# Describe the data type and function prototype to cffi.
ffi.cdef("int main(int argc, char ** argv);")

# Interesting variation: passing invalid arguments to add_data will trigger
# a cffi type-checking exception.
lib.main(2, ffi.new("char[]", "you".encode('ascii')))
