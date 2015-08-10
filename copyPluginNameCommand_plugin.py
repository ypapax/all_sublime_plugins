import sublime, sublime_plugin
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, 'copyPluginName'))
import readMe_model

class plugin_window__copy_plugin_name_for_command__Command(sublime_plugin.WindowCommand):
    def run(self):
    	pluginName = readMe_model.windowPluginName(self)
    	pluginNameNoSpace = pluginName.replace('_', ' ')
    	commandLine = '{"caption": "My: '+pluginNameNoSpace+'", "command": "'+pluginName+'"},'
    	sublime.status_message("in clipboard"+commandLine)
    	sublime.set_clipboard(commandLine)
    	self.window.run_command('commands_file')
    	

        
