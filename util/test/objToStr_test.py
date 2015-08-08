import unittest
import sys
sys.path.insert(0, '..')

import color
import assertMy
import assertMy

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		result = assertMy.objToStr(("hello\nhello2", "world"))
		expected = """("hello
hello2", "world")"""
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()