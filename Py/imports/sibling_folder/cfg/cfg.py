from os import path, chdir
import sys
currdir = path.dirname(path.realpath(path.abspath(__file__)))
print(path.join(currdir, "../../imp_folder"))
sys.path.append(path.join(currdir, "../../imp_folder"))

#from pyfile2 import *
