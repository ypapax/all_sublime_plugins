
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
		filename = "/asdf/adfa/d"
		result = absRel3.folder(filename)
		expected = "/asdf/adfa"
		self.assertEqual(result, expected)

if __name__ == '__main__':
	unittest.main()		
