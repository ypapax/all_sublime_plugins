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
		(caller, method, args, returnParams) = generateTestFileNameForGoTest.getGoFuncDeclarationPartsByLineContent("func OneTwoFiftyTwoAnchors() (html template.HTML) {")
		assertMy.equals(caller, "")
		assertMy.equals(method, "OneTwoFiftyTwoAnchors")
		assertMy.equals(args, "")
		assertMy.equals(returnParams, "html template.HTML")

if __name__ == '__main__':
	unittest.main()