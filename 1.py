from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

import os
import sys
import time
import poplib
import email
import webbrowser
# import sendTempl
#77
sys.path.append('../')
from common.utils import stringDate, county, cleanShlk, openBrowser
from common.email import getEmail_pop1, getEmail_pop
from common.scenarios import loginToolkit, clickIfSelected, typeFormField, loginATD
proxy1http = ""
# if len(sys.argv) < 6:
#   print('FAILED. parameters are missed ' )
#   print('USAGE: run.py toolkitDomain loginName loginPass webPage contactId proxyhttp' )
#   sys.exit()
#
# toolkitDomain = sys.argv[1]
# loginName = sys.argv[2]
# loginPass = sys.argv[3]
# webPage = sys.argv[4]
# contactId = sys.argv[5]
# proxy1http = sys.argv[6]
# isProxy = len(sys.argv)
files = set()
fi = open('text.html', 'w', encoding='utf8')
max_wait_sec = 30
#subj_set = ["empty", "toro"]
subj_set = ["Housing Inventory Snapshot"] #, "Follow Up: Sent message confirmation"]
# spectionList = ['Valentines Day', 'Daylight Savings', "St Patricks Day", 'Easter', 'Spring Day', 'Mather & Father', '4July', 'Halloween', 'Thanksgiving', 'Holidays', 'Christmas', 'HappyNewYear', 'Chinese New Year', 'Hanukkah', 'Birthday', 'MemorialDay', 'EarthDay', 'LaborDay', 'ColumbusDay', 'VeteransDay',
#                 'OLIVE', 'WHITE', 'TERRACOTTA', 'BLACK-GOLD', 'RED', 'RED-BLUE', 'GREY', 'BLUE', 'GREEN', 'TURQUOISE', 'BROWN', 'BLACK-RED', 'DARK-BLUE', 'BROWN-GREEN', 'Cityline', 'Single Home', 'Seasons']

success = True
try:
    driver = openBrowser ( proxy1http )
    loginATD(driver)
    driver.find_element_by_link_text("Housing Inventory Snapshot Manager").click()
    # driver.find_element_by_css_selector("input._month").click()
    # wd.find_element_by_css_selector("input._month").send_keys("\\undefined")
    # wd.find_element_by_css_selector("input._month").click()
    time.sleep(4)
    typeFormField(driver.find_element_by_css_selector("input.text._realtorId"), "12840347017")
    driver.find_element_by_css_selector("input._sendTestCtl.btn").click()
    WebDriverWait(driver, max_wait_sec).until(EC.alert_is_present())
    driver.switch_to_alert().accept()
    time.sleep(8)
    #get_mail
    text = getEmail_pop("mail.propertyminder.com", "110", "chupina.anastasia@propertyminder.com", "Recaiqu4", subj_set[0])
    for i in range(len(text)):
        f = open('text' + str(i) + '.html', 'w', encoding='utf8')
        time.sleep(3) # 5*4 sec ждем и проверяем письмо с нужным сабж
        f.write(text[i]) #str(arrayOfLists) + '\n')
        url = 'file://' + os.path.realpath('text' + str(i) + '.html')
        driver.get(url)
        time.sleep(3)
        # if i == 1:
        #    driver.get(url, new = 2)
        driver.find_element_by_link_text ("HERE").click()
        f.close()
    #webbrowser.open(url, new = 2) #просмотр в Opera
    time.sleep(5)
    #print(msgtext)
finally:
    driver.quit()
    if not success:
        raise Exception("Test failed.")
print('789_8')




def getEmail_pop1(host1, port1, recipient, password, subj_set): #не работает
    bodyarray = set()
    for i in range(8):
        pop=poplib.POP3(host = host1, port = port1, timeout = 3)
        pop.user(recipient)
        pop.pass_(password)
        num = pop.stat()[0] #метод статистики, 1й эл-т [0] - это их кол-во, считаем
        if num > 0:
            for n in range(num):

                msglines = pop.retr(n+1)[1] #получаем письмо, параметр - индекс начинается с 1(потому +1), возвращает кортеж, текст письма во 2м элементе [1]
                msgtext = "\n".join(map(lambda x: x.decode('utf-8'), msglines)) #склеиваем эти строки, предварительно декодирование
                msg = email.message_from_string (msgtext) #это получили сообшение, в к-ром выделили текст письма, заголовок, анализирем на сабж
                try:
                    if msg.get("Subject") in subj_set:
                        pop.dele(n+1) #пометка на удаление
                        text =  msg.get_payload()  #если заголовок сходится с заданным, то получаем тело письма msg.get_payload
                        bodyarray.append(text)
                        print(text)
                        pop.quit()
                        print ('234_'+str(i))
                        return bodyarray
                except:
                    pop.quit()
        #    else:
        print("345")
        pop.quit()
        time.sleep(4)



def getEmail_pop(host1, port1, recipient, password, subj_set): #фильтр по единственному Subj
    for i in range(5):
        pop=poplib.POP3(host = host1, port = port1, timeout = 3)
        pop.user(recipient)
        pop.pass_(password)
        num = pop.stat()[0] #метод статистики, 1й эл-т [0] - это их кол-во, считаем
        if num > 0:
            for n in range(num):
                msglines = pop.retr(n+1)[1] #получаем письмо, параметр - индекс начинается с 1(потому +1), возвращает кортеж, текст письма во 2м элементе [1]
                msgtext = "\n".join(map(lambda x: x.decode('utf-8'), msglines)) #склеиваем эти строки, предварительно декодирование
                msg = email.message_from_string (msgtext) #это получили сообшение, в к-ром выделили текст письма, заголовок, анализирем на сабж
                if msg.get("Subject") == subj_set:
                        pop.dele(n+1) #пометка на удаление
                        text =  msg.get_payload()  #если заголовок сходится с заданным, то получаем тело письма msg.get_payload
                        print(text)
                        pop.quit()
                        return text
                #except:
                #pop.quit()
        pop.quit()
        time.sleep(3)




