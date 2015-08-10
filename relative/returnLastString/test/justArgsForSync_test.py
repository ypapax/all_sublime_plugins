import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/relative/returnLastString')
import color
import assertMy
import returnLast

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		fileContent = """create = require 'selWebDriver/create.iced'
fullUrl = require '../../fullUrl.iced'
admin = require '../../routes/admin.iced'

module.exports = ()->
	[driver, webdriver] = create()
	url = fullUrl "/"
    driver.get url
    driver.findElement(webdriver.By.name('login')).sendKeys admin.login
    driver.findElement(webdriver.By.name('pass')).sendKeys admin.pass
    driver.findElement(webdriver.By.id('loginBtn')).click();

    return [driver, webdriver]

	"""
		result = returnLast.justArgsForSync(fileContent)
		expected = "[driver, webdriver]"
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()