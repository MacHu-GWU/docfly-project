from __future__ import print_function
from docfly import Docfly
import shutil
 
try:
    shutil.rmtree(r"source\toppackage")
except Exception as e:
    print(e)
     
docfly = Docfly("toppackage", dst="source")
docfly.fly()
