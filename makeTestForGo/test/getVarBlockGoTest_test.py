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
		(caller, args, returnParams) = ("org *Org", "orgId string, someBool bool", "org *Org, ok bool")
		result = generateTestFileNameForGoTest.getVarBlockGoTest(caller, args, returnParams)
		expected = ('var (\n\torg *Org\n\n\torgId string\n\tsomeBool bool\n\n\torg *Org\n\tok bool\n\n\torg_expected *Org\n\tok_expected bool\n        )', 'orgId,someBool', 'org,ok')
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()