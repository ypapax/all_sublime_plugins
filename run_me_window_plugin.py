import re
import sys

import sublime, sublime_plugin
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, 'copyPluginName'))
import readMe_model

class plugin_window__run_command__Command(sublime_plugin.WindowCommand):
    def run(self):
    	commandName = readMe_model.windowPluginName(self)

    	
    	result = "window.run_command('{0}')".format(commandName)
    	sublime.set_clipboard(result)
    	sublime.status_message("in clipboard: "+result)
        
