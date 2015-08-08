import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/makeTest')
import color
import assertMy
import generateTestFileNameForGoTest

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		targetFileContent = """package main

func absByRel(relFilePath, currentFolderPwd string) (absPath string) {

}

func main() {
	targetFileOrFolderAbsOrRel, _ := my.GetArgBashTerminal(1)
}
"""
		position = 22
		result = generateTestFileNameForGoTest.createTestFileContentBySourceFileTargetAndPosition(targetFileContent, position)
		expected = """package main
import (
    "my"
	"testing"
)

func Test_absByRel(t *testing.T) {
    var (
	

	relFilePath string
	currentFolderPwd string

	absPath string

	absPath_expected string
        )
    absPath = absByRel(relFilePath,currentFolderPwd)
    
	expectedJson_absPath := ``
	my.FromJson(expectedJson_absPath, &absPath_expected)
	my.Test(absPath, absPath_expected, t)
}"""
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()