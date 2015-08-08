
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../util'))
import pyFind
import unittest
import color
import navigateToModel

class Test(unittest.TestCase):
    def test_testName(self):
        color.blue("test here baby")

        filename1 = os.path.join(currentFolder, '../testPoligon/py/as/a.py')
        position1 = len("""import b_model2 as b_model

import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
import color



class Test(unittest.TestCase):
    
    def test_bigFile(self):
        color.blue("test here baby")
        

        expected = ['', 'startsLikeCodeNumber']
        


        result = b_model.getO""")
      
        result = navigateToModel.filenameAndPositionTransform(filename1, position1)

        expected = ('/Users/maks/Library/Application Support/Sublime Text 3/Packages/navigateTo/testPoligon/py/as/b_model2.py', 
            790)
        print(result)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()     
