import bash
import unittest


class Test(unittest.TestCase):
	def test_ls(self):
		(out, err) = bash.run_script("echo 'Hello'")
		self.assertEqual(out, b'Hello\n')
		print (out)

if __name__ == '__main__':
	unittest.main()		