import sys
import sublime, sublime_plugin
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, 'coffee'))
import coffee_compile_model
		
class coffee_compile_plugin_Command(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        filename = view.file_name()
        coffee_compile_model.coffeeCompile(filename)
        sublime.status_message("coffee compile ok")
        
        
