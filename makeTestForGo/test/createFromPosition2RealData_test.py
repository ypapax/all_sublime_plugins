import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/makeTest')

import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/moveNearReplace')
import filer2

import color
import assertMy
import generateTestFileNameForGoTest
import os


class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")

		filename = os.path.dirname(os.path.realpath(__file__)) + "/poligion/poligonRealFromRunly.go"
		position = 461

		expected = os.path.dirname(os.path.realpath(__file__)) + "/poligion/Test_searchYoutubeByYoutubeId_test.go"

		if os.path.isfile(expected):
			os.remove(expected)
		result = generateTestFileNameForGoTest.createFromPosition(filename, position)
		testFileContent = filer2.read(result)

		expectedText = """package db
import (
    "my"
	"testing"
)

func Test_searchYoutubeByYoutubeId(t *testing.T) {
    var (
	

	youtubeId string

	onlyOne *YoutubeSearchResult

	onlyOne_expected *YoutubeSearchResult
        )
    onlyOne = searchYoutubeByYoutubeId(youtubeId)
    
	expectedJson_onlyOne := ``
	my.FromJson(expectedJson_onlyOne, &onlyOne_expected)
	my.Test(onlyOne, onlyOne_expected, t)
}"""


		assertMy.equals(result, expected)
		assertMy.equals(testFileContent, expectedText)

if __name__ == '__main__':
	unittest.main()