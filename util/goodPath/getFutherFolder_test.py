import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
import color
import getFutherFolder_model

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		startFromFile = "/Users/maks/Library/Application Support/Sublime Text 3/Packages/goodPath/forTest/a/b/c_start.js"
		result = getFutherFolder_model.get(startFromFile)
		expected = "/Users/maks/Library/Application Support/Sublime Text 3/Packages/goodPath/forTest/a"
		self.assertEqual (result, expected)
		

if __name__ == '__main__':
	unittest.main()		