from pickle import PROTO

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import ddddocr
from colorama import Fore, Back, Style
from colorama import init;
from sympy.codegen import Print

init()
from colorama import Fore, init; init()
import os
import random

sao = []
with open('_internal\saohua.txt','r', encoding='utf-8') as f:
    content = f.read()
    elements = content.split('+')
    for element in elements:
        sao.append(element.strip())###读取小骚话的库


array = []
with open('_internal\shouhuo.txt','r', encoding='utf-8') as f:
    content = f.read()
    elements = content.split('；')
    for element in elements:
        array.append(element.strip())###读取每日收获的库
kunhuo = []
with open('_internal\kunhuo.txt','r', encoding='utf-8') as f:
    content = f.read()
    elements = content.split('；')
    for element in elements:
        kunhuo.append(element.strip())###读取每日困惑的库
mtjh = []
with open('_internal\mtjihua.txt','r', encoding='utf-8') as f:
    content = f.read()
    elements = content.split('；')
    for element in elements:
        mtjh.append(element.strip())###读取明天计划的库





def menu1():
    print('---------------------------------------------------------------------------')
    print(Fore.GREEN + "欢迎使用")
    print(Fore.RED+"1. 进入自动打卡程序(请确保你的库里已经预存数据 否则会输出空格导致签到失败)")
    print('2，查看预设库')
    print('3,修改预设库')
    print("4. 返回上级菜单（如果有）或退出")
    choice = input(Fore.YELLOW+"请选择对应数字：")
    print(Fore.GREEN+'----------------------------------------------------')
    if choice == '1':
        menu4()
    elif choice=='2':
        menu2()
    elif choice=='3':
        menu3()
    elif choice == '4':
        # 如果这是顶级菜单，可能直接退出程序或执行其他操作
        print("退出程序或返回上级菜单的操作（根据实际情况实现）")
        return
    else:
        print("无效选择，请重新输入。")
        menu1()
def menu2():
    array = []
    with open('_internal\shouhuo.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        elements = content.split('；')
        for element in elements:
            array.append(element.strip())  ###读取每日收获的库
    kunhuo = []
    with open('_internal\kunhuo.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        elements = content.split('；')
        for element in elements:
            kunhuo.append(element.strip())  ###读取每日困惑的库
    mtjh = []
    with open('_internal\mtjihua.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        elements = content.split('；')
        for element in elements:
            mtjh.append(element.strip())  ###读取明天计划的库
    print('这是每日收获的库',array)
    print('这是每日困惑的库',kunhuo)
    print('这是明天计划的库',mtjh)
    print(input('回车以继续'))
    print('----------------------------------------------------------------------------------')
    menu1()

def menu3():

    def enen1():
        print(Fore.GREEN + "1.修改每天收获")
        print("2. 修改每日困惑")
        print('3，修改明天计划')
        print("4. 返回上级菜单（如果有）或退出")
        choice = input(Fore.YELLOW+"请选择：")

        if choice == '1':
            array_str = input("请输入中文数组内容，逗号分隔：")
            array = [item.strip() for item in array_str.split('；')]

            # 将数组内容写入文件
            with open('shouhuo.txt', 'w', encoding='utf-8') as f:
                for item in array:
                    f.write(item + '\n')
            print(Fore.GREEN+'保存成功并返回首页')
            menu3()

        elif choice == '2':
            array_str = input(Fore.YELLOW+"请输入中文数组内容，逗号分隔：")
            array = [item.strip() for item in array_str.split('；')]

            # 将数组内容写入文件
            with open('kunhuo.txt', 'w', encoding='utf-8') as f:
                for item in array:
                    f.write(item + '\n')
            print('保存成功并返回首页')
            menu3()
        elif choice == '3':
            array_str = input(Fore.YELLOW+"请输入中文数组内容，逗号分隔：")
            array = [item.strip() for item in array_str.split('；')]

            # 将数组内容写入文件
            with open('mtjihua.txt', 'w', encoding='utf-8') as f:
                for item in array:
                    f.write(item + '\n')
            print('保存成功并返回首页')
            menu3()
        elif choice == '4':
            # 如果这是顶级菜单，可能直接退出程序或执行其他操作
            print("退出程序或返回上级菜单的操作（根据实际情况实现）")
            menu1()
        else:
            print("无效选择，请重新输入。")
            menu1()


    enen1()

def menu4():
          print(Fore.GREEN+"正在准备.........................................................................")

          print(Fore.RED+'欢迎使用神鹰哥牌自动打卡................')
          print('由于使用的是第三方运行库，谨慎相信下列网址')

          print("请确保你已经下载python以及必要解释器，谷歌浏览器最新版本 否则代码无法运行！！！！！！！！（炒鸡重要） ")
          print("代码绒乱，第一次写 有问题联系企鹅号2464573162")
          print('运维：208吊毛们')
          print('请确保你的库中已经设置了填入的参数')
          while True:
           i=input(Fore.BLUE + "输入账号(请正确填写)")
           o=input("输入密码（正确填写）")
           print(input('请再次确保你提前预存了数据，回车以继续'))
           while True:

             ocr = ddddocr.DdddOcr()

             options = webdriver.ChromeOptions()
             options.add_experimental_option('excludeSwitches', ['enable-logging']) # for ignore warning and error
             driver = webdriver.Chrome(options=options)
             driver.implicitly_wait(4)
             driver.get('http://223.15.246.118:9003/zhxy-app/pages/tabs/home/home')

             time.sleep(2) # 这里出现captcha时间有点长，等待2秒
             driver.maximize_window()
             driver.refresh()


    # 获取元素展示内容为图片数据
             driver.find_element(By.CLASS_NAME, 'uni-input-input').send_keys(i)
             element = driver.find_element(By.XPATH,"//input[@type='password' and @maxlength='140' and @enterkeyhint='done' and @autocomplete='off' and @class='uni-input-input']").send_keys(o)
             time.sleep(1)

             element = driver.find_element(By.XPATH,"/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-view[1]/uni-view[1]/uni-view/uni-text").click()
             pngData = driver.find_element(By.XPATH,'/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[1]/uni-view/uni-view[3]/uni-view/uni-view[2]/uni-view/uni-view[2]/uni-view/uni-image/img').screenshot_as_png
             res = ocr.classification(pngData)
             print('验证码是', res)

             element = driver.find_element(By.XPATH,"/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[1]/uni-view/uni-view[3]/uni-view/uni-view[2]/uni-view/uni-view[1]/uni-view/uni-input/div/input").send_keys(res)
             time.sleep(4)
             element = driver.find_element(By.XPATH,"/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-button").click()
             time.sleep(1)
             if "登录失败" in driver.page_source or "账号或密码错误" in driver.page_source:
               driver.quit()
               print(Fore.RED+'--------------------------------------------------------------------------------------------------------------------------------')
               print('账号密码错误 请重新输入')
               i=input(Fore.BLUE+'输入账号')
               o=input('输入密码')
               print(Fore.GREEN+'输入成功，正在准备重新登录，运行可能会过慢，清耐心等待')
               retry=True
               continue
             time.sleep(2)

             element = driver.find_element(By.XPATH,"/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[1]/uni-view[1]/uni-view[2]/uni-view[1]").click()
             time.sleep(1)
             element_locator = (By.XPATH,"/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[5]/uni-view/uni-input/div/input")
             try:
               element = driver.find_element(By.XPATH,"/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[5]/uni-view/uni-input/div/input").send_keys("东校区")
               time.sleep(1)
               random_data = random.choice(array)
               element = driver.find_element(By.XPATH,"/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[6]/uni-view[2]/uni-view/uni-textarea/div/textarea").send_keys(random_data)
               time.sleep(1)
               jtkh=random.choice(kunhuo)
               element = driver.find_element(By.XPATH,"/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[7]/uni-view[2]/uni-view/uni-textarea/div/textarea").send_keys(jtkh)
               time.sleep(1)
               mrjh= random.choice(mtjh)
               element = driver.find_element(By.XPATH,"/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[8]/uni-view[2]/uni-view/uni-textarea/div/textarea").send_keys(mrjh)
               time.sleep(2)
               element=driver.find_element(By.XPATH,'/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[9]/uni-button').click()
               print("运行完成，已经成功运行,下次运行将在24小时后")
               print('每日小骚话：')
               saohua= random.choice(sao)
               print(Fore.YELLOW+saohua)

               driver.quit()
               time.sleep(86400)
             except:
                 print(Fore.RED+'检测到你已经完成了千天向上，默认程序执行完成 将在24小时后再次尝试执行')
                 print(Fore.GREEN+'每日小骚话:')
                 saohua = random.choice(sao)
                 print(Fore.YELLOW+saohua)
                 print('--------------------------------------------------------------------')
                 driver.quit()
                 time.sleep(86400)
                 continue
menu1()













