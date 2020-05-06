try:
    import cPickle as pickle
except ModuleNotFoundError:
    import pickle

from tempfile import mkstemp

class A:
    def __init__(self):
        self.a = "a"

a = A()
b = A()

fd, path = mkstemp()

print(path)

def save_object(obj, filename):
    with open(filename, "wb") as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

def pickled_items(filename):
    with open(filename, "rb") as f:
        while True:
            try:
                yield pickle.load(f)
            except EOFError:
                break

print([a,a,b])
print(set([a,a,b]))
save_object(set([a, a, b]), path)

for items in pickled_items(path):
    for item in items:
        print(item.a)
