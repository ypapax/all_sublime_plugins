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


class clip_to_file_icedCommand(sublime_plugin.WindowCommand):
    def run(self):       
        clip = sublime.get_clipboard()
        result = pyOutPutParse.parseIced(clip)
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('result in clip_to_file_iced.py')
        print(result)
        pyOutPutParse.writeFile(result)
        self.window.run_command('plugin_next')
        print('plugin_next 2', '---------------------------------------------------')

