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
		(caller, methodName, returnArgsCommaStr, varsCommasStr) = ("caller", "methodName", "res1,res2", "var1,var2,var3")
		result = generateTestFileNameForGoTest.innerTestFuncPartGoTestPrepare_callTestableFunc(caller, methodName, returnArgsCommaStr, varsCommasStr)
		expected = "res1,res2 = caller.methodName(var1,var2,var3)"
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()