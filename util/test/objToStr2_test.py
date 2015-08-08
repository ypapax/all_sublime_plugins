import unittest
import sys
sys.path.insert(0, '..')

import color
import assertMy
import assertMy

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		obj = ("hello\n world", ['org', 'ok'])
		result = assertMy.objToStr(obj)
		expected = """("hello
 world", ["org", "ok"])"""
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()