from cffi import FFI

ffi = FFI()

#lib = ffi.dlopen('./libsomelib.so')
lib = ffi.dlopen('./somelib.so')
print('Loaded lib {0}'.format(lib))

# Describe the data type and function prototype to cffi.
ffi.cdef('''
        typedef struct {
            int num;
                double dnum;
                } DataPoint;

                DataPoint add_data(const DataPoint* dps, unsigned n);
                ''')

# Create an array of DataPoint structs and initialize it.
dps = ffi.new('DataPoint[]', [(20, 2.2), (30, 3.3), (40, 4.4), (50, 5.5)])

print('Calling add_data via cffi')
# Interesting variation: passing invalid arguments to add_data will trigger
# a cffi type-checking exception.
dout = lib.add_data(dps, 4)
print('dout = {0}, {1}'.format(dout.num, dout.dnum))
