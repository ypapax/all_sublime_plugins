
import unittest
import sys
sys.path.insert(0, '..')
import color
import util

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		result = util.clearEmptyLines("""def run(self):
       
       window = self.window""")

		expected = """def run(self):
       window = self.window"""

		self.assertEqual(result, expected)


		

if __name__ == '__main__':
	unittest.main()		
