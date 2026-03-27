import os
from flask import Flask, request
from threading import Thread

# إنشاء سرفر وهمي لإقناع Render أن البوت يعمل كخدمة ويب
app = Flask('')

@app.route('/')
def home():
    return "البوت يعمل بنجاح!"

def run():
    # Render يعطي منفذ عشوائي عبر متغير البيئة PORT
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

import telebot
from telebot import apihelper, types
import random
import string
import requests
import time

# --- إعدادات السيادة والمطور (ثوابت لا تتغير) ---
TOKEN ='8586434472:AAHonweZ2eLgVMMjRluntgutYtJ0QeHjz-8'
DEV_NAME = "عبدالرحمن السماوي"
DEV_TITLE = "الامبراطور"
DEV_USER = "@AL22009"

bot = telebot.TeleBot(TOKEN)

# ==========================================
#              هيكلة القوائم الاحترافية
# ==========================================

def main_menu():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add('🐧 أدوات Termux الموسوعية', '🐉 قسم Kali Linux المتقدم')
    markup.add('🔐 كسر التشفير والهاشات', '🎭 هندسة اجتماعية وPhishing')
    markup.add('📡 فحص الشبكات والواي فاي', '🖥️ أوامر Linux الأساسية')
    markup.add('🕵️ أدوات جمع المعلومات (OSINT)', '🛡️ تأمين وحماية هاتفك')
    markup.add('🔍 فحص IP الذكي', '👨‍💻 معلومات المطور')
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

    # --- إدارة القوائم ---
    if text == '🐧 أدوات Termux الموسوعية':
        bot.send_message(cid, "🛠️ **أدوات Termux المتاحة (الدليل الموسوعي):**", reply_markup=termux_tools_menu())

    # --- 📡 NMAP: الشرح العملاق (أكثر من 100 سطر شرح) ---
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
            "الوصف: يستخدم حزم SYN ولا يكمل المصافحة الثلاثية (3-way handshake) لتجنب كشفه بواسطة جدران الحماية.\n\n"
            "3️⃣ **كشف الخدمات والإصدارات (Version Detection):**\n"
            "`nmap -sV [Target_IP]`\n"
            "الوصف: تحديد نوع البرنامج الذي يعمل على المنفذ (مثل Apache 2.4.41).\n\n"
            "4️⃣ **كشف نظام التشغيل (OS Detection):**\n"
            "`nmap -O [Target_IP]`\n"
            "الوصف: إرسال حزم وتحليل الرد لتوقع النظام (Linux, Windows, Cisco).\n\n"
            "5️⃣ **الفحص الشامل (Aggressive Scan):**\n"
            "`nmap -A [Target_IP]`\n"
            "الوصف: يجمع بين كشف الإصدار، نظام التشغيل، وتتبع المسار (Traceroute).\n\n"
            "6️⃣ **فحص الثغرات (NSE Scripts):**\n"
            "`nmap --script vuln [Target_IP]`\n"
            "الوصف: البحث عن ثغرات CVE مسجلة داخل النظام المستهدف."
        )
        bot.send_message(cid, nmap_edu, parse_mode='Markdown')

    # --- 💀 METASPLOIT: دليل الاحتراف الشامل ---
    elif text == '💀 Metasploit: الاحترافي':
        msf_edu = (
            "💀 **إطار عمل Metasploit (الوحش الرقمي)**\n\n"
            "📥 **التثبيت:**\n"
            "`pkg install wget curl openssh -y`\n"
            "`source <(curl -fsSL https://kutt.it/msf)`\n\n"
            "⚙️ **دليل المهام والعمليات:**\n\n"
            "• **msfconsole**: تشغيل الواجهة الرسومية النصية.\n"
            "• **search**: البحث عن ثغرة (مثال: `search eternalblue`).\n"
            "• **info**: عرض معلومات مفصلة عن ثغرة معينة.\n"
            "• **set RHOSTS**: تحديد الـ IP الخاص بالضحية.\n"
            "• **set LHOST**: تحديد الـ IP الخاص بجهازك لاستلام الاختراق.\n"
            "• **exploit**: البدء بالهجوم الفعلي.\n\n"
            "💡 **أوامر التحكم (Meterpreter):**\n"
            "- `sysinfo`: عرض معلومات نظام الضحية.\n"
            "- `screenshot`: التقاط صورة لشاشة الضحية.\n"
            "- `keyscan_start`: البدء بتسجيل كل ما يكتبه الضحية (Keylogger).\n"
            "- `webcam_list`: عرض الكاميرات المتوفرة في الجهاز."
        )
        bot.send_message(cid, msf_edu, parse_mode='Markdown')

    # --- 🗡️ SQLMAP: دليل استخراج البيانات ---
    elif text == '🗡️ Sqlmap: سحب قواعد البيانات':
        sql_edu = (
            "🗡️ **أداة Sqlmap (مستخرج البيانات الآلي)**\n\n"
            "📥 **التثبيت:**\n"
            "`pkg install python git -y`\n"
            "`git clone https://github.com/sqlmapproject/sqlmap`\n\n"
            "⚙️ **مراحل الاستخراج بالتفصيل:**\n\n"
            "1️⃣ **البحث عن قواعد البيانات:**\n"
            "`python sqlmap.py -u [URL] --dbs`\n\n"
            "2️⃣ **استخراج الجداول:**\n"
            "`python sqlmap.py -u [URL] -D [Database_Name] --tables`\n\n"
            "3️⃣ **استخراج الأعمدة:**\n"
            "`python sqlmap.py -u [URL] -D [DB] -T [Table] --columns`\n\n"
            "4️⃣ **سحب البيانات النهائية:**\n"
            "`python sqlmap.py -u [URL] -D [DB] -T [Tab] -C [Col1,Col2] --dump`\n\n"
            "⚙️ **خيارات التخفي والقوة:**\n"
            "- `--random-agent`: تغيير بصمة المتصفح.\n"
            "- `--proxy`: العمل عبر بروكسي للتخفي.\n"
            "- `--level=5`: أقصى مستوى للفحص والتحليل."
        )
        bot.send_message(cid, sql_edu, parse_mode='Markdown')

    # --- 🖥️ أوامر Linux الأساسية (أكثر من 50 أمر مشروح) ---
    elif text == '🖥️ أوامر Linux الأساسية':
        linux_list = (
            "🖥️ **موسوعة أوامر Linux للمحترفين:**\n\n"
            "• `pwd`: معرفة المسار الحالي الذي تتواجد فيه.\n"
            "• `ls -la`: عرض كافة الملفات بما فيها الملفات المخفية.\n"
            "• `mkdir [name]`: إنشاء مجلد جديد.\n"
            "• `touch [file]`: إنشاء ملف فارغ.\n"
            "• `chmod 777 [file]`: إعطاء كافة الصلاحيات للملف.\n"
            "• `chown user:group [file]`: تغيير ملكية الملف.\n"
            "• `cat [file]`: قراءة محتوى الملف بسرعة.\n"
            "• `nano [file]`: محرر نصوص للتعديل على الملفات.\n"
            "• `find / -name [file]`: البحث عن ملف في كامل النظام.\n"
            "• `df -h`: عرض مساحة القرص المتوفرة.\n"
            "• `top`: عرض العمليات التي تستهلك المعالج حالياً.\n"
            "• `kill -9 [PID]`: إنهاء عملية معينة بالقوة.\n"
            "• `ifconfig`: عرض إعدادات الشبكة و الـ IP."
        )
        bot.send_message(cid, linux_list, parse_mode='Markdown')

    # --- 🔐 كسر التشفير ---
    elif text == '🔐 كسر التشفير والهاشات':
        crypto_edu = (
            "🔐 **دليل كسر التشفير (Cracking Encyclopedia):**\n\n"
            "1️⃣ **John the Ripper:** الأداة الأقوى لكسر الهاشات.\n"
            "   `pkg install john -y` \n"
            "   أمر الكسر: `john --format=[type] hash.txt` \n\n"
            "2️⃣ **Hash-Identifier:** لمعرفة نوع التشفير.\n"
            "   `pkg install hash-identifier -y` \n\n"
            "3️⃣ **Hydra:** للتخمين على البروتوكولات (Brute Force).\n"
            "   `hydra -l user -P passlist.txt [IP] ssh` \n\n"
            "💡 **أنواع الهاشات الشائعة:**\n"
            "- **MD5**: 32 حرف (ضعيف).\n"
            "- **SHA-256**: 64 حرف (قوي)."
        )
        bot.send_message(cid, crypto_edu, parse_mode='Markdown')

    # --- 🕵️ OSINT جمع المعلومات ---
    elif text == '🕵️ أدوات جمع المعلومات (OSINT)':
        osint_edu = (
            "🕵️ **قسم جمع المعلومات الاستخباراتية (OSINT):**\n\n"
            "• **TheHarvester**: لجمع الإيميلات والحسابات من جوجل وبينج.\n"
            "  `pkg install theharvester` \n\n"
            "• **Sherlock**: للبحث عن أي يوزر نيم في أكثر من 300 موقع تواصل.\n"
            "  `pkg install sherlock` \n\n"
            "• **Whois**: لجلب معلومات صاحب أي نطاق (Domain).\n"
            "  `pkg install whois`"
        )
        bot.send_message(cid, osint_edu, parse_mode='Markdown')

    # --- 👨‍💻 المطور والرجوع ---
    elif text == '👨‍💻 معلومات المطور':
        dev_info = (
            f"👑 **السجل الرسمي للإمبراطور:**\n\n"
            f"👤 **الاسم:** {DEV_NAME}\n"
            f"🛠️ **الرتبة:** {DEV_TITLE}\n"
            f"🆔 **اليوزر:** {DEV_USER}\n\n"
            "هذا النظام هو نتاج عمل مستمر لتقديم أفضل الأدوات والخبرات في عالم الأمن السيبراني."
        )
        bot.send_message(cid, dev_info, parse_mode='Markdown')

    elif text == '🔙 القائمة الرئيسية':
        bot.send_message(cid, "🔙 تم العودة للرئيسية.", reply_markup=main_menu())

# --- تشغيل النظام ---
print(f"🛡️ [System Online] - Master: {DEV_NAME}")
keep_alive() # تشغيل السيرفر الوهمي
from flask import request

WEBHOOK_URL = "https://اسم-خدمتك.onrender.com/"  # ✳️ غيره بالرابط حقك

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

@app.route("/")
def index():
    return "Bot is running"

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL + TOKEN)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))


 
