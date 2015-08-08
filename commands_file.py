import os
import shutil
import sublime
import sublime_plugin
import ntpath

class commands_fileCommand(sublime_plugin.WindowCommand):

    def run(self):
        currentFolder = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(currentFolder, '../Default/Default (OSX).sublime-commands:2')

        print(path)
        
        self.window.open_file(path, sublime.ENCODED_POSITION)