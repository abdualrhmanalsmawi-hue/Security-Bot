import telebot
from telebot import apihelper, types
import random
import string
import requests
import time

# --- إعدادات المطور (ثابتة - الإمبراطور) ---
TOKEN = '8586434472:AAH8GcS0eVa7W77q3r6GXI20OcZw41JFjuM'
DEV_NAME = "عبدالرحمن السماوي"
DEV_TITLE = "الامبراطور"
DEV_USER = "@AL22009"

bot = telebot.TeleBot(TOKEN)

# ==========================================
#              تصميم القوائم (Keyboard)
# ==========================================

def main_menu():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add('🐧 أدوات Termux', '🐉 Kali Linux')
    markup.add('🔍 فحص IP الذكي', '👨‍💻 المطور')
    return markup

def termux_tools_menu():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add('📡 Nmap التفصيلي', '💀 Metasploit Pro')
    markup.add('🗡️ Sqlmap SQLi', '⌨️ Crunch Pass')
    markup.add('🐙 Git & GitHub', '🐍 Python & Ruby')
    markup.add('🦈 Wireshark/Tshark', '📶 Aircrack-ng')
    markup.add('🔙 القائمة الرئيسية')
    return markup

def kali_markup_menu():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add('📥 تثبيت كالي (NetHunter)', '📡 Nmap للمتقدمين')
    markup.add('🦈 تحليل Wireshark', '🚫 أدوات قطع النت')
    markup.add('🔙 القائمة الرئيسية')
    return markup

# ==========================================
#            الرسالة الترحيبية
# ==========================================

@bot.message_handler(commands=['start'])
def welcome(message):
    welcome_text = (
        "🛡️ **مرحباً بك في نظام الأمن السيبراني المتطور**\n\n"
        "عزيزي الامبراطور، هذا البوت هو مرجعك الشامل لتعلم أدوات الاختراق الأخلاقي.\n\n"
        "✨ **ماذا ستجد هنا؟**\n"
        "• شرح جميع أدوات Termux بأوامرها التفصيلية.\n"
        "• بناء لستات التخمين وفحص الثغرات.\n"
        "• دروس تثبيت Kali Linux وإدارة الشبكات.\n\n"
        f"👑 **المطور:** {DEV_NAME} ({DEV_TITLE})\n"
        f"🔗 **للدعم التقني:** {DEV_USER}\n\n"
        "اختر القسم الذي تريد البدء به من الأسفل 👇"
    )
    bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown', reply_markup=main_menu())

# ==========================================
#            معالجة الأوامر (Handlers)
# ==========================================

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    cid = message.chat.id
    text = message.text

    # --- القوائم الرئيسية ---
    if text == '🐧 أدوات Termux':
        bot.send_message(cid, "🛠️ **موسوعة أدوات Termux:**\nاختر الأداة لعرض شرح الأوامر بالتفصيل.", reply_markup=termux_tools_menu())
    
    elif text == '🐉 Kali Linux':
        bot.send_message(cid, "🐉 **قسم Kali Linux الاحترافي:**\nأدوات النظام المتقدمة وإدارة الشبكات.", reply_markup=kali_markup_menu())

    # --- شرح أداة Nmap (الأداة الأقوى للفحص) ---
    elif text == '📡 Nmap التفصيلي':
        nmap_desc = (
            "📡 **أداة Nmap (Network Mapper):**\n"
            "تستخدم لاكتشاف الأجهزة والخدمات في الشبكة.\n\n"
            "📥 **أوامر التثبيت:**\n"
            "`pkg install nmap -y`\n\n"
            "⚙️ **الأوامر وشرحها:**\n"
            "1️⃣ `nmap [IP]`\n"
            "← فحص سريع للمنافذ المفتوحة.\n"
            "2️⃣ `nmap -sV [IP]`\n"
            "← معرفة إصدار الخدمات (Version Detection).\n"
            "3️⃣ `nmap -O [IP]`\n"
            "← محاولة كشف نظام التشغيل (OS Detection).\n"
            "4️⃣ `nmap --script vuln [IP]`\n"
            "← فحص الثغرات الموجودة في الجهاز المستهدف."
        )
        bot.send_message(cid, nmap_desc, parse_mode='Markdown')

    # --- شرح أداة Metasploit ---
    elif text == '💀 Metasploit Pro':
        msf_desc = (
            "💀 **إطار Metasploit:**\n"
            "أقوى أداة لتنفيذ الاستغلال واختبار الاختراق.\n\n"
            "📥 **أوامر التثبيت:**\n"
            "`pkg install metasploit -y`\n\n"
            "⚙️ **أوامر التشغيل:**\n"
            "• `msfconsole`: لفتح الأداة.\n"
            "• `search [service]`: للبحث عن ثغرة لخدمة معينة.\n"
            "• `use exploit/[name]`: لاختيار استغلال معين.\n"
            "• `show options`: لعرض الإعدادات المطلوبة."
        )
        bot.send_message(cid, msf_desc, parse_mode='Markdown')

    # --- شرح أداة Sqlmap ---
    elif text == '🗡️ Sqlmap SQLi':
        sql_desc = (
            "🗡️ **أداة Sqlmap:**\n"
            "متخصصة في كشف واستغلال ثغرات حقن SQL.\n\n"
            "📥 **أوامر التثبيت:**\n"
            "`pkg install python git -y`\n"
            "`git clone https://github.com/sqlmapproject/sqlmap`\n\n"
            "⚙️ **أوامر الفحص:**\n"
            "• `python sqlmap.py -u [URL] --dbs`\n"
            "← سحب قواعد البيانات للموقع.\n"
            "• `python sqlmap.py -u [URL] -D [DB_Name] --tables`\n"
            "← سحب جداول قاعدة بيانات معينة."
        )
        bot.send_message(cid, sql_desc, parse_mode='Markdown')

    # --- شرح أداة Crunch ---
    elif text == '⌨️ Crunch Pass':
        crunch_desc = (
            "⌨️ **أداة Crunch:**\n"
            "لإنشاء قواميس كلمات المرور (Wordlists).\n\n"
            "📥 **التثبيت:** `pkg install crunch -y`\n\n"
            "⚙️ **شرح الأمر:**\n"
            "`crunch 4 8 abcd123 -o pass.txt`\n"
            "• `4`: الحد الأدنى للطول.\n"
            "• `8`: الحد الأقصى للطول.\n"
            "• `abcd123`: الأحرف المستخدمة في التخمين.\n"
            "• `-o`: لحفظ النتائج في ملف."
        )
        bot.send_message(cid, crunch_desc, parse_mode='Markdown')

    # --- شرح أداة Aircrack-ng ---
    elif text == '📶 Aircrack-ng':
        air_desc = (
            "📶 **أداة Aircrack-ng:**\n"
            "مجموعة أدوات لاختراق شبكات Wi-Fi (WPA/WEP).\n\n"
            "📥 **التثبيت:** `pkg install aircrack-ng -y`\n\n"
            "⚙️ **خطوات العمل:**\n"
            "1️⃣ `airmon-ng start wlan0` (تفعيل وضع المراقبة).\n"
            "2️⃣ `airodump-ng wlan0mon` (البحث عن الشبكات).\n"
            "3️⃣ `aireplay-ng --deauth 0 -a [BSSID] wlan0mon` (طرد الأجهزة من الشبكة)."
        )
        bot.send_message(cid, air_desc, parse_mode='Markdown')

    # --- قسم Kali Linux ---
    elif text == '📥 تثبيت كالي (NetHunter)':
        kali_ins = (
            "🐉 **تثبيت Kali NetHunter على Termux:**\n\n"
            "1️⃣ التحديث: `pkg update && pkg upgrade` \n"
            "2️⃣ تحميل السكريبت:\n`wget -O install-nethunter-termux https://offs.ec/2Mws39s` \n"
            "3️⃣ إعطاء الصلاحية: `chmod +x install-nethunter-termux` \n"
            "4️⃣ بدء التنصيب: `./install-nethunter-termux`"
        )
        bot.send_message(cid, kali_ins, parse_mode='Markdown')

    # --- ميزات إضافية ---
    elif text == '🔍 فحص IP الذكي':
        bot.send_message(cid, "🌐 أرسل عنوان الـ IP الآن، وسأقوم بجلب الموقع الجغرافي، الدولة، والشركة المزودة فوراً.")

    elif text == '👨‍💻 المطور':
        dev_text = (
            f"👑 **معلومات الإمبراطور:**\n\n"
            f"👤 **الاسم:** {DEV_NAME}\n"
            f"🆔 **اليوزر:** {DEV_USER}\n"
            f"🛠️ **الرتبة:** {DEV_TITLE}\n\n"
            "خبير في البرمجة وأمن المعلومات. هذا البوت هو ثمرة تطوير مستمر لخدمة المجتمع التقني."
        )
        bot.send_message(cid, dev_text, parse_mode='Markdown')

    elif text == '🔙 القائمة الرئيسية':
        bot.send_message(cid, "🔙 تم الرجوع للقائمة الرئيسية.", reply_markup=main_menu())

# --- تشغيل المحرك ---
print(f"🛡️ [System Active] - Welcome Master {DEV_NAME}")
bot.polling(non_stop=True)
