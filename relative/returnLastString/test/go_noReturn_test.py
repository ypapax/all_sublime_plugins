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
		inputModel = """module.exports = (autocb)->

	await rf.getO "telsAll", defer telsObjectList
	telIdList = []
	for tel in telsObjectList
		counterO tel, telsObjectList
		await insertTel tel, defer()
		telIdList.push tel.Id
"""
		result = returnLast.go(inputModel)
		expected = ""
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()