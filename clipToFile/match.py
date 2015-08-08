import re
def iced(string):
	m = re.findall(r'(/.*\.iced):(\d+)', string)
	return m

def go(string):
	m = re.findall(r'(/.*\.iced):(\d+)', string)
	return m