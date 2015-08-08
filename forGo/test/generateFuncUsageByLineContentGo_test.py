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
		result = modelCopyMethoUsageGo.generateFuncUsageByLineContentGo("""func mainPageMegaLocals(en bool, ds *calldb.DataStore) (locals *MegaLocals) {
""")
		expected = """/*var (
	

	en bool
	ds *calldb.DataStore

	locals *MegaLocals
        )*/
locals = mainPageMegaLocals(en,ds)"""
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()