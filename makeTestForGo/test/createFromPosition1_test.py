import unittest
import sys

import sys
import filer2

import color
import assertMy
import generateTestFileNameForGoTest
import os


class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")

		filename = os.path.dirname(os.path.realpath(__file__)) + "/poligion/poligon.go"
		position = 56

		expected = os.path.dirname(os.path.realpath(__file__)) +  "/poligion/Test_doAllForMiByUrl_test.go"
		if os.path.isfile(expected):
			os.remove(expected)
		result = generateTestFileNameForGoTest.createFromPosition(filename, position)
		testFileContent = filer2.read(result)

		expectedText = """package elit
import (
    "my"
	"testing"
)

func Test_doAllForMiByUrl(t *testing.T) {
    var (
	

	url string
	expected menuItem
	t *testing.T


        )
    doAllForMiByUrl(url,expected,t)
    
}"""


		assertMy.equals(result, expected)
		assertMy.equals(testFileContent, expectedText)

if __name__ == '__main__':
	unittest.main()