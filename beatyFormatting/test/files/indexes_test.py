
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/beatyFormatting')
import duplicateLines
		

import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
import color

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		lis = ["1", "2", "1"]
		result = duplicateLines.indexes(lis, "1")
		expected = [0, 2]
		self.assertEqual(result, expected)
		

if __name__ == '__main__':
	unittest.main()		
		