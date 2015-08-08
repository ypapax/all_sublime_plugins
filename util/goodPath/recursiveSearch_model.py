import os, fnmatch

# def listChildren(self):
#   yield self
#   for child in self.children:
#     yield from child.listChildren()

def find_files(directory, pattern):
    gotExtension = any(i for i in pattern if i == '.')
    if not gotExtension:
        pattern = pattern + '.*'

    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                # yield filename
                return filename

import os.path                
def getAllFiles(path):   
    fileName = os.path.basename(path)
    if(any(i for i in fileName if i == '.')):
        path = os.path.dirname(path)

    fileNames = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in [f for f in filenames]:
            fileNames.append( os.path.join(dirpath, filename))
    return fileNames        
