import sublime
import sublime_plugin
import os
from os import listdir
from os.path import isfile, join
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/goodPath')

import findAllRelative_model
class repaire_relative_paths_for_all_recursive_plugin_Command(sublime_plugin.WindowCommand):
    def run(self):
       
       
       
       
       
       
       window = self.window
       view = window.active_view()
       filename = view.file_name()

       findAllRelative_model.repaireRecursive(filename)
       sublime.status_message("repaire_relative_paths_for_all_recursive_plugin_ done")
       


