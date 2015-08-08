import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/makeTest')
import color
import assertMy
import generateTestFileNameForGoTest

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		(caller, method, args, returnParams) = generateTestFileNameForGoTest.getGoFuncDeclarationPartsByLineContent("func (caller *CallerType) LocalsByYoutubeId(ds *mon.DataStore, youtubeId string) int {")
		assertMy.equals(caller, "caller *CallerType")
		assertMy.equals(method, "LocalsByYoutubeId")
		assertMy.equals(args, "ds *mon.DataStore, youtubeId string")
		assertMy.equals(returnParams, "")

if __name__ == '__main__':
	unittest.main()