
import unittest
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '../util'))
import color
import match
class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		result = match.iced("Object.<anonymous> (/Users/maks/Dropbox/nodeApps/call/routes/straight.iced:3:7)")
		print(result)
		self.assertEqual(result, [('/Users/maks/Dropbox/nodeApps/call/routes/straight.iced', '3')])
	def test_2(self):
		color.blue("test here baby")
		result = match.iced("""at require (module.js:380:17)
  at Object.<anonymous> (/Users/maks/Dropbox/nodeApps/call/routes/straight.iced:3:7)
  at Object.<anonymous> (/Users/maks/Dropbox/nodeApps/call/routes/straight.iced:1:1)
  at Module._compile (module.js:456:26)""")
		color.blue("result")
		print(result)
		self.assertEqual(result, [('/Users/maks/Dropbox/nodeApps/call/routes/straight.iced', '3'), ('/Users/maks/Dropbox/nodeApps/call/routes/straight.iced', '1')])	

	def test_3(self):
		color.blue("test here baby")
		result = match.iced("""Error: Cannot find module './map'
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
""")
		color.blue("result")
		print(result)
		self.assertEqual(result, [('/Users/maks/Dropbox/nodeApps/call/routes/straight.iced', '3'), ('/Users/maks/Dropbox/nodeApps/call/routes/straight.iced', '1'), ('/Users/maks/Dropbox/nodeApps/call/server.iced', '51'), ('/Users/maks/Dropbox/nodeApps/call/server.iced', '1')])	
	
if __name__ == '__main__':
	unittest.main()		
