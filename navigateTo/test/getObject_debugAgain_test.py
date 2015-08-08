
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
import pyFind
import navigateToModel

import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
import color

inputText = """import os
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/findUsages')
import reactOnCursorPosition
        

import sublime, sublime_plugin

class plugin_window_find_usages_plugin_Command(sublime_plugin.WindowCommand):
    def run(self,  obj="usages", command="find"):
        view = self.window.active_view()
        region1 = view.sel()[0]
        position = region1.a
        view = self.window.active_view()
        filename = view.file_name()
        
        if filename and os.path.isfile(filename):
            
            (filename2, position2, status) = reactOnCursorPosition.starter(filename, position, obj, command)
            window = self.window
            if filename2 != filename:
                self.window.open_file(filename2)
                view = self.window.active_view()
            target_region = sublime.Region(position2, position2)
            view.sel().clear()
            view.sel().add(target_region)
            view.show(target_region)
            print(status)
            sublime.status_message(status)

        else:

            sublime.status_message("no such file exists on disk "+str(filename))
        
"""



class Test(unittest.TestCase):
    
    def test_bigFile(self):
        color.blue("test here baby")
        

        expected = ['reactOnCursorPosition', 'starter']
        
        position = 638

        result = navigateToModel.getObject(inputText, position)
        color.red('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('result')
        print(repr(result))
        color.red('*****************************************************************')

        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()     
