import os

import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '../util'))
import absRel3 as absRel
import filer2 as filer
import color
import re

def filename2Total(filename, obj, method):
    if not obj:
        return filename
    else:
        return filename2(filename, obj)

def filename2(filename, obj):
   
    data = filer.read(filename)

    
    color.red('obj')
    print(repr(obj))
    
    regex =  '(\S+) as '+obj
    
    color.red('regex')
    print(repr(regex))
        

    m = re.findall (regex, data)
    match = len(m)
    if match:
        obj = m[0]
    
    # folder = os.path.join(os.path.dirname(filename), obj+ '.py')    
    rel2 = './'+obj
    filename2 = absRel.AbsAddExtension(filename, rel2)
    if not os.path.isfile(filename2):
        regex2 = "sys.path.insert\(0, '(.+)'\)"
        matches = re.findall(regex2, data)
        for m in matches:
            filename2 = os.path.join(m, obj+ '.py')
            if os.path.isfile(filename2):
                break
    if not os.path.isfile(filename2):
        filename2 = filename                
    return filename2
