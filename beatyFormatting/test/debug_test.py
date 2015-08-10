import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
import beatyModel
import unittest
import color
import assertMy


class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		inputText = """\tdef py(text):
	regex = "{0}print\(.+\)|{0}color\..+\)".format("\n\s+")
	replace1 = re.sub (regex, '', text)
	# result = util.clearEmptyLines(replace1)
	result = replace1
	return result
def pyFile(filename):
	fileText = filer.read(filename)
	fileText = py(fileText)
	filer.write(filename, fileText)"""
		expected = """def py(text):\n\tregex = "{0}print\\(.+\\)|{0}color\\..+\\)".format("\n\\s+")\n\treplace1 = re.sub (regex, \'\', text)\n\t# result = util.clearEmptyLines(replace1)\n\tresult = replace1\n\treturn result\n\n\ndef pyFile(filename):\n\tfileText = filer.read(filename)\n\tfileText = py(fileText)\n\tfiler.write(filename, fileText)"""
		result = beatyModel.py(inputText)	
		color.red("inputText")
		print(repr(inputText))
		print(inputText)
		assertMy.stringDiffByLines(result, expected)




if __name__ == '__main__':
	unittest.main()		

		

