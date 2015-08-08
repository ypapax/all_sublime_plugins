
import sys
import sublime, sublime_plugin

import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/coffee')
import coffee_compile_model
		
class coffee_compile_plugin_Command(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        filename = view.file_name()
        coffee_compile_model.coffeeCompile(filename)
        sublime.status_message("coffee compile ok")
        
        
