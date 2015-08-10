import inspect
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '../workflow'))
sys.path.insert(0, os.path.join(currentFolder, '../moveNearReplace'))
sys.path.insert(0, os.path.join(currentFolder, '../util'))
sys.path.insert(0, os.path.join(currentFolder, '../navigateTo'))
import iterationsClass as ic
import re
import absRel3
from os import walk
import color
import filer2
import navigateToModel
# i = None
class FindUsagesModel:
    def __init__(self, dataFolder = os.path.join(currentFolder, 'data')):
        iterations = ic.Iterations()
        iterations.dataFolder = dataFolder
        self.i = iterations
    # def loadIterations(dataFolder = "/Users/maks/Library/Application Support/Sublime Text 3/Packages/findUsages/data"):
    #     i = ic.Iterations()             
    #     i.dataFolder = dataFolder
    #     return i

    def command(self, commandName, *arg):
        method = getattr(self, commandName)
        args = inspect.getargspec(method).args
        argsLen = len(args)
        if arg and argsLen >= 2:
            return method(*arg)
        else:
            return method()


    def next(self, filename=None, position=None):
        # i = loadIterations()
        current = self.i.next()
        
        status = self.i.status()
        current += (status,)
        return current


            
    def find(self, filename, position):

        text = filer2.read(filename)
        [obj, method] = navigateToModel.getObject(text, position)

        

        mypath = absRel3.folder(filename)
        
        targetFiles = []
        for (dirpath, dirnames, filenames) in walk(mypath):

            targetFiles.extend([ os.path.join(dirpath, f) for f in filenames if absRel3.Ext(f) == 'py'])

        regex = "{}.\(".format(method)
        regex = re.compile(regex)       
        
        returnList = []     
        for f in targetFiles:
            # text = filer2.read(f)
            positions = navigateToModel.getPositions(f, regex)      
            if positions:
                returnList.extend([(f, p) for p in positions])

        
        self.i.setAll(returnList)



        if returnList:
            current = returnList[-1]
            (f,p) = current
            self.i.currentSet("{0}{1}".format(f,p))
            
            count = len(returnList)
            
            status = "{0} of {1}".format(count, count)
            # current.insert(2, status)
            current += (status,)
        else:
            status = "no found"
            current = None  
        return current  

