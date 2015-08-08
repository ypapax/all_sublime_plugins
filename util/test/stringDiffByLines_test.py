
import unittest
import sys
sys.path.insert(0, '..')
import color
import sys
import assertMy
		
class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		str1 = "kuku\n\nkuku2"
		str2 = "kuku\nkuku3"
		# assertMy.stringDiffByLines(str1, str2)
		
	# def test_testName2(self):
	# 	color.blue("test here baby")
	# 	str1 = "kuku\n\nkuku2"
	# 	str2 = "kuku\nkuku3"
	# 	assertMy.stringDiffByLines(str1, str2)	
if __name__ == '__main__':
	unittest.main()		
