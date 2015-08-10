import os
import sys
import shutil
import sublime
import sublime_plugin
import ntpath
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, 'clipToFile'))
sys.path.insert(0, os.path.join(currentFolder, 'util'))
import pyOutPutParse5 as pyOutPutParse
import color
import util


class clip_to_file_icedCommand(sublime_plugin.WindowCommand):
    def run(self):       
        clip = sublime.get_clipboard()
        result = pyOutPutParse.parseIced(clip)
        print(result)
        pyOutPutParse.writeFile(result)
        self.window.run_command('plugin_next')

