import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, 'makeTest'))
import forPy
        

import sublime, sublime_plugin

class plugin_window_create_py_test_Command(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        filename = view.file_name()
        
        view = self.window.active_view()
        region1 = view.sel()[0]
        position = region1.a

        testFile = forPy.createFromPosition(filename, position)
        self.window.open_file(testFile)

        
        
