import os
from os.path import basename

import sublime, sublime_plugin

class plugin_text_copy_name_Command(sublime_plugin.WindowCommand):
    """Set opened file name to clipboard without extension"""
    def run(self):
        
        view = self.window.active_view()
        filename = view.file_name()
        justName = basename(filename)

        
        justName = os.path.splitext(justName)[0]
        sublime.set_clipboard(justName)
        sublime.status_message("set to clipboard: "+ justName)
