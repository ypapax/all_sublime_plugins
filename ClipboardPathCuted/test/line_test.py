import unittest
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))

import color
import assertMy
import clipboardPathModel

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		line = "  at aboutSocr (/Users/maks/Dropbox/nodeApps/redisVgo/rdb/city/fullCity/fullCityNameWithSocrWithoutRegionAndCountry_byCity.iced:17:4)\n"
		result = clipboardPathModel.do(line)
		expected = "/Users/maks/Dropbox/nodeApps/redisVgo/rdb/city/fullCity/fullCityNameWithSocrWithoutRegionAndCountry_byCity.iced:17:4"
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()