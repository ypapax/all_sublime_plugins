import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
sys.path.insert(0, os.path.join(currentFolder, '../../moveNearReplace'))
import assertMy
import clearModel as clear
import unittest
import color
import filer2 as filer


class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		inputText = """import sublime
import sublime_plugin
import os
from os import listdir
from os.path import isfile, join
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/goodPath')

import findAllRelative_model
class repaire_relative_paths_plugin_Command(sublime_plugin.WindowCommand):
    def run(self):
       print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
       print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
       print("new run repaire_relative_paths_plugin_")
       print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
       print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
       window = self.window
       view = window.active_view()
       filename = view.file_name()
       findAllRelative_model.goAndWrite(filename)
       sublime.status_message("repaire_relative_paths_plugin done")
       


"""
		filename = os.path.join(currentFolder, 'files/printColor.poligon')

		filer.write(filename, inputText)

		clear.pyFile(filename)
		result = filer.read(filename)
		
		color.red('result')
		print(repr(result))

		expected = """import sublime
import sublime_plugin
import os
from os import listdir
from os.path import isfile, join
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/goodPath')
import findAllRelative_model
class repaire_relative_paths_plugin_Command(sublime_plugin.WindowCommand):
    def run(self):
       window = self.window
       view = window.active_view()
       filename = view.file_name()
       findAllRelative_model.goAndWrite(filename)
       sublime.status_message("repaire_relative_paths_plugin done")"""
		color.red('expected')
		print(expected)
		
		assertMy.stringDiffByLines(result, expected	)

		# self.assertEqual(result, expected)


if __name__ == '__main__':
	unittest.main()		
		