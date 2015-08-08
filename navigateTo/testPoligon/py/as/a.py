import b_model2 as b_model

import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
import color



class Test(unittest.TestCase):
    
    def test_bigFile(self):
        color.blue("test here baby")
        

        expected = ['', 'startsLikeCodeNumber']
        


        result = b_model.getObject(inputText, positionForBigTest)

        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()     
