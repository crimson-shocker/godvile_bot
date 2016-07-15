#! /usr/bin/env python3
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#---Variable---
prot = 'Противник'
global find_enemy

#/---Variable---

#---passwd_file---
print('===============Start_bot===============')
f = open('/opt/passwd')
a = f.read()
r = a.replace("\n", "")
username = r.split(':')[0]
passwd = r.split(':')[1]
f.close()
#/---passwd_file---

browser = webdriver.Firefox()
browser.get('https://godville.net')

#---login---
browser.find_element_by_id('username').send_keys(username)
time.sleep (1)
browser.find_element_by_id('password').send_keys(passwd)
time.sleep (1)
browser.find_element_by_css_selector('input[name="commit"]').click()
time.sleep (1)
#/---login---

try:
    WebDriverWait(browser, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'h2.block_title'))
    )
except:
	pass
#---script_body---

#--lists--
word = ['кирпич']
#/--lists--

#--stats--
class statistics:
	def hp(self):
		hp = browser.find_element_by_css_selector('#hk_health > div.l_val').text
		return(int(hp.split(' /')[0]))


	def mob(self):
		monster = browser.find_element_by_css_selector('div.block_content > div > div.line > div.l_capt').text
		return(monster)

	def prana_charge(self):
		pran_charge = browser.find_element_by_css_selector('span.acc_val').text
		return(pran_charge)

	def prana(self):
		prana_find = browser.find_element_by_css_selector('div.gp_val')
		prana_percent = str(prana_find.text)
		prana_count = prana_percent.split("%")[0]
		return(int(prana_count))

	def gold(self):
		hero_gold = browser.find_element_by_css_selector('#hk_gold_we > div.l_val').text
		try:
			return int((hero_gold.split(" ")[1]))
		except:
			return 0

	def if_hero_with_mob(self):
		while mob() == prot:
			time.sleep(2)

st = statistics() #statistic object
#/--stats--
#--interaction with the hero--
class prod_voice:
	def dig(self):
		browser.find_element_by_id('godvoice').send_keys('клад')
		time.sleep(1)
		browser.find_element_by_id('voice_submit').click()

	def stone(self):
		while True:
			if st.prana() > 25:
				browser.find_element_by_xpath("//a[contains(text(),'Сделать хорошо')]").click()
				time.sleep(3)
			else:
				break

			if word[0] in browser.find_element_by_css_selector('div.d_msg').text:
				break
			

		

voice = prod_voice()
#/--interaction with the hero--
#--arena
class arena:
	def try_find_enemy(self):
		try:
			find_enemy = browser.find_element_by_css_selector('#o_info > div.block_h > h2.block_title').text
			return find_enemy
		except:
			find_enemy = " "
			return find_enemy

	def hero_arena(self):
#'Отправить на арену'
#no batton and have time until arena
#browser.find_element_by_css_selector('div.arena_msg').text
		if "Арена откроется" in browser.find_element_by_css_selector('div.arena_msg').text:
			print(browser.find_element_by_css_selector('div.arena_msg').text)
			time.sleep(1)
			print("Arena is not avaliable. We must exit! bye!")
			exit(0)
		elif "Отправить на арену" in browser.find_element_by_css_selector('a.no_link.to_arena').text:
			print('Start_arena')
			browser.find_element_by_css_selector('a.no_link.to_arena').click()
			time.sleep(2)
			alert = browser.switch_to_alert()
			time.sleep(2)
			alert.accept()
			time.sleep(1)
			try:
				alert.accept()
				time.sleep(1)
				exit(0)
			except:
				pass

			time.sleep (3)

#               def try_find_enemy():
#                       try:
#                               find_enemy = browser.find_element_by_css_selector('#o_info > div.block_h > h2.block_title').text
#                               return find_enemy
#                       except:
#                               find_enemy = " "
#                               return find_enemy

#
#                while try_find_enemy() != prot and prana() >= 4:
#                        print('Wait enemy in arena...')
#                        time.sleep (5)
#                else:
#                        print("Enemy is come! Arena begin!")
#                        time_process_battle_shout()


	def god_battle_voice(self):
		try:
			browser.find_element_by_id('godvoice').send_keys('бей')
			print("Hit!")
			time.sleep (1)
			browser.find_element_by_id('voice_submit').click()
		except:
			print("Oops, not now... wait!")


ar = arena() #arena object
#/--arena--
#--AI--
def main():
	if st.hp() == 0: #resurection
		browser.find_element_by_xpath("//a[contains(text(),'Воскресить')]").click()

	try:
		browser.find_element_by_xpath("//a[contains(text(),'@')]").click()
	except:
		pass

	if st.mob() != prot and st.gold() > 9000:
		voice.stone()
		time.sleep(1)
		voice.stone()
		time.sleep(1)
		voice.stone()
	elif st.gold() > 6000:
		voice.stone()
		time.sleep(1)
		voice.stone()
		time.sleep(1)
	elif st.gold() > 3000:
		voice.stone()
		time.sleep(1)

	if st.prana() > 55 and "Отправить на арену" in browser.find_element_by_css_selector('a.no_link.to_arena').text:
		ar.hero_arena()
		
	while st.prana() > 55:
		while st.mob() == prot:
			time.sleep(5)
		
		if st.mob() != prot:
			voice.dig()
			time.sleep(1)
	else:
		browser.quit()
			

#/--AI--


if __name__=='__main__':
	main()
