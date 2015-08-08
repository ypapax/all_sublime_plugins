import sublime, sublime_plugin
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/moveNearReplace')
import filer2 as filer
import sys
import navigateToModel
import os
class navigate_to_search_targetCommand(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        region1 = view.sel()[0]
        position = region1.a
        view = self.window.active_view()
        filename = view.file_name()
        
        if filename and os.path.isfile(filename):

            (filename2, position2) = navigateToModel.filenameAndPositionTransform(filename, position)
            msg = "found: {0} {1}".format(filename2, position2)
            window = self.window
            if filename2 != filename:
                self.window.open_file(filename2)
                view = self.window.active_view()
            target_region = sublime.Region(position2, position2)
            view.sel().clear()
            view.sel().add(target_region)
            view.show(target_region)
        else:
            msg = "no such file exists on disk "+str(filename)

        print(msg)    
        sublime.status_message(msg)    