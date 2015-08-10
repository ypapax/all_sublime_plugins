
import sublime, sublime_plugin, os.path

import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/moveNearReplace')
import absRel3 as absRel


class RelativeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		
		target = sublime.get_clipboard()
		source = self.view.file_name()
		print('target:', target, '-----------------------------------------------------')
		print('source:', source, '-----------------------------------------------------')
		rel = absRel.Rel(source, target)
		
		for pos in self.view.sel():
			self.view.insert(edit, pos.begin(), rel)


		
													
