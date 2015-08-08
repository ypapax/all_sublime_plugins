
import unittest
import sys
sys.path.insert(0, '..')
import color
import util

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		result = util.clearEmptyLines("""hellow\n\nworld""")

		expected = """hellow\nworld"""

		self.assertEqual(result, expected)


		

if __name__ == '__main__':
	unittest.main()		
