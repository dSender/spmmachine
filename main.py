from selenium import webdriver
import time
import random


proxy =    ['157.230.240.140:8080',
            '91.208.39.70:8080',
            '221.126.249.102:8080',
            '138.68.166.224:8080',
            '151.106.10.60:8080',
            '219.107.218.202:8080',
            '185.85.116.61:8080',
            '185.85.117.109:8080',
            '185.85.118.67:8080',
            '201.49.110.42:8080',
            '156.67.221.222:8080',
            '138.68.166.224:8080'
            ]

user_ = {1:'name',2:'family',3:'fa44iliee',4:'958yisavfsgv'}
crome_opt = webdriver.ChromeOptions()

def ok(phone):
    try:
        crome_opt.add_argument('--proxy-server=%s' % random.choice(proxy))
        driver = webdriver.Chrome(executable_path = '/home/tevirp/Desktop/scripts/spamer/chromedriver', chrome_options=crome_opt)
        driver.get("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone")
        driver.find_element_by_id('field_phone').clear()
        driver.find_element_by_id('field_phone').send_keys(phone)
        time.sleep(5)
        driver.find_element_by_xpath('//div[@class="form-actions mt-5x"]/input').click()
        time.sleep(3)
        driver.quit()
    except:
        pass


def yan(phone):
    try:
        crome_opt.add_argument('--proxy-server=%s' % random.choice(proxy))
        driver = webdriver.Chrome(executable_path = '/home/tevirp/Desktop/scripts/spamer/chromedriver', chrome_options=crome_opt)
        driver.get("https://passport.yandex.ru/registration/mail?from=mail&origin=home_desktop_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F")
        driver.find_element_by_id('firstname').send_keys(user_[1])
        driver.find_element_by_id('lastname').send_keys([user_[2]])
        driver.find_element_by_id('login').send_keys([user_[3]])
        driver.find_element_by_id('password').send_keys([user_[4]])
        time.sleep(5)
        driver.find_element_by_class_name('textinput__control').send_keys([user_[4]])
        driver.find_element_by_id('phone').send_keys(phone[1:])
        time.sleep(5)
        driver.find_element_by_xpath('//div[@class="registration__send-code show-block"]/button').click()
        time.sleep(3)
        driver.quit()
    except:
        pass


def inst(phone):
    try:
        crome_opt.add_argument('--proxy-server=%s' % random.choice(proxy))
        driver = webdriver.Chrome(executable_path = '/home/tevirp/Desktop/scripts/spamer/chromedriver')
        driver.get("https://www.instagram.com/?hl=ru")
        driver.find_element_by_name('emailOrPhone').send_keys(phone)
        time.sleep(1)
        driver.find_element_by_name('username').send_keys('ewbaBHvsfhjdvsadf')
        time.sleep(1)
        driver.find_element_by_name('password').send_keys('43fds35basmvcx')
        time.sleep(1)
        driver.find_elements_by_xpath('//button[@class="_0mzm- sqdOP  L3NKy       "]')[1].click()
        time.sleep(3)
        driver.quit()
    except:
        pass

def auto_ru(phone):
    try:
        crome_opt.add_argument('--proxy-server=%s' % random.choice(proxy))
        driver = webdriver.Chrome(executable_path = '/home/tevirp/Desktop/scripts/spamer/chromedriver', chrome_options=crome_opt)
        driver.get("https://auth.auto.ru/login/?r=https%3A%2F%2Fauto.ru%2F")
        driver.find_element_by_id('confirm-button').click()
        time.sleep(5)
        driver.find_element_by_class_name('TextInput__control').send_keys(phone)
        time.sleep(2)
        driver.find_element_by_xpath('//button[@class="Button Button_color_blue Button_size_l Button_type_button Button_width_default"]').click()
        time.sleep(3)
        driver.quit()
    except:
        pass








































































#
