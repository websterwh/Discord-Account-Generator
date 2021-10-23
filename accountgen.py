from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
from selenium.webdriver.common.keys import Keys
import sys


pchars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
uchars = '123567890'


def gen():
    print('''What email do you want to use?
[1] Temp-Mail
[2] Mohmal-Temp-Mail''')
    mails = int(input('[?]> '))

    temp_mail = 'https://temp-mail.org/cs/'

    Mohmal = 'https://www.mohmal.com/en/inbox'

    discord = 'https://discord.com/register'

    accs = int(input('How many acount do you wanna generate?: '))

    username = input('Account username: ')

    for i in range(accs):
        name = ''.join(random.choices(uchars, k=5)) + ' | ' + username

        password = ''.join(random.choices(pchars, k=12))

        driver = webdriver.Chrome(ChromeDriverManager().install())
        if mails == 1:
            driver.get(temp_mail)
            time.sleep(5)

            try:
                email = driver.find_elements_by_id('click-to-copy')[0].click()
                time.sleep(1)


            except:
                print('Some error with website... ')
                time.sleep(5)


        if mails == 2:
            driver.get(Mohmal)
            time.sleep(3)
            emaill = driver.find_element_by_class_name("email").click()
            time.sleep(1)


        driver.execute_script("window.open('');")
        time.sleep(1)


        driver.switch_to.window(driver.window_handles[1])
        driver.get(discord)
        time.sleep(1)


        driver.find_element_by_name('email').send_keys(Keys.CONTROL, 'v')
        time.sleep(1)


        driver.find_element_by_name('username').send_keys(name)
        time.sleep(1)


        driver.find_element_by_name('password').send_keys(password)
        time.sleep(1)


        driver.find_element_by_id("react-select-2-input").send_keys('11', Keys.ENTER, '9', Keys.ENTER,  '1998', Keys.ENTER)
        time.sleep(1)


        driver.find_elements_by_tag_name('button')[0].click()
        print('Verify captcha and take the Token if you want. [You need to do it manually]')
        print('If you want account with verified email you need to do it manually.')
        time.sleep(3)


        namee = 'accounts'
        with open(f'{namee}.txt', 'a') as saveFile:
            saveFile.writelines('Username: ' + ''.join(name))
            saveFile.writelines(' Password: ' + ''.join(password+'\n'))
        print(f'Password {password} and Username: {name} saved to {namee}.txt file!')
        time.sleep(3)


        restart = input('Did you verify captcha and took token? If yes press ENTER to continue with generating: ')
        restart = i


def lobby():
    print('''
╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╭━╮╭╮╭╮╱╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃┃╭╯┃┃┃┃╱╱╱╱╱╱┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╭╯╰╮┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╭╯╰╮
┃╰━╯┣╮╭┳━━┳━━┳╮╱╭╮┃╰╯╯╭┫┃┃┃╭━━┳━╮┃┃╱┃┣━━┳━━┳━━┳╮╭┳━╋╮╭╯┃┃╱╰╋━━┳━╮╭━━┳━┳━┻╮╭╋━━┳━╮
┃╭━━┫┃┃┃━━┫━━┫┃╱┃┃┃╭╮┃┣┫┃┃┃┃┃━┫╭╯┃╰━╯┃╭━┫╭━┫╭╮┃┃┃┃╭╮┫┃╱┃┃╭━┫┃━┫╭╮┫┃━┫╭┫╭╮┃┃┃╭╮┃╭╯
┃┃╱╱┃╰╯┣━━┣━━┃╰━╯┃┃┃┃╰┫┃╰┫╰┫┃━┫┃╱┃╭━╮┃╰━┫╰━┫╰╯┃╰╯┃┃┃┃╰╮┃╰┻━┃┃━┫┃┃┃┃━┫┃┃╭╮┃╰┫╰╯┃┃
╰╯╱╱╰━━┻━━┻━━┻━╮╭╯╰╯╰━┻┻━┻━┻━━┻╯╱╰╯╱╰┻━━┻━━┻━━┻━━┻╯╰┻━╯╰━━━┻━━┻╯╰┻━━┻╯╰╯╰┻━┻━━┻╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯                                         Made by Lososik
        ''')


    print('''
[1] Start
[2] Help
[3] Exit''')


    start = int(input('[?]> '))


    if start == 1:
        start = gen()


    if start == 2:
        print('''
Wassup buddy... If you find some bug or tool isnt works dm me on discord Lososik#0954 and I will try to help you...
If one of the emails will not work, use another type of email.''')


        press = input('Press eny key: ')
        press = lobby()


    if start == 3:
        sys.exit('')


if __name__ == '__main__':
    lobby()

else:
    sys.exit('Error...')
