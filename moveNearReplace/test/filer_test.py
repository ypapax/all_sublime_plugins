import filer2 as filer
import unittest
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
import color

class Test(unittest.TestCase):
    

 
    def test_writeFile(self):
        path = os.path.join(currentFolder, '../writeThisFile.iced')
        filer.write(path, "")
        empty_expected = filer.read(path)
        self.assertEqual (empty_expected, "")

        actualValue = """ 3
        4
         5"""

        filer.write(path, actualValue) 
        mustEqualToActual = filer.read(path)
        self.assertEqual(mustEqualToActual, actualValue)


if __name__ == '__main__':
    unittest.main()     