import sys
class A:
    def __init__(self):
        self.a = "a"

    def __enter__(self):
        try:
            raise Exception("Oops in __enter__")
        except:
            if self.__exit__(*sys.exc_info()):
                self.enter_ok = False
            else:
                raise
        return self

    def __exit__(self, e_typ, e_val, trcbak):
        print(e_val)
        if e_typ == AssertionError:
            print(e_typ)
        return True

class B:
    def __init__(self):
        self.a = "b"

    def __enter__(self):
        return self

    def __exit__(self, e_typ, e_val, trcbak):
        pass

if __name__=="__main__":
    with A() as a:
        with B() as b:
            assert(True == False)
