import unittest
import sys

import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
import bash


class Test(unittest.TestCase):
	def test_ls(self):
		(out, err) = bash.run_script("echo 'Hello'")
		self.assertEqual(out, b'Hello\n')
		print (out)

if __name__ == '__main__':
	unittest.main()		