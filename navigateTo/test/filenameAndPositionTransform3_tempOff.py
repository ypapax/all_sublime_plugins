
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/navigateTo')
import pyFind
import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
import color




import navigateToModel
        

class Test(unittest.TestCase):
    def test_testName(self):
        color.blue("test here baby")
        filename1 = '/Users/maks/Library/Application Support/Sublime Text 3/Packages/navigateTo/testPoligon/clip_clear_to_file.py'
        position1 = 568
      
        result = navigateToModel.filenameAndPositionTransform(filename1, position1)

        expected = ('/Users/maks/Library/Application Support/Sublime Text 3/Packages/moveNearReplace/filer2.py', 705 )
            
        print(result)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()     
