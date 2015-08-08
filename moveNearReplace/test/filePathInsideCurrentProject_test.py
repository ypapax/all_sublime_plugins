import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/moveNearReplace')
import color
import assertMy
import absRel3

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		sourceFilePath = "/Users/maks/Dropbox/nodeApps/orad/test/sodora.iced"
		targetFilePath = "/Users/maks/Dropbox/nodeApps/redisVgo/rdb/meta/delOrgIdByMeta.iced"
		result = absRel3.filePathInsideCurrentProject(sourceFilePath, targetFilePath)
		expected = False
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()