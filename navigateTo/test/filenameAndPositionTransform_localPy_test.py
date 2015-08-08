import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
import pyFind
import unittest
import sys
import color
import navigateToModel
        

class Test(unittest.TestCase):
    def test_testName(self):
        color.blue("test here baby")
        currentFolder = os.path.dirname(os.path.realpath(__file__))
        filename1 = os.path.join(currentFolder, '../testPoligon/local.py')
        position1 = 22
      
        result = navigateToModel.filenameAndPositionTransform(filename1, position1)

        expected = (filename1, 9)
            
        print(result)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()     