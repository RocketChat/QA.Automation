# QA.Automation
**Title**: QA.Automation\
**OverView**: It consists of automated end to end Regression test scripts for all the basic functionalities in 
Rocket.chat, written in Selenium webdriver with Python. The purpose of QA Regression is to ensure that the entire system 
works flawlessly after any code change.

The test scripts allows cross browser testing
with all the test cases to be executed on most popular browsers: Chrome, Firefox, Safari, and IE.\
The project also supports running Selenium Webdriver tests with Python on BrowserStack.\
 The test reports can be generated with
HTML and Allure plugins.\
**Features**: 
1. Login to Rocket.chat with Username and Password 
2. Create New User 
3. Create New DM
4. Create New Channel
5. Add users to a Channel
6. Create Discussion
7. Post Message in a Private channel
8. Post Message in a Public channel
9. Post an emoji
10. Perform Favorite-Unfavorite action in a channel
11. Perform Read-Unread action in a channel
12. Perform Hide-Show action in a channel
13. Perform Leave-Join action in a channel
14. Perform Favorite-Unfavorite action in a DM
11. Perform Read-Unread action in a DM
12. Perform Hide-Show action in a DM
13. Add quote
14. Add Reaction
15. Reply in thread
16. Search User
17. Search Public Channel
18. Search Private Channel
19. View Extended-Mode
20. View Medium-Mode
21. View Condensed-Mode
22. Logout Rocket.chat
    
**Dependencies**
1. Download and Install Python 3.9 from the official link-  [https://www.python.org/downloads/]
   
2. Check python and pip is installed successfully\
   `python --version`\
   `pip --version`
   
3. Set Environment Variable for Python.
   
4. Install selenium libraries\
   `pip install -U selenium`
   
5. Download PyCharm - community edition
   [https://www.jetbrains.com/pycharm/]
   
6. Download Chrome, Firefox and IE drivers.
    [https://www.selenium.dev/downloads/]
   
On Windows unzip and paste the driver under Scripts folder in python
On Mac, go to path "/usr/local/bin" and paste the unzipped driver.

7. Install Pytest: On terminal, run below command\
    `pip install pytest`
   
8. Install allure: \
    Windows: `scoop install allure`\
    Mac: `brew install allure`
   
9. Install html Report:\
    `pip install pytest-html`

10. Pycharm Installations - Go to Python Interpreter on pycharm and install below plugins:
    1. allure-pytest
    2. pytest-html
    3. browserstack-local
    
11. For Parallel Mode - run below command in terminal: \
    `pip install pytest-xdist`
    
    To execute tests:\
    `pytest filename.py -v -s -n 2` \
    (Give any value for n e.g n 2 will open two tabs simultaneously)
    
**Running the Project**\
    `git clone https://github.com/RocketChat/QA.Automation.git` \
    `cd QA.Automation`

**To run all the Test cases use below commands:**\
    1. `pytest Tests`\
    2. `pytest -v -s Tests`\
    3. `py.test -v -s Tests`

**To run a single Test case use below commands:**\
    1. `pytest Tests/filename.py`\
    2. `pytest -v -s Tests/filename.py`\
    3. `py.test -v -s Tests/filename.py`

**To generate html report in test execution use below command**\
    1. `Pytest -v -s —html = report.html filename.py`
 
**To generate allure report in test execution use below command**  
    1. `pytest -v -s --alluredir="<path of the folder>" Tests/filename.py`\
    Here path is : "./reports/allure_reports"

**View html reports in a browser**\
    In pycharm, copy path of report.html file and paste in the browser or directly open the report.html
    file in pycharm and click on the browser icon to view the reports.

**View allure reports in a browser**\
    Copy the path of the allure_reports folder generated after the test execution in the pycharm. 
    Now go to the terminal and run below command:\
    `allure serve <path of the folder>`

**Browserstack Testing**\
    Follow Browserstack documentation here: [https://www.browserstack.com/docs/]


   