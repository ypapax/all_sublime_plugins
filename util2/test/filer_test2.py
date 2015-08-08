
import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
import color
import filer2 as filer
class Test(unittest.TestCase):
    def test_zero(self):
        pos = 729
        filename = '/Users/maks/Dropbox/nodeApps/call/deleteDb.iced'
        data = filer.read(filename)
        char = data[729]
        print('char=',char)
        

if __name__ == '__main__':
    unittest.main()     
