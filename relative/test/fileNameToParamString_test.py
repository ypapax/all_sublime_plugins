import unittest
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
import color
import assertMy
import getParams

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("virsion")
		print(sys.version_info)
		inputModel = os.path.join(currentFolder, 'filesPoligon/poligon.iced')
		result = getParams.fileNameToParamString(inputModel)
		expected = "countryId, regionId"
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()