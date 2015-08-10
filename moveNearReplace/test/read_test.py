import unittest
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
import color
import assertMy
import filer2

class Test(unittest.TestCase):
    def test_testName(self):
        color.blue("test here baby")

        result = filer2.read(os.path.join(currentFolder, '../../find_usages_plugin.py'))

        indexes = range(638)


        for i in indexes:
            # color.red(str(i)+result[i])
            number = color.color(str(i), "red")
            char = color.color(repr(result[i]), "green")
            line = "{0} - {1}".format(number, char)
            print(line)
        # expected = ""
        # assertMy.equals(result, expected)

if __name__ == '__main__':
    unittest.main()