import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, 'ClipboardPathCuted'))
import clipboardPathModel
        
import sublime, sublime_plugin



class clipboard_path_cutted_Command(sublime_plugin.WindowCommand):
    def run(self):

        clip = sublime.get_clipboard()
        clearedPath = clipboardPathModel.do(clip)

        sublime.set_clipboard(clearedPath)
        sublime.status_message("set to clipboard: "+clearedPath)
        self.window.run_command('open_clipboard_path')

      

        


        
