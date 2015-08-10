import unittest
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
sys.path.insert(0, os.path.join(currentFolder, '..'))
import color
import assertMy
import create_test_node_model

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		inputFileName = "/a/b/c/d.iced"
		fatherFolder = "/a/b"

		result = create_test_node_model.localFileName(inputFileName, fatherFolder)
		expected = "c/d.iced"
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()