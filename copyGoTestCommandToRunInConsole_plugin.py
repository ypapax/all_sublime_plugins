import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, 'navigateTo'))
import navigateToModel

import sublime, sublime_plugin

class plugin_window_create_go_test_Command(sublime_plugin.WindowCommand):
	# it dont create test it just copy to clipboard string to run this test in console
    def run(self):
        view = self.window.active_view()
        filename = view.file_name()
        
        view = self.window.active_view()
        region1 = view.sel()[0]
        position = region1.a

        command = navigateToModel.fileNameAndPositionTo_goRunTestCommand(filename, position)

        sublime.set_clipboard(command)
        sublime.status_message("in clipboard: "+command)

        
        
