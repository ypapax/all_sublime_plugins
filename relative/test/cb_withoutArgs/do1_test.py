import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/relative')
import color
import assertMy
import relativeRequireIced_model

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		# /Users/maks/Dropbox/nodeApps/monvgo/model/mongo/mdb_vgo_cb.iced
		source = '/Users/maks/Library/Application Support/Sublime Text 3/Packages/relative/test/cb_withoutArgs/poligon/source.iced'
		target = '/Users/maks/Library/Application Support/Sublime Text 3/Packages/relative/test/cb_withoutArgs/poligon/target.iced'
		result = relativeRequireIced_model.do(target, source)
		expected = ("target = require './target.iced'", 'await target defer err, db')

		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()