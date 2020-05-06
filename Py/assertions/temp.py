#!/usr/bin/python

class A:
    def __init__(self):
        self.msg = "colder than absolute zero"

def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0), (A().msg, 0)
   return ((Temperature-273)*1.8)+32

print(KelvinToFahrenheit(273))
print(int(KelvinToFahrenheit(505.78)))
#print(KelvinToFahrenheit(-5))

try:
    KelvinToFahrenheit(-5)
except Exception as e:
    print(e)
