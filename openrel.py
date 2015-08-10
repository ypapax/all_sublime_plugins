import sublime, sublime_plugin
import re, os, os.path

class OpenrelCommand(sublime_plugin.WindowCommand):
  
    def run(self):
        relative = sublime.get_clipboard()
        absolute1 = ""
        absolute1 = self.window.active_view().file_name()
        absolute2 = os.path.normpath(os.path.join(os.path.dirname(absolute1), relative))
        self.window.open_file(absolute2)
                  
        
    def is_enabled(self):
        return bool(sublime.get_clipboard().strip())

