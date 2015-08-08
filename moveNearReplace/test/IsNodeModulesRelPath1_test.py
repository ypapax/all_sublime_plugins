import unittest
import sys
import color
import assertMy
import absRel3


class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		path = "/Users/maks/Dropbox/nodeApps/redisVgo/rdb/meta/delOrgIdByMeta.iced"
		result = absRel3.IsNodeModulesRelPath(path)
		expected = "/Users/maks/Dropbox/nodeApps/redisVgo/rdb/meta/delOrgIdByMeta.iced"
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()