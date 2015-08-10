import unittest
import sys
import get_test_model

class Test(unittest.TestCase):
	def test_testName(self):
		get_test_model.makeGetTest(False)
		get_test_model.makeGetTest(False)

if __name__ == '__main__':
	unittest.main()