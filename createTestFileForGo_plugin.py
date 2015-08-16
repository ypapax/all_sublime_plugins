import sys
import generateTestFileNameForGoTest
import sublime, sublime_plugin

class create_go_testCommand(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        filename = view.file_name()
        
        view = self.window.active_view()
        region1 = view.sel()[0]
        position = region1.a

        testFile = generateTestFileNameForGoTest.createFromPosition(filename, position)
        self.window.open_file(testFile)

        
        
