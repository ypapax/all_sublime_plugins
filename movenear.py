# Moves or simply renames files via a keyboard shortcut using python os and shutil modules.

import os
import shutil
import sublime
import sublime_plugin
import ntpath


class MovenearCommand(sublime_plugin.WindowCommand):

    def run(self):
        # get current view
        view = self.window.active_view()
        # get current filename
        filename = view.file_name()
        # read clipboard
        clip = sublime.get_clipboard()

        # check if we have full path in clipboard
        clipGotFullPath = clip[0] == '/'
        if (clipGotFullPath):
            newPath = os.path.dirname(clip)
            filenameOnly = ntpath.basename(filename)

            newPath = os.path.join(newPath, filenameOnly)
        else:
            newPath = filename

        # show move rename input
        self.window.show_input_panel("Move/Rename:", newPath, lambda user_input: self.rename(view, filename, user_input), None, None)

    def rename(self, view, old_filename, new_filename):
        if not self.validateFileName(view, old_filename, new_filename):
            return
        if view.is_dirty():
            view.window().run_command("save")
        window = view.window()
        # make movement:
        self.fileOperations(window, old_filename, new_filename)
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
            # moving file
            shutil.move(old_file, new_file)
            self.window.run_command("close")
            self.window.open_file(new_file)  
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