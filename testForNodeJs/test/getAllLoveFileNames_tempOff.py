import unittest
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
import color
import assertMy
import create_test_node_model

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		fatherFolder = os.path.abspath(os.path.join(currentFolder, 'testPoligon'))
		localFile = 'a/b.iced'
		inputFileName = fatherFolder+localFile
		testFolder = fatherFolder+'test/'
		


		result = create_test_node_model.getAllLoveFileNames(inputFileName)
		expectedTesting = testFolder + localFile + "/testing.iced"
		expectedTestTest = testFolder + localFile + "/1_Love/test_test.iced"
		inputJs = testFolder + localFile + "/1_Love/input.js"
		expectedJs = testFolder + localFile + "/1_Love/expected.js"
		expected = (expectedTesting, expectedTestTest, expectedJs, inputJs)
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()