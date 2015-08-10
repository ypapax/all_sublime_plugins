import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, 'beatyFormatting'))
import beatyModel
		
import sublime, sublime_plugin

class plugin_window_beaty_python_Command(sublime_plugin.WindowCommand):
    def run(self):
    	view = self.window.active_view()
    	filename = view.file_name()
    	beatyModel.pyFileFull(filename)

        
