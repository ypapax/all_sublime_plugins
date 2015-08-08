import unittest
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
import color
import assertMy
import navigateToModel

class Test(unittest.TestCase):
  def test_testName(self):
    color.blue("test here baby")
    filename = os.path.join(currentFolder, 'poligon/example.go')
    position = 43
    result = navigateToModel.fileNameAndPositionTo_goRunTestCommand(filename, position)
    expectedPath = os.path.join(currentFolder, 'poligon')
    expected = """cd "{0}"; TALK=1 go test -test.run Test_FromJson0""".format(expectedPath)
    assertMy.equals(result, expected)

if __name__ == '__main__':
  unittest.main()