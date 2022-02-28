from selenium import webdriver
import moodle_locators as locators
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import datetime
import sys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

# from selenium.webdriver.common.keys import Keys
from faker import Faker
fake = Faker(locale='en_CA')




options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions.key_actions import KeyActions


# Moodle Test Automation Plan
# Launch Moodle App website - validate we are on the home page.
# navigate to Login screen - validate we are on the login page
# login = validate we are on the Dashboard page
# navigate to Add new user page - validate
# populate the new user form using Faker fake data
# submit the form - validate
# search for new user - validate
# logout
# login with new user credentials - validate
# logout
# login back with admin account
# search for a new user
# delete new user.

# ------------------Locators Section-------------------

# ------------------------------------------------------

# commented the following 2 lines for lab 3 assignment
# s = Service(executable_path='C:\\Tools\\chromedriver.exe')
# driver = webdriver.Chrome(service=s)


def setUp():
    print(f'Launch {locators.app} App')
    print('--------------------~*~--------------------')
    # Make browser full screen
    driver.maximize_window()
    # Give browser up to 30 seconds to respond
    driver.implicitly_wait(30)
    # Navigate to Moodle app website
    driver.get(locators.url)
    # Check that Moodle URL and the home page title are displayed
    if driver.current_url == locators.url and driver.title == locators.moodle_homepage_title:
        print(f'Yey! {locators.app} Launched Successfully')
        print(f'{locators.app} homepage URL: {driver.current_url}\nHome Page Title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.app}  did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page Title: {driver.title}')


def teardown():
    if driver is not None:
        print('----------------------------')
        print(f'The test is Completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


# Login to moodle
def login(username, password):
    print(f'{driver.current_url} and {locators.url}')
    if driver.current_url == locators.url:
        driver.find_element(By.LINK_TEXT, 'Log in').click()
        # if driver.current_url == 'http://52.39.5.126/login/index.php':
        if driver.current_url == locators.moodle_login_page_url:
            print('Clicked Login button successfully')
            sleep(0.25)
            driver.find_element(By.ID, 'username').send_keys(username)
            sleep(0.25)
            driver.find_element(By.ID, 'password').send_keys(password)
            driver.find_element(By.ID, 'loginbtn').click()
            # driver.find_element(By.ID, 'loginbtn')
            print(f'Login is successful with userid {username}')
            # validate we are at Dashboard
            # if driver.title == 'Dashboard' and driver.current_url == 'http://52.39.5.126/my/':
            if driver.title == 'Dashboard' and driver.current_url == locators.moodle_dashboard_url:
                assert driver.current_url == locators.moodle_dashboard_url
                assert driver.title == 'Dashboard'
                print(f'Login successful. Moodle Dashboard is displayed - Page title: {driver.title}')
            else:
                print(f'Dashboard is not displayed. Check your code and try again')


# 2. Maximize the browser window.

    driver.maximize_window()

# 3. Navigate to the Google Canada website and check that this page has Google in the title and https://www.google.ca/  as the current URL.

# driver.get(locators.url)

# 4. If yes, display a user-friendly message about successful landing and correct title.
# Use condition to check URL and the Title.
# if driver.current_url == locators.url and driver.title == 'Software Quality Assurance Testing':
#     # print('Successfully launched Google Canada website')
#     print('Successfully launched Moodle website')
# else:
#     print('Moodle didn\'t launch successfully')
#     print(f'Current URL: {driver.current_url}, page Title: {driver.title}')
#     teardown()

# navigate to Add new user page - validate


def log_out():
    driver.find_element(By.CLASS_NAME, 'userpicture').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//span[contains(., "Log out")]').click()
    sleep(0.25)
    # validate logout successful
    if driver.current_url == locators.url:
        print(f'Logout successful {datetime.datetime.now()}')
    else:
        print(f'{driver.current_url}: Else loop')


def create_new_user():
    driver.find_element(By.XPATH, '// span[text() = "Site administration"]').click()
    print('\nSuccessfully clicked on Site Administration Tab on Left Panel')
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Add a new user').click()
    assert driver.find_element(By.LINK_TEXT, 'Add a new user').is_displayed()
    print(f'Navigate to add new user page: - Page Title {driver.title}')

    driver.find_element(By.ID, 'id_username').send_keys(locators.new_username)
    # driver.find_element(By.XPATH,'//em[contains(text(),"Click to enter text")]').send_keys(password)
    driver.find_element(By.LINK_TEXT, 'Click to enter text').click()
    driver.find_element(By.ID, 'id_newpassword').send_keys(locators.new_password)
    driver.find_element(By.ID, 'id_firstname').send_keys(locators.first_name)
    driver.find_element(By.ID, 'id_lastname').send_keys(locators.last_name)
    driver.find_element(By.ID, 'id_email').send_keys(locators.email)

    Select(driver.find_element(By.ID, 'id_maildisplay')).select_by_visible_text('Allow everyone to see my email address')
    sleep(0.25)
    driver.find_element(By.ID, 'id_moodlenetprofile').send_keys(locators.moodle_add_new_user_profile)
    driver.find_element(By.ID, 'id_city').send_keys('Vancouver')
    Select(driver.find_element(By.ID, 'id_country')).select_by_visible_text('Canada')
    Select(driver.find_element(By.ID, 'id_timezone')).select_by_visible_text('America/Vancouver')
    driver.find_element(By.ID,  'id_description_editoreditable').clear()
    driver.find_element(By.ID, 'id_description_editoreditable').send_keys(locators.description)
    # Select(driver.find_element(By.ID,'id_lang'))
    # driver.find_element(By.ID,'id_moodle_additional_names').click()
    # upload a picture
    # click arrow element
    driver.find_element(By.CLASS_NAME, 'dndupload-arrow').click()
    sleep(0.50)
    # driver.find_element(By.LINK_TEXT,'Server files').click()
    # sleep(0.25)
    # driver.find_element(By.LINK_TEXT, 'sl_Frozen').click()
    # sleep(0.50)
    # driver.find_element(By.LINK_TEXT,'sl_How to build a snowman').click()
    # sleep(0.25)
    # driver.find_element(By.LINK_TEXT, 'Course image').click()
    # sleep(0.50)
    # driver.find_element(By.LINK_TEXT, 'gieEd4R5T.png').click()
    img_path = ['Server files', 'sl_Frozen', 'sl_How to build a snowman', 'Course image', 'gieEd4R5T.png']
    for p in img_path:
        driver.find_element(By.LINK_TEXT, p).click()
        sleep(0.25)

    # Select a radio button here
    # driver.find_element(By.XPATH,'//input[@value="4"]').click()
    driver.find_element(By.XPATH, '//label[contains(.,"Create an alias/shortcut to the file")]').click()
    driver.find_element(By.XPATH, '//button[contains(.,"Select this file")]').click()
    sleep(0.25)
    # sleep(0.25)
    driver.find_element(By.ID, 'id_imagealt').send_keys(locators.pic_description)
    sleep(0.25)

    # populate Additional Name
    driver.find_element(By.LINK_TEXT, 'Additional names').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_firstnamephonetic').send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_lastnamephonetic').send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_middlename').send_keys(locators.middle_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_alternatename').send_keys(locators.first_name)
    sleep(0.25)

    # populate Interest
    driver.find_element(By.LINK_TEXT, 'Interests').click()
    for tag in locators.list_of_interests:
        # Method1
        # driver.find_element(By.XPATH,'//input[contains(@id,"form_autocomplete_input")]').send_keys(tag + Keys.ENTER)
        driver.find_element(By.XPATH, '//input[contains(@id,"form_autocomplete_input")]').send_keys(tag + '\n')
        # method 2
        sleep(0.25)
        # print(locators.list_of_interests)
        # driver.find_element(By.XPATH, '//input[contains(@id,"form_autocomplete_input")]').send_keys(Keys.ENTER)
        # sleep(0.25)
        # Method 3

    driver.find_element(By.LINK_TEXT, 'Optional').click()
    opt, ids, val = locators.list_opt, locators.list_ids, locators.list_val
    sleep(0.25)
    for i in range(len(locators.list_opt)):
        opt, ids, val = locators.list_opt[i], locators.list_ids[i], locators.list_val[i]
        # print(f'Populate {opt}')
        driver.find_element(By.ID, ids).send_keys(val)
        sleep(0.25)

########################################
    # Press Submit button
    driver.find_element(By.ID, 'id_submitbutton').click()
    sleep(0.25)
    print(f'------ New User "{locators.new_username}/{locators.new_password}, {locators.email}" is added --------')
#######################################

    # breakpoint()


def search_user():
    # check we are on the user;s Main Page
    if driver.current_url == locators.moodle_users_main_page:
        assert driver.find_element(By.LINK_TEXT, 'Browse list of users').is_displayed()
        print('\'Browse list of users page\'is displayed')
        sleep(0.25)
        # check we can search user by email
        print(f'----------Search for user by email address: {locators.email}')
        driver.find_element(By.CSS_SELECTOR, 'input#id_email').send_keys(locators.email)
        sleep(0.25)
        driver.find_element(By.CSS_SELECTOR, 'input#id_addfilter').click()
        if driver.find_element(By.XPATH, f'//td[contains(.,"{locators.email}")]'):
            print(f'---User: {locators.email} is found')
        # breakpoint()
        # driver.find_element(By.CSS_SELECTOR,'input[id="id_addfilter"]')


def check_new_user_can_login():
    print('inside check_new_user_can_login()')
    if driver.title == locators.moodle_dashboard_title and driver.current_url == locators.moodle_dashboard_url:
        print('Inside first if check_new_user_can_login()')
        # if driver.find_element(By.XPATH,f'//span[contains(.,"{locators.full_name}")]').is_displayed():
        if driver.find_element(By.XPATH, f'//span[contains(.,"{locators.full_name}")]').is_displayed():
            print('Inside second if check_new_user_can_login()')
            print(f'User with full name is displayed {locators.full_name}')
            logger('created')

# delete user method


def delete_user():
    driver.find_element(By.XPATH, '// span[text() = "Site administration"]').click()
    print('\nSuccessfully clicked on Site Administration Tab on Left Panel')
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    driver.find_element(By.LINK_TEXT, 'Browse list of users').click()
    sleep(0.25)

    search_user()
    driver.find_element(By.XPATH, '//i[@title="Delete"]').click()
    driver.find_element(By.XPATH, '//button[contains(.,"Delete")]').click()
    print('Delete Successful')
    # logger(f'User Deleted at {datetime.datetime.now()}')
    logger('Deleted')
    # breakpoint()


def logger(action):
    # create variable to store the file content
    old_instance = sys.stdout
    log_file = open('message.log', 'a')  # open log file and append a record
    sys.stdout = log_file
    print(f'{locators.email}\t'
          f'{locators.new_username}\t'
          f'{locators.new_password}\t'
          f'{datetime.datetime.now()}\t'
          f'{action}')
    sys.stdout = old_instance
    log_file.close()


# setUp()
# # ------ CREATE NEW USER -------------
# login(locators.admin_user_name, locators.admin_password) # LOGIN AS ADMIN
# create_new_user()
# search_user()
# log_out()
# #-------------------------------------
# # -------- LOGIN AS NEW USER -----------------
# login(locators.new_username, locators.new_password)
# check_new_user_can_login()
# #logger('created')
# log_out()
# # --------------------------------------------
# # ---------- DELETE NEW USER -----------------
# login(locators.admin_user_name, locators.admin_password)
# delete_user() # delete new user function call goes here
# log_out()
# # --------------------------------------------
# teardown()
