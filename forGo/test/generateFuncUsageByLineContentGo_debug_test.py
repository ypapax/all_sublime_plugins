import unittest
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
import color
import assertMy
import modelCopyMethoUsageGo

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		result = modelCopyMethoUsageGo.generateFuncUsageByLineContentGo("""func getOrSetLoginAndPassTest(beforeTestPass, beforeTestEmail, expectedEmail string, expectedPassLen int, t *testing.T) {
""")
		expected = """/*var (
	

	beforeTestPass string
	beforeTestEmail string
	expectedEmail string
	expectedPassLen int
	t *testing.T

        )*/
getOrSetLoginAndPassTest(beforeTestPass,beforeTestEmail,expectedEmail,expectedPassLen,t)"""
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()