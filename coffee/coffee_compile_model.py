import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '../util'))
sys.path.insert(0, os.path.join(currentFolder, '../clipToFile'))
import bash
import color
import subprocess        

def coffeeCompile(filename):
    bashCommand = 'coffee -cb "{}"'.format(filename)
    color.red("bashCommand")
    print(bashCommand)


      
 #    process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE)
 #    output = process.communicate()[0]

 #    import subprocess
    # subprocess.Popen(bashCommand)
    bash.run_script(bashCommand)