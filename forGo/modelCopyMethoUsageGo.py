
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '../moveNearReplace'))
sys.path.insert(0, os.path.join(currentFolder, '../navigateTo'))
sys.path.insert(0, os.path.join(currentFolder, '../util'))
sys.path.insert(0, os.path.join(currentFolder, '../makeTestForGo'))
import filer2
        
import navigateToModel
import absRel3
import color
import sys
import os
import re


import sys
import generateTestFileNameForGoTest as g


def generateFuncUsageByLineContentGo(lineContent):

    # get func parts:
    (caller, method, args, returnParams) = g.getGoFuncDeclarationPartsByLineContent(lineContent)
    returnParamsSplitedList = g.splitArgs(returnParams)
    color.red("returnParamsSplitedList")
    print(returnParamsSplitedList)

     # split args
    argsSplitedList = g.splitArgs(args)
    # get vars commas str
    (_, varsCommasStr, _) = g.getVarBlockByStructureListOfNameTypeName(argsSplitedList)    
    # get return params comma string
    (_, returnParamsCommasStr, _) = g.getVarBlockByStructureListOfNameTypeName(returnParamsSplitedList)    

    callerVarName = g.getCallerVarName(caller)


    funcCall = g.innerTestFuncPartGoTestPrepare_callTestableFunc(callerVarName, method, returnParamsCommasStr, varsCommasStr)

    # get var block and add before funcCall
    (varBlock, _, _) = getVarBlock(caller, args, returnParams)

    # func usage total
    funcUsageTotal = "/*{}*/\n{}".format(varBlock, funcCall)
    return funcUsageTotal

def getVarBlock(caller, args, returnParams):
    # split args
    (varBlockInnerArgs, argsVarsCommas, argsVarsList) = g.splitAndFullPrepare(args)
    # split return params
    (varBlockInnerReturnParams, returnParamsVarsCommas, returnParamsList)   = g.splitAndFullPrepare(returnParams)
    returnParamsSplitedList = g.splitArgs(returnParams)
    # generate total var block
    # which consists of:
    #   caller var
    #   inner args vars
    #   return args vars
    varBlockTmpl = """var (
\t{}
{}
{}
        )"""
    varBlock =varBlockTmpl.format(caller, varBlockInnerArgs, varBlockInnerReturnParams)
    print("argsVarsCommas")
    print(argsVarsCommas)
    return (varBlock, argsVarsCommas, returnParamsVarsCommas)
def main_getFuncUsageByFileNameAndPosition(filename, position):
    targetFileContent = filer2.read(filename)
    lineContent = g.getFullLineWhereCursorIs(targetFileContent, position)
    return generateFuncUsageByLineContentGo(lineContent)

