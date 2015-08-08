import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/moveNearReplace')

import filer2 as filer

import sublime, sublime_plugin

class plugin_window__find_and_get_relative__Command(sublime_plugin.WindowCommand):
    def run(self):
    	view = self.window.active_view()
    	filename = view.file_name()

    	filer.read(filename)


        
