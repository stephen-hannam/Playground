from tempfile import mkstemp

fd, path = mkstemp()

# use a context manager to open (and close) file descriptor fd (which points to path)
with open(fd, 'w') as f:
    f.write('TEST\n')

print(path)
