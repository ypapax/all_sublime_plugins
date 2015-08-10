import sublime, sublime_plugin
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, 'workflow'))
import iterationsClass as ic

class plugin_window_iterations_Command(sublime_plugin.WindowCommand):
    def run(self, command="add"):
        view = self.window.active_view()
        filename = view.file_name()

        reg1 = view.sel()[0]
        (row, col) = view.rowcol(reg1.a)
        row = row + 1
        file_row = "{0}:{1}".format(filename, row)
        print('row = ', row)
        i = ic.Iterations()
        i.realFolder()

        result = i.command(command, file_row)

        if result:
            toClip = result
            sublime.set_clipboard(toClip)
            sublime.status_message("set to clipboard: "+toClip)

            self.window.run_command('open_clipboard_path')
        else:
            sublime.status_message("no changing view")  


        


        
