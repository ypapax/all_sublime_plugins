import absRel3 as absRel

import unittest

class Test(unittest.TestCase):
	def test_Abs(self):
		# self.failUnlessEqual(1 + 1, 2)
		print("oke doke")
		absolute = absRel.Abs('/a/b/c/d.js', '../../e.js')
		print('result absolute', absolute)
		self.assertEqual (absolute, '/a/e.js')
	def test_Rel(self):
		rel = absRel.Rel('/a/b/c/d.js', '/a/b/e.js')
		self.assertEqual (rel, '../e.js')	
	def test_Rel2(self):
		rel = absRel.Rel('/Users/maks/Dropbox/nodeApps/call/routes/straight.iced', '/Users/maks/Dropbox/nodeApps/call/routes/map/map.iced')
		self.assertEqual (rel, './map/map.iced')	
	def test_Rel_near(self):
		rel = absRel.Rel('/a/b/d.js', '/a/b/e.js')
		self.assertEqual (rel, './e.js')	
	def test_Rel_To_Rel(self):
		result = absRel.RelToRel('/a/b/c/d.js', '/a/b/d.js', '../f.js')
		self.assertEqual (result, './f.js')	
	def test_Rel_onSelf(self):
		result = absRel.Rel('/a/b/c/d.js', '/a/b/c/d.js')
		self.assertEqual (result, './d.js')		
	def test_AbsAddExtension(self):
		result = absRel.AbsAddExtension('/a/b/c/d.iced', '../../e')
		self.assertEqual (result, '/a/e.iced')		
		

if __name__ == '__main__':
	unittest.main()			

# 	target: /Users/maks/Dropbox/nodeApps/call/routes/map/map.iced -----------------------------------------------------
# source: /Users/maks/Dropbox/nodeApps/call/routes/straight.iced