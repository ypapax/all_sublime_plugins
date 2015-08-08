import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + '/goodPath')
import getFutherFolder_model
        
import sys
import color
    
import re
def filename(filepath):
    """justfilename"""
    return filepath.split('/')[-1].split('.')[0]
    

def folder(filepath):
    """folderAbsWithoutFileName"""
    parts = filepath.split('/')
    parts = parts[:-1]
    return str.join('/',parts)



def clearRel(stringWithRel):
    rel = stringWithRel


def gotExtension(path):
    fileName = os.path.basename(path)
    return any(i for i in fileName if i == '.')


def Abs(absolute1, relative):
    print("absolute", absolute1)
    print("relative", relative)
    absoluteResult = os.path.normpath(os.path.join(os.path.dirname(absolute1), relative))
    return absoluteResult

def Ext(filename):
    return filename.split('.')[-1]

def AbsAddExtension(absolute1, relative):
    default_ext = '.iced'
    ext = Ext(absolute1)
    if not ext:
        ext = default_ext
    else:
        ext = '.'+ext    
    rel = Abs(absolute1, relative)
    if not gotExtension(relative):
        rel += ext # default extension
    return rel


def Rel(absSource, absTarget):
    print("absSource", absSource)
    print("absTarget", absTarget)
    pathSource = os.path.dirname(absSource)
    pathTarget = os.path.dirname(absTarget)
    rel = os.path.relpath(absTarget, absSource)#[3:]
    if (pathTarget != pathSource):
        rel = rel[3:]
    else:
        rel = rel[1:]
    
    if(len(rel) == 0):
        rel = './'+os.path.basename (absTarget)
    elif (rel[0] != '.'):
        rel = './'+rel
            
    print('result rel', rel)
    return rel

def RelAndCutIfNodeModules(absSource, absTarget):
    relative = Rel(absSource, absTarget)

    if not filePathInsideCurrentProject(absSource, absTarget):
        return re.sub('^[\.\.\/]+', '', relative) # replace starting points like '../../../pages' to 'pages'
    else:    
        return IsNodeModulesRelPath(relative)
    # if relative

def IsNodeModulesRelPath(relPath):
    # ../../../../node_modules/
    if "../node_modules/" in relPath:
        return re.sub('[\.\./]+node_modules/', '', relPath) 
     
    else:
        return relPath    
def filePathInsideCurrentProject(sourseFilePath, targetFilePath):
    # get project fatherFolder of sourseFilePath (where package.json lives)
    sourceFatherFolder = getFutherFolder_model.get(sourseFilePath)
    # return true if fatherFolder is inside targetFilePath        
    return targetFilePath.startswith (sourceFatherFolder)
def RelToRel(abs1, abs2, rel1):
    absOfRequiredModuleTarget = Abs(abs1, rel1)
    print ("absOfRequiredModuleTarget", absOfRequiredModuleTarget)
    print ("abs2", abs2)
    rel2 = Rel (abs2, absOfRequiredModuleTarget)
    return rel2