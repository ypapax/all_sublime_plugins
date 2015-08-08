import os
import shutil
import sublime
import sublime_plugin
import ntpath



import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/clipToFile')


import pyOutPutParse5 as pyOutPutParse
import color
import util


class clip_to_fileCommand(sublime_plugin.WindowCommand):
    def run(self):       
        clip = sublime.get_clipboard()
        result = pyOutPutParse.parse(clip)
        pyOutPutParse.writeFile(result)
        self.window.run_command('plugin_next')
