import sublime, sublime_plugin, os.path

class CopyrelCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        relative = sublime.get_clipboard()
        
        
        absolute1 = ""


        
        absolute1 = self.active_window().view.file_name()
        print("self.window.project().fileName()")
        print(self.window.project().fileName())
        # print("absolute1")
        # print(absolute1)

        absolute2 = os.path.normpath(os.path.join(os.path.dirname(absolute1), relative))
        sublime.set_clipboard(absolute2)




