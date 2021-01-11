import sys, os
sys.path.append(os.path.abspath('../AutomationModule'))
from automation_init import AutomationInit
automation = AutomationInit()
automation.chrome()
#automation.firefox()
#automation.safari()
browser = automation.getBrowser()
automation.login()
browser.save_screenshot("/Users/ishratmanzoor/Desktop/QA.Automation/Screenshots/Login.png")
browser.implicitly_wait(10)

automation.delay()
browser.close()

