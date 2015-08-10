import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, 'moveNearReplace'))
import absRel3
import sublime, sublime_plugin, os.path

class relative_path_insertCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		
		target = sublime.get_clipboard()
		source = self.view.file_name()
		
		
		relativePath = absRel3.RelAndCutIfNodeModules(source, target)
		print("relativePath in justInsertRelativePath_sublime_plugin_TextCommand.py")
		print(relativePath)

		self.view.insert(edit, self.view.sel()[0].begin(), relativePath) # do not change clipboard just inserts near cursor

		


		
													
