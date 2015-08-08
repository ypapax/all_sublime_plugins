import os
import sublime, sublime_plugin

class plugin_window_nosetests_Command(sublime_plugin.WindowCommand):
    def run(self):
        # sublime.set_clipboard(absolute2)
        view = self.window.active_view()
        filename = view.file_name()
        dirName = os.path.dirname(filename)
        command = """cl "{}" && python3 -m nose""".format(dirName)
        toClip = command
        sublime.set_clipboard(toClip)
        sublime.status_message("set to clipboard: "+toClip)


