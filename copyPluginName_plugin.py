import re
import sys

import sublime, sublime_plugin
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, 'copyPluginName'))
import readMe_model

class plugin_window__command_name__Command(sublime_plugin.WindowCommand):
    def run(self):
    	commandName = readMe_model.windowPluginName(self)

    	sublime.set_clipboard(commandName)
    	sublime.status_message("in clipboard: "+commandName)
        
