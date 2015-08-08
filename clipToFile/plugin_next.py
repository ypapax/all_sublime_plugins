

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


def openNextOrPrev(self, move):
    view = self.window.active_view()
    region1 = view.sel()[0]
    if(region1 is not None):
        line = view.line(region1)
        
        (row, col) = view.rowcol(line.begin())  
        lineNumber = row + 1
    else:
        lineNumber = 0
    
    filename = view.file_name()
    fileNameAndLine = filename + ":" + str(lineNumber)
       
    result = pyOutPutParse.read(fileNameAndLine, move)     
    if not result:
        sublime.status_message("no data in file")
    else:    
        self.window.open_file(result, sublime.ENCODED_POSITION)

class plugin_nextCommand(sublime_plugin.WindowCommand):
    def run(self):
        openNextOrPrev(self, "next")

# class plugin_next_textCommand(sublime_plugin.TextCommand):
#     def run(self, edit):
#         openNextOrPrev(self, "next")        
class plugin_top_next_prevCommand(sublime_plugin.WindowCommand):
    def run(self):
        openNextOrPrev(self, "top")     
class plugin_prevCommand(sublime_plugin.WindowCommand):
    def run(self):
        openNextOrPrev(self, "prev")        