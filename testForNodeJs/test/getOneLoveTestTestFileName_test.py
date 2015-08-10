import os
import unittest
import sys
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
import color
import assertMy
import create_test_node_model

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		fatherFolder = "/a/b/c"
		localPath = "e/f.iced"
		# oneLoveFolder = os.path.join(fatherFolder, localPath, "1_Love")
		testingFolder = create_test_node_model.getTestingFolder(fatherFolder, localPath)
		oneLoveFolder = create_test_node_model.getOneLoveFolder(testingFolder)
		result = create_test_node_model.getOneLoveTestTestFileName(oneLoveFolder)
		expected = "/a/b/c/test/e/f.iced/1_Love/test_test.iced"
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()