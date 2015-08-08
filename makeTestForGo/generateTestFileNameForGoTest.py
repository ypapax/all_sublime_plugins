import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/navigateTo')
import navigateToModel
import absRel3
import color
import os
import re
import filer2


def getPackageName(fileContent):
    match = re.search(r"package (.*)",fileContent).groups()[0]
    color.red("match")
    print(match)
    return match


def createFileNameForGoTest(testFolder, testMethodName): # but it dont create file, just fileName
    i = 0
    while(True):
        if i == 0:
            iStr = ''
        else:
            iStr = str(i)
        testFileName = "{0}{1}_test.go".format(testMethodName.strip(), iStr)
        testFile = os.path.join(testFolder, testFileName)
        exists = os.path.isfile(testFile)

        if not exists: break
        i = i + 1

    return (testFile, i)


def createFromPosition(filename, position):
    return writeTestFileBySourceFileTargetAndPosition(filename, position)

def writeTestFileBySourceFileTargetAndPosition(targetFileName, position):
    ### read target file name ###
    targetFileContent = filer2.read(targetFileName)
    ### generate test file content by targetFileContent and position ###
    testFileContent = createTestFileContentBySourceFileTargetAndPosition(targetFileContent, position)
    color.red("testFileContent")
    print(testFileContent)

    methodName = getMethodNameByFileContentAndPosition(targetFileContent, position)
    return create(targetFileName, methodName, testFileContent)

def getMethodNameByFileContentAndPosition(targetFileContent, position):
    lineContent = getFullLineWhereCursorIs(targetFileContent, position)
    (_, methodName, _, _) = getGoFuncDeclarationPartsByLineContent(lineContent)
    return methodName



def createTestFileContentBySourceFileTargetAndPosition(targetFileContent, position):
    ### get line content by targetFileContent and position ###
    lineContent = getFullLineWhereCursorIs(targetFileContent, position)
    ### get all main parts of current line ###
    (caller, methodName, args, returnParams) = getGoFuncDeclarationPartsByLineContent(lineContent)
    ### get package name ###
    packageName = getPackageName(targetFileContent)
    ### get test method name ###
    testMethodName = getTestMethodName(methodName)
    ### generate test file content ###
    testFileContent = generateTestTextByGoFuncDeclarationParts(packageName, testMethodName, caller, methodName, args, returnParams)
    return testFileContent


def createTestFileContent(packageName, testMethodName, methodName):
    importMy = '"my"\n\t'
    testCallerObj = "my."
    if packageName == "my":
        importMy = ""
        testCallerObj = ""


    template = """package {0}
import (
\t{3}"testing"
)

func {1}(t *testing.T) {{
    actual := {2}()
    var expected interface{{}}
    expectedJson := ``
    {4}FromJson(expectedJson, &expected)
    {4}Test(actual, expected, t)
}}"""
        

    testText = template.format(packageName, testMethodName, methodName, importMy, testCallerObj)

    return testText

def getTestMethodName(methodName):
    testMethodName = "Test_{0}".format(methodName)
    return testMethodName


# writes "fileText" to test file by source "filename" and "methodName"
def create(filename, methodName, testFileContent):
    dirName = absRel3.folder(filename)  
    testFolder = os.path.join(dirName)
    if not os.path.exists(testFolder): os.makedirs(testFolder)

    testMethodName = getTestMethodName(methodName)

    (testFile, i) = createFileNameForGoTest(testFolder, testMethodName)

    

    justFileName = absRel3.filename(filename)


    
    # testText = createTestFileContent(packageName, testMethodName, methodName)
    filer2.write(testFile, testFileContent)
    return testFile


# func LocalsByYoutubeId(ds *mon.DataStore, youtubeId string) *YoutubeIdLocals {
# must return "ds *mon.DataStore, youtubeId string"
def findArgsStrByFileLineGoForTest(fileLine):
    return ""


def getFullLineWhereCursorIs(fileText, cursorPosition):
    # return navigateToModel.getSubstr(fileText, cursorPosition, ['\n'])
    lineNumber = getLineNumberByTextAndCursorPosition(fileText, cursorPosition)
    lines = fileText.splitlines()    
    lineContent = lines[lineNumber-1]
    return lineContent
def getLineNumberByTextAndCursorPosition(fileText, cursorPosition):
    textFromStartToCursor = fileText[0:cursorPosition]

    print("textFromStartToCursor")
    print(textFromStartToCursor)
    howManyNextLineCharsUntilCursor = textFromStartToCursor.count('\n')
    lineNumber=howManyNextLineCharsUntilCursor + 1
    return lineNumber

# func (caller *CallerType) LocalsByYoutubeId(ds *mon.DataStore, youtubeId string) (res1 *YoutubeIdLocals, res2 int) {
def getGoFuncDeclarationPartsByLineContent(lineContent):
    caller = getCallerByLineContentGo(lineContent)
    method = getMethodNameByLineContentGo(lineContent)
    args = getArgsByLineContentGo(lineContent)
    returnParams = getReturnParamsByLineContentGo(lineContent)
    return (caller, method, args, returnParams)

def getCallerByLineContentGo(lineContent):
    regex = re.compile(r"func \((.+?)\)")
    m = regex.findall(lineContent)
    if m:
        lastGroup = m[-1]
        result = lastGroup
        return result
    else:
        return ""

# func (caller *CallerType) LocalsByYoutubeId(ds *mon.DataStore, youtubeId string) (res1 *YoutubeIdLocals, res2 int) {
# must return LocalsByYoutubeId
def getMethodNameByLineContentGo(lineContent):
    regex = re.compile(r"(\S+?)\(")
    m = regex.findall(lineContent)
    if m:
        lastGroup = m[-1]
        result = lastGroup
        return result
    else:
        return ""

# func (caller *CallerType) LocalsByYoutubeId(ds *mon.DataStore, youtubeId string) (res1 *YoutubeIdLocals, res2 int) {
# must return "ds *mon.DataStore, youtubeId string"
def getArgsByLineContentGo(lineContent):
    color.red("lineContent")
    print(lineContent)
    regex = re.compile(r"\S\(([^\(]+)\)")
    m = regex.findall(lineContent)
    if m:
        lastGroup = m[-1]
        result = lastGroup
        return result
    else:
        return ""

def removeMethodNameCallerAndEmptyBrackets(lineContent):
    methodName = getMethodNameByLineContentGo(lineContent)
    caller = getCallerByLineContentGo(lineContent)
    # lineContentWithoutMethodName = lineContent.replace(methodName, "")
    return removeEmptyBrackets(
        lineContent
            .replace(caller, "")
    )
    # lineContentWithoutMethodNameAndColler = lineContentWithoutMethodName.
    # lineContentWithoutMethodNameAndCollerAndEmptyBrackets = (lineContentWithoutMethodNameAndColler)
    # return lineContentWithoutMethodNameAndCollerAndEmptyBrackets

def removeEmptyBrackets(lineContent):
    return lineContent.replace(" ()", " ")

def getReturnParamsByLineContentGo(lineContent):
    color.red("lineContent")
    print(lineContent)
    regex = re.compile(r"\s\(([^\(\)]+)\) {$")

    m = regex.findall(lineContent)
    if m:
        lastGroup = m[-1]
        result = lastGroup
        return result
    else:
        # # second chanse to find return SINGLE "return type" like
        # # func Func() int {}
        # # should return "int"
        # regex = re.compile(r"(\S+?) {$")
        # m = regex.findall(result)
        # if m:
        #     lastGroup = m[-1]
        #     result = lastGroup
        #     return result

        return ""

def getCallerVarName(caller):
    if len(caller) > 0:
        callerParts = splitArgs(caller)
        callerVarName = callerParts[0]['var'] 
    else:
        callerVarName = ""
    return callerVarName

def generateTestTextByGoFuncDeclarationParts(packageName, testMethodName, caller, methodName, args, returnParams):
    ### get var block and its sub parts ###
    varBlock, argVarCommas, returnParamsVarCommas = getVarBlockGoTest(caller, args, returnParams)
    ### import "my" part ###
    importMy = '"my"\n\t'

    testCallerObj = "my."
    if packageName == "my":
        importMy = ""
        testCallerObj = ""
    ### generate part before func() in test ###    
    beforeFuncPart = """package {0}
import (
    {1}"testing"
)
""".format(packageName, importMy)
    # split return params
    returnParamsSplitedList = splitArgs(returnParams)
    # split args
    argsSplitedList = splitArgs(args)
    # get vars commas str
    (_, varsCommasStr, _) = getVarBlockByStructureListOfNameTypeName(argsSplitedList)    
    # get return params comma string
    (_, returnParamsCommasStr, _) = getVarBlockByStructureListOfNameTypeName(returnParamsSplitedList)    
    # get caller var name
    callerVarName = getCallerVarName(caller)
    ### generate call func part ###
    funcCallPart = innerTestFuncPartGoTestPrepare_callTestableFunc(callerVarName, methodName, returnParamsCommasStr, varsCommasStr)


    actualAndExpectedPart = innerBlockExpectedAndActualCheckForAllReturnParams(returnParamsSplitedList)

    template = """{0}
func {1}(t *testing.T) {{
    {4}
    {2}
    {3}
}}"""
        

    testText = template.format(beforeFuncPart, testMethodName, funcCallPart, actualAndExpectedPart, varBlock)
    return testText
def innerTestFuncPartGoTestPrepare(methodName, returnArgsCommaStr, varsCommasStr):
    callFunc = innerTestFuncPartGoTestPrepare_callTestableFunc(methodName, returnArgsCommaStr, varsCommasStr)
    return """{0}
    var expected interface{{}}
    expectedJson := ``
    {4}FromJson(expectedJson, &expected)
    {4}Test(actual, expected, t)""".format(callFunc, returnArgsCommaStr, varsCommasStr)
def innerTestFuncPartGoTestPrepare_callTestableFunc(caller, methodName, returnArgsCommaStr, varsCommasStr):
    leftPart = ""
    if len(returnArgsCommaStr) > 0:
        leftPart = """{0} = """.format(returnArgsCommaStr)
    if len(caller) > 0:
        caller = caller + "."
    return """{0}{3}{1}({2})""".format(leftPart, methodName, varsCommasStr, caller)
def innerTestFuncPartGoTestPrepare_prepareOneExpectedComparison(returnVarTypeModel):
    (varName, varType) = getVarNameAndTypeByStructure(returnVarTypeModel)
    varNameExpected = paramNameAddExpected(varName)
    return """\texpectedJson_{1} := ``
\tmy.FromJson(expectedJson_{1}, &{2})
\tmy.Test({1}, {2}, t)""".format(varType, varName, varNameExpected)

def innerBlockExpectedAndActualCheckForAllReturnParams(returnVarTypeModelList):
    totalInnerBlockActualAndAssertComparison = ""
    for returnVarTypeModel in returnVarTypeModelList:
        totalInnerBlockActualAndAssertComparison += "\n" + innerTestFuncPartGoTestPrepare_prepareOneExpectedComparison(returnVarTypeModel)
    return totalInnerBlockActualAndAssertComparison

def getVarNameAndTypeByStructure(varTypeStructure):
    return (varTypeStructure["var"], varTypeStructure["varType"])




def getVarBlockGoTest(caller, args, returnParams):
    # split args
    (varBlockInnerArgs, argsVarsCommas, argsVarsList) = splitAndFullPrepare(args)
    # split return params
    (varBlockInnerReturnParams, returnParamsVarsCommas, returnParamsList)   = splitAndFullPrepare(returnParams)
    returnParamsSplitedList = splitArgs(returnParams)
    # get expected vars block
    (expectedVarsBlock, _, _) = splitAndFullPrepareExpectedVarBlock(returnParamsSplitedList)
    # generate total var block
    # which consists of:
    #   caller var
    #   inner args vars
    #   return args vars
    #   expected vars
    varBlockTmpl = """var (
\t{}
{}
{}
{}
        )"""
    varBlock =varBlockTmpl.format(caller, varBlockInnerArgs, varBlockInnerReturnParams, expectedVarsBlock)
    print("argsVarsCommas")
    print(argsVarsCommas)
    return (varBlock, argsVarsCommas, returnParamsVarsCommas)
def splitArgs(commaStringArgs):
    commaStringArgs = commaStringArgs.strip()
    if len(commaStringArgs)==0:
        return []
    else:
        color.red("commaStringArgs")
        print(commaStringArgs)
        ### comma split - split for different args###
        args = commaStringArgs.split(",")
        print("args")
        print(args)
        varTypeStructureList = []
        ### reversing for args like (arg1, arg2 string) - to get first args with type ###
        argsReversed = reversed(args)
        for arg in argsReversed:
            arg = arg.strip()
            print("arg")
            print(arg)
            ### space split - split for arg name and type ###
            argParts = arg.split(" ")
            color.red("argParts")
            print(argParts)
            ### first - it is var name, second = var type ###
            thereIsType = len(argParts)==2
            if thereIsType:
                (var, varType) = argParts
                lastOkType = varType
            else:
                var = argParts[0]
                varType = lastOkType
            varTypeStructure=generateVarTypeStructure(var, varType)
            varTypeStructureList.append(varTypeStructure)
        ### reverse back ###
        return varTypeStructureList[::-1]
def generateVarTypeStructure(var, varType):
    return {"var": var, "varType": varType}

def splitedArgPrepare(splitedArg):
    var = splitedArg["var"]
    varType = splitedArg["varType"]
    return ("{} {}".format(var, varType), var, varType)
def splitAndFullPrepare(argsCommaString):
    argsSplitedList = splitArgs(argsCommaString)
    print("argsSplitedList")
    print(argsSplitedList)
   
    return getVarBlockByStructureListOfNameTypeName(argsSplitedList)
def getVarBlockByStructureListOfNameTypeName(argsSplitedList):
    varNames = []
    varBlockInner = ""
    for splitedArg in argsSplitedList:
        forVarBlockInner, var, varType = splitedArgPrepare(splitedArg)
        varNames.append(var)
        varBlockInner += "\n\t" + forVarBlockInner
        # varNameStructureList.append("var": )
    varNamesCommas = ','.join(varNames)
    return varBlockInner, varNamesCommas, varNames

def splitAndFullPrepareExpectedVarBlock(argsSplitedListForReturnParams):
    expectedStructureList = convertStructureListToExpected(argsSplitedListForReturnParams)
    return getVarBlockByStructureListOfNameTypeName(expectedStructureList)
def convertStructureListToExpected(structureList):
    structureListExpected = []
    for item in structureList:
        name, typeName = getVarNameAndTypeByStructure(item)   
        name = paramNameAddExpected(name)     
        structureListExpected.append(generateVarTypeStructure(name, typeName))
    return structureListExpected
def paramNameAddExpected(paramName):
    return paramName + "_expected"





