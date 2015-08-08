
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/foGo')
import modelCopyMethoUsageGo
        

import sublime, sublime_plugin

class copy_method_usage_to_clip_go_Command(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        filename = view.file_name()
        
        view = self.window.active_view()
        region1 = view.sel()[0]
        position = region1.a

        # get method usage 
        # and put it to clipboard
        funcUsage = modelCopyMethoUsageGo.main_getFuncUsageByFileNameAndPosition(filename, position)
        sublime.set_clipboard(funcUsage)
        sublime.status_message("set to clipboard: "+funcUsage)
        
        
