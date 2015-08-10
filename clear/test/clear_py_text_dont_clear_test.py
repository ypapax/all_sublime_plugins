import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
sys.path.insert(0, os.path.join(currentFolder, '../../moveNearReplace'))
import clearModel as clear
import assertMy
import unittest
import color

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		inputText = """\nimport sublime, sublime_plugin\nimport sys\nsys.path.insert(0, "'"/Users/maks/Library/Application Support/Sublime Text 3/Packages/clear"'")\nimport clearModel\nclass plugin_window_clear_Command(sublime_plugin.WindowCommand):\n    def run(self):\n    \tview = self.window.active_view()\n    \tfilename = view.file_name()\n    \tclearModel.pyFile(filename)\n"""

		result = clear.py(inputText)

		

		expected = inputText
		color.red('expected')
		print(expected)
		color.red('result')
		print(result)

		assertMy.stringDiffByLines(result, expected)
		


if __name__ == '__main__':
	unittest.main()		
		