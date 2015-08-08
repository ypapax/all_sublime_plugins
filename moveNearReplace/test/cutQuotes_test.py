import cutQuotes
import unittest

class Test(unittest.TestCase):
	def test_basic_addition(self):
		inputList = ["'../grab/2_allFilesAtOnes/findInFullRegion'", '"./grab/redisFunc"']
		result = cutQuotes.cutQuotes (inputList)
		expected = ["../grab/2_allFilesAtOnes/findInFullRegion", './grab/redisFunc']
		self.assertEqual (result, expected)

if __name__ == '__main__':
	unittest.main()		