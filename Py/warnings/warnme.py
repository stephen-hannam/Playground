import warnings

def fxn():
    warnings.warn("deprecated", DeprecationWarning)

#with warnings.catch_warnings(record=True) as w:
#    # Cause all warnings to always be triggered.
#    warnings.simplefilter("always")
#    # Trigger a warning.
#    fxn()
#    # Verify some things
#    assert len(w) == 1
#    assert issubclass(w[-1].category, DeprecationWarning)
#    assert "deprecated" in str(w[-1].message)
#    print(w[0].message)

warnings.warn("hello", UserWarning)
