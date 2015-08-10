create = require 'selWebDriver/create.iced'
fullUrl = require '../../fullUrl.iced'
admin = require '../../routes/admin.iced'

module.exports = ()=>
	[driver, webdriver] = create()
	url = fullUrl "/"
    driver.get url
    driver.findElement(webdriver.By.name('login')).sendKeys admin.login
    driver.findElement(webdriver.By.name('pass')).sendKeys admin.pass
    driver.findElement(webdriver.By.id('loginBtn')).click();

    return [driver, webdriver]

	