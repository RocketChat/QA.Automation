from automation_init import AutomationInit
automation = AutomationInit()
#automation.chrome()
automation.firefox()
#automation.safari()
browser = automation.getBrowser()
automation.login()
browser.implicitly_wait(10)

automation.delay()
browser.close()

