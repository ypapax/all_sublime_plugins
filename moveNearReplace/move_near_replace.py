# Moves or simply renames files via a keyboard shortcut using python os and shutil modules.
# Configure the shortcut in the .sublime-keymap file of your choice.
# See keymap file included in this project for a reference.
# Currently, it only moves files to pre-existing directories.

import sys
import replace_require
import os
import shutil
import sublime
import sublime_plugin
import ntpath

def replacePathes (old_filename, new_filename):
    replace_require.Replace2(old_filename, new_filename)
    
class move_near_replaceCommand(sublime_plugin.WindowCommand):

    def run(self):
        view = self.window.active_view()
        filename = view.file_name()
        clip = sublime.get_clipboard()
        newPath = os.path.dirname(clip)
        filenameOnly = ntpath.basename(filename)

        newPath = os.path.join(newPath, filenameOnly)
        self.window.show_input_panel("Move/Rename with path replacing:", newPath, lambda user_input: self.rename(view, filename, user_input), None, None)

    def rename(self, view, old_filename, new_filename):
        if not self.validateFileName(view, old_filename, new_filename): 
            return
        if view.is_dirty():
            view.window().run_command("save")
        window = view.window()
        self.fileOperations(window, old_filename, new_filename)

        #put replacing here
        print("old_filename", old_filename)
        print("new_filename", new_filename)
        replacePathes (old_filename, new_filename)
        # view.close()
        # self.window.open_file(new_filename, sublime.ENCODED_POSITION)
        
        # sublime.active_window().active_view().run_command("revert")
        # view.run_command("revert")
        print("done-----with refresh-5-----------+++++++++++++++++++)))))))))))))))))))))))))))))))")
        window.run_command("close")
        window.open_file(new_filename)
        self.setSelection(view, window.active_view())

    def validateFileName(self, view, old_file, new_file):
        if len(new_file) is 0:
            sublime.error_message("Error: No new filename given.")
            return False
        if view.is_loading():
            sublime.error_message("Error: The file is still loading.")
            return False
        if view.is_read_only():
            sublime.error_message("Error: The file is read-only.")
            return False
        if(new_file == old_file):
            sublime.error_message("Error: The new file name was the same as the old one.")
            return False
        return True

    def fileOperations(self, window, old_file, new_file):
        try:
            shutil.move(old_file, new_file)
        except IOError as e:
            if e.errno == 2:  # No such file or directory (on new_file)
                new_dir = os.path.dirname(new_file)
                os.makedirs(new_dir)
                shutil.move(old_file, new_file)
            else:
                raise e
        except Exception as e:
            raise e

        if old_file.endswith(".py"):
            os.remove(old_file + "c")

        if os.access(new_file, os.R_OK):  # Can read new file
            window.run_command("close")
            window.open_file(new_file)
        else:
            sublime.error_message("Error: Can not read new file: " + new_file)

    def setSelection(self, old_view, new_view):
        new_view.sel().clear()
        new_view.sel().add_all(old_view.sel())
    def is_enabled(self):
        return True #bool(sublime.get_clipboard().strip())    