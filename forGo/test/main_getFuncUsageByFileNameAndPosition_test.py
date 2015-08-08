import unittest
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
import color
import assertMy
import modelCopyMethoUsageGo

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		filename=os.path.join(currentFolder, 'poligon/forTest.go')
		position = 1283
		result = modelCopyMethoUsageGo.main_getFuncUsageByFileNameAndPosition(filename, position)
		expected = """/*var (
	

	firstDigits string
	en bool
	ds *calldb.DataStore

	locals *MegaLocals
        )*/
locals = numbersMegaLocals(firstDigits,en,ds)"""
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()