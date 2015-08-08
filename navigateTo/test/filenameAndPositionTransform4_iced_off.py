
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
        filename1 = '/Users/maks/Dropbox/nodeApps/call/db.iced'
        position1 = 626
      
        result = navigateToModel.filenameAndPositionTransform(filename1, position1)

        expected = ('/Users/maks/Dropbox/nodeApps/call/db.iced', 868 )
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()     
