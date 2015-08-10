import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/relative/returnLastString')
import color
import assertMy
import returnLast

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		fileName = "/Users/maks/Library/Application Support/Sublime Text 3/Packages/relative/returnLastString/test/poligon/testFile.iced"
		result = returnLast.doAllByFileName(fileName)
		expected = """[err, telIdList] = result
th.err err"""
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()