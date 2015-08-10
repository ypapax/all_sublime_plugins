import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, 'moveNearReplace'))


import getRel
    
import absRel3 as absRel
import sublime, sublime_plugin

class plugin_window__go_to_relative_plugin__Command(sublime_plugin.WindowCommand):
    def run(self, rel): 
        window = self.window
        view = self.window.active_view()
        filename = view.file_name()
        if not rel:
            view = self.window.active_view()
            region1 = view.sel()[0]
            line = view.line(region1)
            linetext = view.substr(line)
            rel = linetext
            rel = getRel.getRel(rel)[0]
        abs2 = absRel.AbsAddExtension(filename, rel)        

        print ("abs1: ", filename)
        print ("abs2: ", abs2)
        self.window.open_file(abs2)
