import sublime, sublime_plugin, os.path

class log_commands_onCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		
		sublime.log_commands(True) 
class log_commands_offCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		
		sublime.log_commands(False) 		

		
													
