import re
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/moveNearReplace')
import filer2
def read(self):
    view = self.window.active_view()
    filename = view.file_name()
    data = filer2.read(filename)
    return data

def windowPluginName(self):
    data = read(self)
    m = re.findall(r'class (.+)Command\(sublime_plugin', data)
    pluginName = m[0]
    return pluginName