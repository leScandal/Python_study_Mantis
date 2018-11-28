def getEmail_pop(host1, port1, recipient, password, subj_set):
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
                for item in subj_set:
                #if msg.get("Subject") == "empty1":
                    if msg.get("Subject") == item:
                        pop.dele(n+1) #пометка на удаление
                        text =  msg.get_payload()  #если заголовок сходится с заданным, то получаем тело письма msg.get_payload
                        pop.quit()
                        print(text)
                else:
                    pop.quit()
    return



max_wait_sec = 30
subj_set = list ("Housing Inventory Snapshot")

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
    getEmail_pop("mail.propertyminder.com", "110", "chupina.anastasia@propertyminder.com", "Recaiqu4", lists_subj)
    time.sleep(4) #5*4 sec ждем и проверяем письмо с нужным сабж
    f.write(text) #str(arrayOfLists) + '\n')
    url = 'file://' + os.path.realpath("text1.html")
    webbrowser.open(url, new = 2) #просмотр в Opera
    driver.get(url)
    driver.find_element_by_link_text ("HERE").click()
    time.sleep(5)
    f.close()
    #print(msgtext)
finally:
    driver.quit()
    if not success:
        raise Exception("Test failed.")
print('789_8')
