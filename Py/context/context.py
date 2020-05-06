import sys
class Context(object):
    def __init__(self):
        self.enter_ok = True

    def __enter__(self):
        try:
            pass
            #raise Exception("Oops in __enter__")
        except:
            if self.__exit__(*sys.exc_info()):
                self.enter_ok = False
            else:
                raise
        return self

    def __exit__(self, e_typ, e_val, trcbak):
        print("Now this runs twice")
        return True


with Context() as c:
    if c.enter_ok:
        print("Only runs if enter succeeded")

print("Execution continues")

