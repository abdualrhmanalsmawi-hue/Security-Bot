import telebot
from telebot import apihelper, types
import random
import string
import requests
import time

# --- إعدادات المطور ---
TOKEN = '8586434472:AAH8GcS0eVa7W77q3r6GXI20OcZw41JFjuM'
DEV_NAME = "عبدالرحمن السماوي"
DEV_TITLE = "الامبراطور"
DEV_USER = "@AL22009"

bot = telebot.TeleBot(TOKEN)

# ملاحظة: إذا كنت ترفع الكود على Render، امسح سطر البروكسي أدناه.
# apihelper.proxy = {'https': 'http://proxy.server:3128'}

# --- تصميم القوائم ---
def main_menu():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add('🐧 أدوات Termux', '🐉 Kali Linux')
    markup.add('🔍 فحص IP', '👨‍💻 المطور')
    return markup

def termux_tools_menu():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add('📡 Nmap', '💀 Metasploit', '🗡️ Sqlmap')
    markup.add('⌨️ Crunch', '🐙 Git', '🐍 Python & Ruby')
    markup.add('🦈 Wireshark', '📶 Aircrack-ng', '🔙 القائمة الرئيسية')
    return markup

def kali_markup_menu():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add('📥 تثبيت كالي', '📡 Nmap المطور')
    markup.add('🦈 Wireshark', '🚫 طرد المتصلين')
    markup.add('🔙 القائمة الرئيسية')
    return markup

# --- الرسالة الترحيبية ---
@bot.message_handler(commands=['start'])
def welcome(message):
    welcome_text = (
        f"🛡️ مرحباً بك في نظام الأمن السيبراني المتطور\n\n"
        f"عزيزي الامبراطور، هذا البوت صُمم ليكون مرجعك الشامل.\n\n"
        f"👑 المطور المسؤول: {DEV_NAME}\n"
        f"استخدم الأزرار بالأسفل للبدء! 👇"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=main_menu())

# --- معالجة الأوامر ---
@bot.message_handler(func=lambda message: True)
def handle_all(message):
    cid = message.chat.id
    text = message.text

    # القوائم
    if text == '🐧 أدوات Termux':
        bot.send_message(cid, "🛠️ قائمة أدوات Termux:", reply_markup=termux_tools_menu())
    
    elif text == '🐉 Kali Linux':
        bot.send_message(cid, "🐉 قسم Kali Linux الاحترافي:", reply_markup=kali_markup_menu())

    # شروحات Termux
    elif text == '📡 Nmap':
        nmap_text = "🛡️ **أداة Nmap**\n\n📥 تثبيت: `pkg install nmap -y`\n\n⚙️ فحص سريع: `nmap [Target]`"
        bot.send_message(cid, nmap_text, parse_mode='Markdown')

    elif text == '💀 Metasploit':
        msf_text = "💀 **Metasploit**\n\n📥 تثبيت: `pkg install metasploit -y`\n\n⚙️ تشغيل: `msfconsole`"
        bot.send_message(cid, msf_text, parse_mode='Markdown')

    elif text == '🗡️ Sqlmap':
        sql_text = "🗡️ **Sqlmap**\n\n📥 تثبيت: `pkg install python git -y`\n\n⚙️ فحص: `python sqlmap.py -u [URL] --dbs`"
        bot.send_message(cid, sql_text, parse_mode='Markdown')

    elif text == '⌨️ Crunch':
        crunch_text = "⌨️ **أداة Crunch:**\n\nتستخدم لإنشاء لستات باسووردات.\n⚙️ مثال: `crunch 4 8 abcd123 -o wordlist.txt`"
        bot.send_message(cid, crunch_text, parse_mode='Markdown')

    elif text == '🐙 Git':
        git_text = "🐙 **أداة Git:**\n\nتستخدم لتحميل المشاريع من GitHub.\n📥 تثبيت: `pkg install git -y`"
        bot.send_message(cid, git_text, parse_mode='Markdown')

    elif text == '🐍 Python & Ruby':
        py_rb_text = "🐍 **لغات البرمجة:**\n\n📥 بايثون: `pkg install python -y` \n💎 روبي: `pkg install ruby -y`"
        bot.send_message(cid, py_rb_text, parse_mode='Markdown')

    elif text == '📶 Aircrack-ng':
        air_text = "📶 **أداة Aircrack-ng:**\n\nلاختبار اختراق شبكات الواي فاي.\n📥 تثبيت: `pkg install aircrack-ng -y`"
        bot.send_message(cid, air_text, parse_mode='Markdown')

    # شروحات Kali
    elif text == '📥 تثبيت كالي':
        kali_text = "🐉 **تثبيت Kali NetHunter:**\n\n1️⃣ `wget -O install-nethunter-termux https://offs.ec/2Mws39s` \n2️⃣ `chmod +x install-nethunter-termux`"
        bot.send_message(cid, kali_text, parse_mode='Markdown')

    elif text == '📡 Nmap المطور':
        nmap_adv = "📡 **Nmap المطور:**\n\n• `nmap --script vuln [IP]` : فحص الثغرات."
        bot.send_message(cid, nmap_adv, parse_mode='Markdown')

    elif text == '🚫 طرد المتصلين':
        kick_text = "🚫 **طرد المتصلين:**\n\n`aireplay-ng --deauth 0 -a [BSSID] wlan0mon`"
        bot.send_message(cid, kick_text, parse_mode='Markdown')

    elif text == '🦈 Wireshark':
        ws_text = "🦈 **Wireshark (TShark):**\n\n1️⃣ كشف الواجهات: `tshark -D` \n2️⃣ بدء التنصت: `tshark -i 1`"
        bot.send_message(cid, ws_text, parse_mode='Markdown')

    # ميزات أخرى
    elif text == '🔍 فحص IP':
        bot.send_message(cid, "🌐 أرسل الـ IP وسأقوم بتحليله لك قريباً.")

    elif text == '👨‍💻 المطور':
        dev_text = f"👑 **معلومات المطور:**\n👤 الاسم: {DEV_NAME}\n🆔 اليوزر: {DEV_USER}\n🛠️ اللقب: {DEV_TITLE}"
        bot.send_message(cid, dev_text, parse_mode='Markdown')

    elif text == '🔙 القائمة الرئيسية':
        bot.send_message(cid, "🔙 تم الرجوع للقائمة الرئيسية.", reply_markup=main_menu())

# تشغيل البوت
print(f"🛡️ [System Active] - Bot by {DEV_NAME} is running!")
bot.polling(non_stop=True)
