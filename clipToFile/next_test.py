
import unittest
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '../util'))
sys.path.insert(0, os.path.join(currentFolder, '../clipToFile'))
import color
import next3 as next



class Test(unittest.TestCase):
    def test_testName(self):
        color.blue("test here baby")
        string = '/file_2_Path:9'
        data = ['/filePath:6', '/file_2_Path:9', '/file_3_Path:3']
        result = next.next(data, string)
        expected = '/file_3_Path:3'
        self.assertEqual (result, expected)
    def test_testName2(self):
        color.blue("test here baby")
        string = '/filePath:6'
        data = ['/filePath:6', '/file_2_Path:9', '/file_3_Path:3']
        result = next.next(data, string)
        expected = '/file_2_Path:9'
        self.assertEqual (result, expected)    
    def test_testName3(self):
        color.blue("test here baby")
        string = '/file_3_Path:3'
        data = ['/filePath:6', '/file_2_Path:9', '/file_3_Path:3']
        result = next.next(data, string)
        expected = '/filePath:6'
        self.assertEqual (result, expected)     
    def test_testName4(self):
        color.blue("test here baby")
        string = '/file_3_Path:5'
        data = ['/filePath:6', '/file_2_Path:9', '/file_3_Path:3']
        result = next.next(data, string)
        expected = '/file_3_Path:3'
        self.assertEqual (result, expected)     
    def test_testName5(self):
        color.blue("test here baby")
        string = '/file_2_Path:8'
        data = ['/filePath:6', '/file_2_Path:9', '/file_3_Path:3']
        result = next.get(data, string, "next")
        expected = '/file_2_Path:9'
        self.assertEqual (result, expected)         
    def test_testName5(self):
        color.blue("test here baby")
        string = '/file_2_Path:8'
        data = ['/filePath:6', '/file_2_Path:9', '/file_3_Path:3']
        result = next.get(data, string, "next")
        expected = '/file_2_Path:9'
        self.assertEqual (result, expected)         
    def test_prev(self):
        color.blue("test here baby")
        string = '/file_2_Path:9'
        data = ['/filePath:6', '/file_2_Path:9', '/file_3_Path:3']
        result = next.prev(data, string)
        expected = '/filePath:6'
        self.assertEqual (result, expected)     
    def test_prev2(self):
        color.blue("test here baby")
        string = '/filePath:6'
        data = ['/filePath:6', '/file_2_Path:9', '/file_3_Path:3']
        result = next.prev(data, string)
        expected = '/file_3_Path:3'
        self.assertEqual (result, expected)      
    def test_prev3(self):
        color.blue("test here baby")
        string = '/file_2_Path:12'
        data = ['/filePath:6', '/file_2_Path:9', '/file_3_Path:3']
        result = next.prev(data, string)
        expected = '/file_2_Path:9'
        self.assertEqual (result, expected)     
    def test_prevNotInList(self):
        color.blue("test here baby")
        string = '/fildsdfse_2_Path:12'
        data = ['/filePath:6', '/file_2_Path:9', '/file_3_Path:3']
        result = next.prev(data, string)
        expected = '/file_3_Path:3'
        self.assertEqual (result, expected)     
    def test_nextNotInList(self):
        color.blue("test here baby")
        string = '/fildsdfse_2_Path:12'
        data = ['/filePath:6', '/file_2_Path:9', '/file_3_Path:3']
        result = next.next(data, string)
        expected = '/file_3_Path:3'
        self.assertEqual (result, expected)     

if __name__ == '__main__':
    unittest.main()     
