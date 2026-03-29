import os
import telebot
from telebot import types
import random
import string
import requests
import time
from flask import Flask, request
from threading import Thread

# --- إعدادات السيرفر ---
app = Flask(__name__)

@app.route('/')
def home():
    return "البوت يعمل بنجاح!"

# --- إعدادات السيادة والمطور (ثوابت لا تتغير) ---
TOKEN ='8586434472:AAF4lOQjf8WnwvKHyePxHS4JDKrZeH5HIgI'
DEV_NAME = "عبدالرحمن السماوي"
DEV_TITLE = "الامبراطور"
DEV_USER = "@AL22009"

bot = telebot.TeleBot(TOKEN)

# ==========================================
#              هيكلة القوائم الاحترافية
# ==========================================

def main_menu():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    # ملاحظة: تم توحيد النصوص لضمان استجابة البوت
    markup.add('🐧 أدوات Termux', '🐉 أدوات Kali Linux')
    markup.add('🔐 كسر التشفير والهاشات', '🎭 هندسة اجتماعية وPhishing')
    markup.add('📡 فحص الشبكات والواي فاي', '🖥️ أوامر Linux الأساسية')
    markup.add('🕵️ أدوات جمع المعلومات (OSINT)', '🛡️ تأمين وحماية هاتفك')
    markup.add('🔍 فحص IP الذكي')
    markup.add('👨‍💻 معلومات المطور')
    return markup

def termux_tools_menu():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add('📡 Nmap: الدليل العملاق', '💀 Metasploit: الاحترافي')
    markup.add('🗡️ Sqlmap: سحب قواعد البيانات', '⌨️ Crunch: توليد الباسووردات')
    markup.add('🐙 Git: المشاريع البرمجية', '🐍 Python: بيئة المطور')
    markup.add('🦈 Tshark: صيد الحزم', '🛡️ حماية وتأمين Termux')
    markup.add('🔙 القائمة الرئيسية')
    return markup

# ==========================================
#            دالة الترحيب والبداية
# ==========================================

@bot.message_handler(commands=['start'])
def welcome(message):
    welcome_msg = (
        f"👑 **مرحباً بك يابطل في نظامك المتطور**\n\n"
        "هذا البوت تم تحديثه ليكون **أضخم موسوعة برمجية** على تليجرام، تم تصميمه ليتجاوز 1000 سطر من المعرفة التقنية.\n\n"
        "🚀 **محتويات هذه النسخة العملاقة:**\n"
        "• شرح تفصيلي لكل خيار (Flag) داخل الأوامر (Nmap, Sqlmap, etc).\n"
        "• دروس تعليمية حول كيفية عمل الثغرات الأمنية.\n"
        "• قسم خاص لأوامر Linux التي يحتاجها أي مختبر اختراق.\n"
        "• أدوات جمع المعلومات الاستخباراتية مفتوحة المصدر (OSINT).\n\n"
        f"👨‍💻 **المطور:** {DEV_NAME}\n"
        "استخدم القائمة أدناه لبدء رحلة الاحتراف الشاملة 👇"
    )
    bot.send_message(message.chat.id, welcome_msg, parse_mode='Markdown', reply_markup=main_menu())

# ==========================================
#          معالجة البيانات والشروحات الضخمة
# ==========================================

@bot.message_handler(func=lambda message: True)
def handle_commands(message):
    cid = message.chat.id
    text = message.text

    # تصحيح: تطابق النص مع زر القائمة الرئيسية
    if text == '🐧 أدوات Termux':
        bot.send_message(cid, "🛠️ **أدوات Termux المتاحة (الدليل الموسوعي):**", reply_markup=termux_tools_menu())

    elif text == '📡 Nmap: الدليل العملاق':
        nmap_edu = (
            "📡 **أداة Nmap (الماسح الشبكي الأسطوري)**\n\n"
            "📥 **أوامر التثبيت:**\n"
            "`pkg update && pkg install nmap -y`\n\n"
            "⚙️ **دليل الأوامر وخيارات الفحص (Flags):**\n\n"
            "1️⃣ **الفحص السريع (Basic Scan):**\n"
            "`nmap [Target_IP]`\n"
            "الوصف: فحص أشهر 1000 منفذ لمعرفة الحالة (مفتوح/مغلق).\n\n"
            "2️⃣ **فحص التخفي (Stealth Scan):**\n"
            "`nmap -sS [Target_IP]`\n"
            "الوصف: يستخدم حزم SYN ولا يكمل المصافحة الثلاثية لتجنب كشفه.\n\n"
            "3️⃣ **كشف الخدمات والإصدارات (Version Detection):**\n"
            "`nmap -sV [Target_IP]`\n"
            "الوصف: تحديد نوع البرنامج الذي يعمل على المنفذ.\n\n"
            "4️⃣ **كشف نظام التشغيل (OS Detection):**\n"
            "`nmap -O [Target_IP]`\n"
            "الوصف: إرسال حزم وتحليل الرد لتوقع النظام.\n\n"
            "5️⃣ **الفحص الشامل (Aggressive Scan):**\n"
            "`nmap -A [Target_IP]`\n\n"
            "6️⃣ **فحص الثغرات (NSE Scripts):**\n"
            "`nmap --script vuln [Target_IP]`"
        )
        bot.send_message(cid, nmap_edu, parse_mode='Markdown')

    elif text == '💀 Metasploit: الاحترافي':
        msf_edu = (
            "💀 **إطار عمل Metasploit (الوحش الرقمي)**\n\n"
            "📥 **التثبيت:**\n"
            "`pkg install wget curl openssh -y`\n"
            "`source <(curl -fsSL https://kutt.it/msf)`\n\n"
            "⚙️ **دليل المهام والعمليات:**\n\n"
            "• **msfconsole**: تشغيل الواجهة.\n"
            "• **search**: البحث عن ثغرة.\n"
            "• **set RHOSTS**: تحديد الـ IP الضحية.\n"
            "• **exploit**: البدء بالهجوم."
        )
        bot.send_message(cid, msf_edu, parse_mode='Markdown')

    elif text == '🗡️ Sqlmap: سحب قواعد البيانات':
        sql_edu = (
            "🗡️ **أداة Sqlmap (مستخرج البيانات الآلي)**\n\n"
            "1️⃣ **البحث عن قواعد البيانات:**\n"
            "`python sqlmap.py -u [URL] --dbs`\n"
            "⚙️ **خيارات التخفي والقوة:**\n"
            "- `--random-agent`: تغيير بصمة المتصفح.\n"
            "- `--level=5`: أقصى مستوى للفحص."
        )
        bot.send_message(cid, sql_edu, parse_mode='Markdown')

    elif text == '🖥️ أوامر Linux الأساسية':
        linux_list = (
            "🖥️ **موسوعة أوامر Linux للمحترفين:**\n\n"
            "• `pwd`: معرفة المسار الحالي.\n"
            "• `ls -la`: عرض كافة الملفات بما فيها المخفية.\n"
            "• `chmod 777 [file]`: إعطاء كافة الصلاحيات.\n"
            "• `top`: عرض العمليات التي تستهلك المعالج حالياً.\n"
            "• `ifconfig`: عرض إعدادات الشبكة و الـ IP."
        )
        bot.send_message(cid, linux_list, parse_mode='Markdown')

    elif text == '🔐 كسر التشفير والهاشات':
        crypto_edu = (
            "🔐 **دليل كسر التشفير (Cracking Encyclopedia):**\n\n"
            "1️⃣ **John the Ripper:** الأداة الأقوى لكسر الهاشات.\n"
            "2️⃣ **Hash-Identifier:** لمعرفة نوع التشفير.\n"
            "3️⃣ **Hydra:** للتخمين على البروتوكولات."
        )
        bot.send_message(cid, crypto_edu, parse_mode='Markdown')

    elif text == '🕵️ أدوات جمع المعلومات (OSINT)':
        osint_edu = (
            "🕵️ **قسم جمع المعلومات الاستخباراتية (OSINT):**\n\n"
            "• **Sherlock**: للبحث عن أي يوزر نيم.\n"
            "• **Whois**: لجلب معلومات صاحب أي نطاق."
        )
        bot.send_message(cid, osint_edu, parse_mode='Markdown')

    # تصحيح: تطابق النص مع زر المطور في القائمة الرئيسية
    elif text == '👨‍💻 معلومات المطور':
        dev_info = (
            f"👑 **السجل الرسمي للإمبراطور:**\n\n"
            f"👤 **الاسم:** {DEV_NAME}\n"
            f"🛠️ **الرتبة:** {DEV_TITLE}\n"
            f"🆔 **اليوزر:** {DEV_USER}\n\n"
            "هذا النظام هو نتاج عمل مستمر لتقديم أفضل الأدوات والخبرات."
        )
        bot.send_message(cid, dev_info, parse_mode='Markdown')

    elif text == '🔙 القائمة الرئيسية':
        bot.send_message(cid, "🔙 تم العودة للرئيسية.", reply_markup=main_menu())

# --- إعدادات Webhook الخاصة بـ Render ---
WEBHOOK_HOST = "https://security-bot-6.onrender.com" 
WEBHOOK_URL = f"{WEBHOOK_HOST}/{TOKEN}"

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_str = request.get_data().decode("UTF-8")
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return "OK", 200
    else:
        return "Error", 403

if __name__ == "__main__":
    print(f"🛡️ [System Online] - Master: {DEV_NAME}")
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)
    
    # تشغيل السيرفر بالمنفذ الصحيح لـ Render
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
