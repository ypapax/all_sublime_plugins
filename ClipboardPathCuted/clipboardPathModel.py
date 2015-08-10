import re
def do(line):
	clearedLine = re.sub(r'.*?(/.*?:\d+:\d+).*', r'\1', line)
	  # at aboutSocr (/Users/maks/Dropbox/nodeApps/redisVgo/rdb/city/fullCity/fullCityNameWithSocrWithoutRegionAndCountry_byCity.iced:17:4)


	return clearedLine.strip()
