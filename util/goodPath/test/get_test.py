import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/goodPath')
import color
import assertMy
import getFutherFolder_model

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		result = getFutherFolder_model.get('/Users/maks/Dropbox/nodeApps/redisVgo/rdb/adres/closeByHash.iced')
		expected = "/Users/maks/Dropbox/nodeApps/redisVgo"
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()