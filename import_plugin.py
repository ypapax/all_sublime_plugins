import os
import sublime, sublime_plugin

class plugin_window_import_Command(sublime_plugin.WindowCommand):
    def run(self):
    	self.window.run_command('plugin_text_copy_name_')
    	view = self.window.active_view()
    	filename = view.file_name()
    	dirname = os.path.dirname(filename)
    	pluginName = sublime.get_clipboard()
    	importLine = "import "+pluginName
    	sublime.status_message("set to clipboard: "+importLine)
    	insertPath ="""
import sys
sys.path.insert(0, '{0}')
{1}
		""".format(dirname, importLine)
    	sublime.set_clipboard(insertPath)
        

		
		