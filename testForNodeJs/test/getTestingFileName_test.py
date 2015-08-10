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
		inputFileName = '/Users/maks/Library/Application Support/Sublime Text 3/Packages/testForNodeJs/test/testPoligon/a/b.iced'
		expected = inputFileName+'/testing.iced'

		result = create_test_node_model.getTestingFileName(inputFileName)
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()