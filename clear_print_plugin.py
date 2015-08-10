import sublime, sublime_plugin
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, 'clear'))
sys.path.insert(0, os.path.join(currentFolder, 'beatyFormatting'))
import clearModel
import beatyModel
class plugin_window_clear_Command(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        filename = view.file_name()
        clearModel.pyFile(filename)
        beatyModel.pyFileFull(filename)