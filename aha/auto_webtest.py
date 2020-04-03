from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

"""
打开谷歌浏览器
进入url指定页面
"""
browser = webdriver.Chrome()
url = r'http://dev.test.ustax.com.cn:9000/?fromurl=http://dev.test.ustax.com.cn:9001/#/'
browser.get(url)
browser.maximize_window()  # 浏览器最大化命令
# browser.find_element_by_css_selector('input[placeholder=登录名]').clear()    # 清空账号数据
# browser.find_element_by_css_selector('input[placeholder=登录名]').send_keys('17585571190')
logInNameInput = browser.find_element_by_css_selector('input[placeholder=登录名]')  # 获取用户名输入框元素
logInNameInput.clear()
logInNameInput.send_keys('17585571191')

logInPwdInput = browser.find_element_by_css_selector('input[placeholder=密码]')     # 获取密码输入框元素
logInPwdInput.clear()
ActionChains(browser).context_click(logInPwdInput).perform()
'''
logInPwdInput.send_keys('1qaz2wsx3edc')
browser.find_element_by_css_selector('button[type=button]').click()
'''
# browser.find_element_by_css_selector('button[type=button]').submit()
# browser.set_window_size(480, 800)  #设置浏览器宽480、高800
# browser.back()  # 浏览器后退按钮
# browser.forward()  # 浏览器前进按钮
'''
<input type = "text" autocomplete = "off" placeholder = "登录名" class ="el-input__inner" >

< input type = "password" autocomplete = "off" placeholder = "密码 " class ="el-input__inner" >


// *[ @ id = "app"] / div / div / div[1] / div / div[2] / div[1] / form / div[1] / div / div / input
'''