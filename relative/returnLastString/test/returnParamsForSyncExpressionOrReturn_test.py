import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/relative/returnLastString')
import color
import assertMy
import returnLast

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")

		targetFileContent = """globalLinkForAdminDeleteCommentBy_id = require 'orad/model/globalLinkForAdminDeleteCommentBy_id.iced'
th = require 'throw'
orgLinkUrlByOrgId = require 'monvgo/model/org/orgLinkUrlByOrgId.iced'
makeLinkUrlGlobal = require '../../links/makeLinkUrlGlobal.iced'


module.exports = (comment)->

  globalLink = globalLinkForAdminDeleteCommentBy_id comment._id
  orgUrlLink = orgLinkUrlByOrgId comment.OrgId
  globalOrgiBizLinkUrl = makeLinkUrlGlobal orgUrlLink
  msgForEmail = comment.Info + "\ndelete: #{globalOrgiBizLinkUrl}"
  """
		result = returnLast.returnParamsForSyncExpressionOrReturn(targetFileContent)
		expected = "msgForEmail"
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()