
from time import sleep
from pyrogram import Client, filters, sync
from pyrogram.errors import FloodWait
import os
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import ChatPermissions
import time
from time import sleep
if os.sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")
app = Client('dedinside-session', api_id=1016382, api_hash='c27834e5683d50a9bacf835a95ec4763')

app.start()

app.stop()
print('''
      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
      ┃       Made by dayot               Созданно dayot        ┃
      ┃  Instagram: @d.dayot1     ┃
      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


''')
print("После ввода задержки напишите в любой телеграм чат команду \n --Команды-- \n.dead 0 \n.night 0 \n.ghoul")
print("\n МЫ НЕ НЕСЕМ ОТВЕТСВЕННОСТИ ЗА ВАШИ ДЕЙСТВИЯ!")
print()
cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))
if cool == 0:
    print("Слишком быстро!")
    cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))
if cool > 10:
    print("Слишком медленно!")
    cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))
if cool < 5:
    print("Слишком быстро!")
    cool = int(input("Введите завис.число - от него будет зависеть скорость(Норма 8):  "))


@app.on_message(filters.command("dd", prefixes=".") & filters.me)
def valentine(_, msg):
    txt = textded.split("\n")
    e = True
    etime = int(msg.text.split('.dd ', maxsplit=1)[1])
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                msg.edit('<b>Error: Нельзя ставить больше 10с!</>')
                sleep(0.5)
                msg.delete()
            except:
               pass
        else:
            try:
                msg.edit(f'❤️{i} ❤️')
                sleep(time/cool)
                msg.edit(f'🧡 {i} 🧡')
                sleep(time/cool)
                msg.edit(f'💛 {i} 💛')
                sleep(time/cool)
                msg.edit(f'💚 {i} 💚')
                sleep(time/cool)
                msg.edit(f'💙 {i} 💙')
                sleep(time/cool)
                msg.edit(f'💜 {i} 💜')
                sleep(time/cool)
                msg.edit(f'🖤 {i} 🖤')
                sleep(time/cool)
                msg.edit(f'🤍 {i} 🤍')
                sleep(time/cool)
            except:
                pass
    msg.edit(f'<b> ⭐ @starzedscript </b>')

textded = '''
<b>доброе утро зайка</b> 🫀
<b>доброе ночи солнышко</b> 💛
<b>доброе ночи котёнок</b> ❤
<b>доброе ночи цветочек</b> 💙
<b>доброе ночи ангелочек</b> 💜
<b>доброе ночи принцесса</b> 💓
<b>доброе ночи красотка</b> 💕 
<b>доброе ночи милашк</b> 💖 
<b>доброе ночи симпатяжка</b> 💗
<b>доброе ночи бусинка</b> 💘
❤ <b>я</b> ❤
<b>💚 тебя 💚</b>
<b>💙 очень 💙</b>
<b>💛 сильно 💛</b>
<b>💜 люблю 💜</b>
'''

textded1 = '''
<b>спокойной ночи зайка</b> 💚
<b>спокойной ночи солнышко</b> 💛
<b>спокойной ночи котёнок</b> ❤
<b>спокойной ночи цветочек</b> 💙
<b>спокойной ночи ангелочек</b> 💜
<b>спокойной ночи принцесса</b> 💓
<b>спокойной ночи красотка</b> 💕 
<b>спокойной ночи милашк</b>а 💖 
<b>спокойной ночи симпатяжка</b> 💗
<b>спокойной ночи бусинка</b> 💘
❤ <b>я</b> ❤
<b>💚 тебя 💚</b>
<b>💙 очень 💙</b>
<b>💛 сильно 💛</b>
<b>💜 люблю 💜</b>
'''

@app.on_message(filters.command("night", prefixes=".") & filters.me)
def valentine(_, msg):
    txt = textded1.split("\n")
    e = True
    etime = int(msg.text.split('.night ', maxsplit=1)[1])
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                sleep(0.5)
                msg.delete()
            except:
                pass
        else:
            try:
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
            except:
                pass
    msg.edit(f'<b> ⭐ inst: d.dayot1</b>')

