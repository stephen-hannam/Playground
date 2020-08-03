on='\x1b(0' # Esc ( 0
off='\x1b(B' # Esc ( B

#print("{0}\x6a{1}".format(on, off))

#print("\x6a".encode())

for i in ["\x6a", "\x6b", "\x6c", "\x6d", "\x6e", "\x71", "\x74", "\x75", "\x76", "\x77", "\x78"]:
    print("{0}: {1}{2}{3}".format(i,on,i,off))
