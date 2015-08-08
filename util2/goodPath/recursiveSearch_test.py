
import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
import color
import recursiveSearch_model

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		result = recursiveSearch_model.find_files('/Users/maks/Library/Application Support/Sublime Text 3/Packages/goodPath/forTest/a', 'package.json')
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		# for i in result:
		self.assertEqual(result, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/goodPath/forTest/a/package.json')
			# print (i)
	def test_noExt(self):
		color.blue("test here baby")
		result = recursiveSearch_model.find_files('/Users/maks/Library/Application Support/Sublime Text 3/Packages/goodPath/forTest/a', 'package')
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		# for i in result:
		self.assertEqual(result, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/goodPath/forTest/a/package.json')
	def test_getAllFiles(self):
		color.blue("test here baby")
		result = recursiveSearch_model.getAllFiles('/Users/maks/Library/Application Support/Sublime Text 3/Packages/goodPath/forTest')
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		print(result)
		expected = ['/Users/maks/Library/Application Support/Sublime Text 3/Packages/goodPath/forTest/a/package.json', '/Users/maks/Library/Application Support/Sublime Text 3/Packages/goodPath/forTest/a/b/c_start.js', '/Users/maks/Library/Application Support/Sublime Text 3/Packages/goodPath/forTest/a/b/e.iced', '/Users/maks/Library/Application Support/Sublime Text 3/Packages/goodPath/forTest/a/b/c/test.iced', '/Users/maks/Library/Application Support/Sublime Text 3/Packages/goodPath/forTest/a/b/c/testForWrite.iced', '/Users/maks/Library/Application Support/Sublime Text 3/Packages/goodPath/forTest/a/b/c/k/f.iced']
		self.assertEqual(result, expected)
	def test_getAllFiles_byFileName(self):
		color.blue("test here baby")
		result = recursiveSearch_model.getAllFiles('/Users/maks/Library/Application Support/Sublime Text 3/Packages/goodPath/forTest/a.js')
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		print(result)
		expected = ['/Users/maks/Library/Application Support/Sublime Text 3/Packages/goodPath/forTest/a/package.json', '/Users/maks/Library/Application Support/Sublime Text 3/Packages/goodPath/forTest/a/b/c_start.js', '/Users/maks/Library/Application Support/Sublime Text 3/Packages/goodPath/forTest/a/b/e.iced', '/Users/maks/Library/Application Support/Sublime Text 3/Packages/goodPath/forTest/a/b/c/test.iced', '/Users/maks/Library/Application Support/Sublime Text 3/Packages/goodPath/forTest/a/b/c/testForWrite.iced', '/Users/maks/Library/Application Support/Sublime Text 3/Packages/goodPath/forTest/a/b/c/k/f.iced']
		self.assertEqual(result, expected)	
		
if __name__ == '__main__':
	unittest.main()		
