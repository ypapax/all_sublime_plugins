import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/moveNearReplace')
import color
import assertMy
import filer2

class Test(unittest.TestCase):
    def test_testName(self):
        color.blue("test here baby")

        result = filer2.read('/Users/maks/Library/Application Support/Sublime Text 3/Packages/findUsages/find_usages_plugin.py')

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