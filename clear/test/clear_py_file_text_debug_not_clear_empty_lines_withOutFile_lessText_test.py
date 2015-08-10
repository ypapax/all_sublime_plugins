import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
sys.path.insert(0, os.path.join(currentFolder, '../../moveNearReplace'))
import assertMy
import clearModel as clear
import unittest
import color
import filer2 as filer

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		inputText = """
    def run(self):
       print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
       print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
       print("new run repaire_relative_paths_plugin_")
       print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
       print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
       window = self.window
       
       


"""
		result = clear.py(inputText)
		expected = """
    def run(self):
       window = self.window
       """
	
		
		assertMy.stringDiffByLines(result, expected	)




if __name__ == '__main__':
	unittest.main()		
		