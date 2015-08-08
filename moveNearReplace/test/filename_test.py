
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
import assertMy
		


import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/moveNearReplace')
import absRel3
		

import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
import color

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		result = absRel3.filename("/a/b/c.js")
		expected = "c"
		assertMy.equals(result, expected)

		

if __name__ == '__main__':
	unittest.main()		
