import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/moveNearReplace')
import color
import assertMy
import filer2

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		result = filer2.read('/Users/maks/Dropbox/nodeApps/orgi/views/selects.jade')
		print(repr(result))
		# expected = ""
		# assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()