import os
import shutil
import sublime
import sublime_plugin
import ntpath



import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/moveNearReplace')


import pyOutPutParse5 as pyOutPutParse

import color
import util
import filer2 as filer


class clip_clear_to_fileCommand(sublime_plugin.WindowCommand):
    def run(self):       
        clip = sublime.get_clipboard()
        
        fileName = '/Users/maks/temp'
        filer.write(fileName, clip)
        self.window.open_file(fileName, sublime.ENCODED_POSITION)
        self.window.run_command("go_to_line", {'line':'0'})

