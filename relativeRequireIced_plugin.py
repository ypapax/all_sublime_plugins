
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/relative')
import relativeRequireIced_model
		


import sublime, sublime_plugin, os.path




		

class relative_just_require_icedCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		
		relativeRequireIced_model.doEveryThingByView(self.view, edit, False)



		
													
