
def flatten_dict(d):
    def expand(key, value):
        if isinstance(value, dict):
            return [ (key + '.' + k, v) for k, v in flatten_dict(value).items() ]
        else:
            return [ (key, value) ]

    items = [ item for k, v in d.items() for item in expand(k, v) ]

    return dict(items)

def flatten(d, l):
    if type(d) == dict:
        for v in d.values():
            flatten(v, l)
    elif type(d) == list:
        l += d
    else:
        l.append(d)

d = {"a": {"b": {"c":"c"}, "d":"b"}, "e": [1,2,3]}
#print(flatten_dict(d))
l=[]
flatten(d,l)
print(l)

