import ast
import sys
import color
import codecs
def read(path):
    f = codecs.open(path, "r")
    return f.read() 

def write(path, content):
    content = str(content)
    print("Writing file "+path+'---------------------------------------------------+++++++++++++++++++++++++++++++++++++++++')
    text_file = codecs.open(path,'w')
    
    text_file.write(content)
    text_file.close()
    
    print(content)


