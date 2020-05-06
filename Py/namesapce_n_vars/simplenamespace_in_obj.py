from types import SimpleNamespace
from json import load
from os.path import isfile

def dict_to_sns(d):
    return SimpleNamespace(**d)

from functools import singledispatch
from types import SimpleNamespace

@singledispatch
def wrap_namespace(ob):
    return ob

@wrap_namespace.register(dict)
def _wrap_dict(ob):
    return SimpleNamespace(**{k: wrap_namespace(v) for k, v in ob.items()})

class A:
    def __init__(self, cfg_path):
        ## using object_hook in json.load
        #with open(cfg_path) as fp:
        #    cfg = load(fp, object_hook=dict_to_sns)
        #[setattr(self, k, v) for k,v in cfg.__dict__.items()]
        with open(cfg_path) as fp:
            cfg = wrap_namespace(load(fp))
        [setattr(self, k, v) for k,v in cfg.__dict__.items()]
        d = {"b": {"c":{"d":"d"}}}
        sns = wrap_namespace(d)
        [setattr(self, k, v) for k,v in sns.__dict__.items()]

#a = A("./cfg.json")
#print(type(a.a))
#print(a.b)
#setattr(getattr(a, "b"), "m", "n")
#print(a.b)
#print(a.b.m)
#print(a.b.c)
#d = {}
#if not isfile(str(d)):
#    print("cool")

class A:
    def __init__(self):
            self.a = "a"

a = A()
b = SimpleNamespace(**{})
setattr(b,"a",a)
print(b.a.a)
