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
		result = create_test_node_model.get2(os.path.abspath(os.path.join(currentFolder, 'testPoligon/vgoPoligon/target.iced')))
		expected = os.path.abspath(os.path.join(currentFolder, 'testPoligon/vgoPoligon/test/target.iced/testing.iced'))
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()