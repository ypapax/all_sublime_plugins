import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, 'relative'))
import relativeRequireIced_model
import sublime, sublime_plugin, os.path

class relative_just_require_icedCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		
		relativeRequireIced_model.doEveryThingByView(self.view, edit, False)



		
													
