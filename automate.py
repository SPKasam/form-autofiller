from selenium import webdriver
import time

web = webdriver.Chrome()
web.get("https://nyu.qualtrics.com/jfe/form/SV_ePNv0eXvGWgCxkq?")
time.sleep(0.5)

next = web.find_element('xpath','//*[@id="NextButton"]')
next.click()
time.sleep(1)

nyu_id = web.find_element('xpath','//*[@id="QID2"]/div[3]/div/fieldset/div/ul/li[2]')
nyu_id.click()
time.sleep(1)

my_email = "pranithkasam7@gmail.com"
email = web.find_element('xpath','//*[@id="QR~QID4"]')
email.send_keys(my_email)
time.sleep(1)

next1 = web.find_element('xpath','//*[@id="NextButton"]')
next1.click()
time.sleep(2)

first_name = "Sai"
first = web.find_element('xpath','//*[@id="QR~QID26~5"]')
first.send_keys(first_name)

last_name = "Kasam"
last = web.find_element('xpath','//*[@id="QR~QID26~6"]')
last.send_keys(last_name)

phone_number = "5126455127"
phone = web.find_element('xpath','//*[@id="QR~QID26~7"]')
phone.send_keys(phone_number)

company_working = "Prudential"
company = web.find_element('xpath','//*[@id="QR~QID26~8"]')
company.send_keys(company_working)

next2 = web.find_element('xpath','//*[@id="NextButton"]')
next2.click()
