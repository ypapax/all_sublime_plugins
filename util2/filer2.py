
import sys
import absRel3
        
import os
import ast
import sys
import color
def read(path):
    color.blue("Reading "+path)
    content = ""
    with open(path, 'r', encoding='utf-8') as content_file:
        content = content_file.read()
        
    # print(content)
    return content  

def readToObj(filename):
    data = None
    with open(filename) as fp:
        data = [ast.literal_eval(line) for line in fp if line.strip()]
    result = data[0] if len(data) else None
    return result

def write(path, content):
    content = str(content)
    print("Writing file "+path+'---------------------------------------------------+++++++++++++++++++++++++++++++++++++++++')
    text_file = open(path, "w", encoding='utf-8')
    
    text_file.write(content)
    text_file.close()
    
    print(content)

def writeEvenIfNoDir(path, content):
    directory = absRel3.folder (path)
    if not os.path.exists(directory):
        os.makedirs(directory)  
    write (path, content)      


