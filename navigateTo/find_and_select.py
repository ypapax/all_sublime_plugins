import sublime, sublime_plugin
     
    
class find_and_select_Command(sublime_plugin.WindowCommand):
    def run(self, target=""):
        
        
        if not target or target == "":
            target = sublime.get_clipboard()
        window = self.window
        view = window.active_view()
        content = view.substr(sublime.Region(0, view.size()))
        begin = content.find(target)
        if begin == -1:
            return
        end = begin + len(target)
        target_region = sublime.Region(begin, end)
        view.sel().clear()
        view.sel().add(target_region)
        view.show(target_region)