import unittest
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))

import pyOutPutParse5 as pyOutPutParse
import color

inputVar1 = "ok"
inputVar = """
Makss-Mac:~ maks$ clear

Makss-Mac:~ maks$ OUTPUT=`python3 "/Users/maks/Library/Application Support/Sublime Text 3/Packages/move_near_replace/replace_require_test.py"`
Traceback (most recent call last):
  File "/Users/maks/Library/Application Support/Sublime Text 3/Packages/move_near_replace/replace_require_test.py", line 6, in <module>
    import replace_require
  File "/Users/maks/Library/Application Support/Sublime Text 3/Packages/move_near_replace/replace_require.py", line 9, in <module>
    
"""

class Test(unittest.TestCase):
	def test_testName(self):
		out = pyOutPutParse.parse(inputVar)
		color.blue("test out")
		print(out)
	def test_filerRead(self)	:
		dataIn = ['/Users/maks/Library/Application Support/Sublime Text 3/Packages/move_near_replace/replace_require_test.py:6', '/Users/maks/Library/Application Support/Sublime Text 3/Packages/move_near_replace/replace_require.py:9']
		pyOutPutParse.writeFile(dataIn)
		dataOut = pyOutPutParse.readFile()
		color.green("dataOut")
		print(dataOut)
		expected = dataIn
		self.assertEqual (dataOut, expected)
	def test_readNext(self)	:
		dataIn = ['/file/path.iced:6', '/file-2-path.iced:8', '/file-2-path.iced:12']
		pyOutPutParse.writeFile(dataIn)
		dataOut = pyOutPutParse.read('/file-2-path.iced:8', "next")
		color.green("dataOut")
		print(dataOut)
		expected = '/file-2-path.iced:12'#'/file/path.iced:6'
		self.assertEqual (dataOut, expected) 
	def test_readNext2(self)	:
		dataIn = ['/file/path.iced:6', '/file-2-path.iced:8', '/file-2-path.iced:12']
		pyOutPutParse.writeFile(dataIn)
		dataOut = pyOutPutParse.read('/file-2-path.iced:6', "next")
		color.green("dataOut")
		print(dataOut)
		expected = '/file-2-path.iced:8'
		self.assertEqual (dataOut, expected)	
	def test_parseIced(self)	:
		inputStr = """host
undefined

module.js:340
    throw err;
          ^
Error: Cannot find module './map'
  at Function.Module._resolveFilename (module.js:338:15)
  at Function.Module._load (module.js:280:25)
  at Module.require (module.js:364:17)
  at require (module.js:380:17)
  at Object.<anonymous> (/Users/maks/Dropbox/nodeApps/call/routes/straight.iced:3:7)
  at Object.<anonymous> (/Users/maks/Dropbox/nodeApps/call/routes/straight.iced:1:1)
  at Module._compile (module.js:456:26)
  at Object.loadFile (/Users/maks/Dropbox/nodeApps/call/node_modules/iced-coffee-script/lib/coffee-script/coffee-script.js:195:19)
  at Module.load (/Users/maks/Dropbox/nodeApps/call/node_modules/iced-coffee-script/lib/coffee-script/coffee-script.js:223:36)
  at Function.Module._load (module.js:312:12)
  at Module.require (module.js:364:17)
  at require (module.js:380:17)
  at Object.<anonymous> (/Users/maks/Dropbox/nodeApps/call/server.iced:51:1)
  at Object.<anonymous> (/Users/maks/Dropbox/nodeApps/call/server.iced:1:1)
  at Module._compile (module.js:456:26)
  at Object.loadFile (/Users/maks/Dropbox/nodeApps/call/node_modules/iced-coffee-script/lib/coffee-script/coffee-script.js:195:19)
  at Module.load (/Users/maks/Dropbox/nodeApps/call/node_modules/iced-coffee-script/lib/coffee-script/coffee-script.js:223:36)
  at Function.Module._load (module.js:312:12)
  at Module.require (module.js:364:17)
  at require (module.js:380:17)
  at Object.<anonymous> (/Users/maks/Dropbox/nodeApps/call/app.js:2:1)
  at Module._compile (module.js:456:26)
  at Object.Module._extensions..js (module.js:474:10)
  at Module.load (module.js:356:32)
  at Function.Module._load (module.js:312:12)
  at Function.Module.runMain (module.js:497:10)
  at startup (node.js:119:16)
  at node.js:901:3

30 Oct 08:20:45 - [nodemon] app crashed - waiting for file changes before starting..."""

		
		result = pyOutPutParse.parseIced(inputStr)
		expected = ["/Users/maks/Dropbox/nodeApps/call/routes/straight.iced:3", 
		"/Users/maks/Dropbox/nodeApps/call/routes/straight.iced:1",
		"/Users/maks/Dropbox/nodeApps/call/server.iced:51",
		"/Users/maks/Dropbox/nodeApps/call/server.iced:1"]
		self.assertEqual (result, expected)			


if __name__ == '__main__':
	unittest.main()		
