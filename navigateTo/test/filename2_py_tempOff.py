
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
import pyFind
import unittest
import color
import pyFind

class Test(unittest.TestCase):
    def test_as(self):
        color.blue("test here baby")
        filename1 = os.path.join(currentFolder, '../testPoligon/py/as/a.py')
        obj = 'b_model'
        result = pyFind.filename2(filename1, obj)
        expected = os.path.join(currentFolder, '../testPoligon/py/as/b_model2.py')
        self.assertEqual(result, expected)
    def test_notAs(self):
        color.blue("test here baby")
        filename1 = os.path.join(currentFolder, '../testPoligon/py/a.py')
        obj = 'b_model'
        result = pyFind.filename2(filename1, obj)
        expected = os.path.join(currentFolder, '../testPoligon/py/b_model.py')
        self.assertEqual(result, expected)        

if __name__ == '__main__':
    unittest.main()     
