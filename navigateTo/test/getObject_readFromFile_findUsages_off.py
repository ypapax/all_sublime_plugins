
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/navigateTo')
import pyFind
import navigateToModel

import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
import color


import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/moveNearReplace')
import filer2


inputText = filer2.read('/Users/maks/Library/Application Support/Sublime Text 3/Packages/findUsages/find_usages_plugin.py')



class Test(unittest.TestCase):
    
    def test_bigFile(self):
        color.blue("test here baby")
        
        indexes = range(len(inputText))
        

        for i in indexes:


        expected = ['reactOnCursorPosition', 'starter']
        
        position = 638

        result = navigateToModel.getObject(inputText, position)
        color.red('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('result')
        print(repr(result))
        color.red('*****************************************************************')

        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()     
