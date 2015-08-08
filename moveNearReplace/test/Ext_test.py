import unittest
import sys
import color
import assertMy
import absRel3

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		result = absRel3.Ext('/a/b.js')
		expected = "js"
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()