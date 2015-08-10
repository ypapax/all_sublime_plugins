import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, 'testForNodeJs'))
import color
import create_test_node_model
		
		
import sublime, sublime_plugin

class plugin_window_create_test_node_Command(sublime_plugin.WindowCommand):
    def run(self):
    	window = self.window
    	view = window.active_view()
    	filename = view.file_name()
    	testingFileName = create_test_node_model.get(filename)

    	window.open_file(testingFileName)

    	
        
