import telebot
import os
import threading
import json
from telebot import types
from google import genai
from flask import Flask

# ==========================================
#           إعدادات البوت
# ==========================================

TOKEN = "8586434472:AAF4lOQjf8WnwvKHyePxHS4JDKrZeH5HIgI"
bot = telebot.TeleBot(TOKEN)

GEMINI_API_KEY = "AQ.Ab8RN6J4M0ISba5SUQnAgL9szzAHx6Hn0Qvrbseu89yHnuBXUw"
ai_client = genai.Client(api_key=GEMINI_API_KEY)

ADMIN_ID = 1036157698

# ==========================================
#           حفظ المستخدمين
# ==========================================

USERS_FILE = "users.json"

def load_users():
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []
    return []

def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)

PERMANENT_USERS = load_users()

# ==========================================
#              Flask
# ==========================================

app = Flask(__name__)

@app.route('/')
def home():
    return "ROOT-7 Bot is running! 🚀"

def run_flask():
    port = int(os.environ.get('PORT', 10000))
    app.run(
        host='0.0.0.0',
        port=port,
        debug=False,
        use_reloader=False
    )

# ==========================================
#            القائمة الرئيسية
# ==========================================

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn_ai = types.KeyboardButton('🤖 الذكاء الاصطناعي')
    btn_cyber = types.KeyboardButton('🛡️ الأمن السيبراني')
    btn_make = types.KeyboardButton('🛠️ صنع بوتات تلجرام')
    btn_dev = types.KeyboardButton('💁‍♂️ مطورو البوت')

    markup.add(btn_ai, btn_cyber)
    markup.add(btn_make)
    markup.add(btn_dev)

    return markup

# ==========================================
#              /start
# ==========================================

@bot.message_handler(commands=['start'])
def send_welcome(message):

    user_id = message.from_user.id
    first_name = message.from_user.first_name or "بدون اسم"

    username = (
        f"@{message.from_user.username}"
        if message.from_user.username
        else "@لا يوجد يوزر"
    )

    # التحقق هل المستخدم موجود مسبقاً
    is_exists = any(user["id"] == user_id for user in PERMANENT_USERS)

    # إذا كان جديد يتم حفظه
    if not is_exists:

        new_user = {
            "id": user_id,
            "name": first_name,
            "username": username
        }

        PERMANENT_USERS.append(new_user)

        save_users(PERMANENT_USERS)

        # إشعار للمالك
        alert = (
            f"🔔 مستخدم جديد دخل البوت!\n\n"
            f"👤 الاسم: {first_name}\n"
            f"🆔 الآيدي: {user_id}\n"
            f"🧷 اليوزر: {username}\n\n"
            f"✅ تم حفظه تلقائياً"
        )

        bot.send_message(ADMIN_ID, alert)

    text = (
        f"أهلاً بك يا {first_name} 🙋‍♂️\n"
        f"مرحباً بك في فريق ROOT—7\n\n"
        f"اختر من القائمة أدناه:"
    )

    bot.send_message(
        message.chat.id,
        text,
        reply_markup=main_menu()
    )

# ==========================================
#              /stats
# ==========================================

@bot.message_handler(commands=['stats'])
def stats(message):

    if message.from_user.id != ADMIN_ID:
        bot.send_message(
            message.chat.id,
            "❌ هذا الأمر خاص بمالك البوت فقط"
        )
        return

    total_users = len(PERMANENT_USERS)

    if total_users == 0:
        bot.send_message(
            message.chat.id,
            "📭 لا يوجد مستخدمين حالياً"
        )
        return

    report = (
        f"📊 إحصائيات البوت\n"
        f"👥 عدد المستخدمين: {total_users}\n\n"
        f"📋 كشف المستخدمين:\n\n"
    )

    for index, user in enumerate(PERMANENT_USERS, start=1):

        report += (
            f"{index}️⃣ الاسم: {user['name']}\n"
            f"🆔 الآيدي: {user['id']}\n"
            f"🧷 اليوزر: {user['username']}\n\n"
        )

    bot.send_message(message.chat.id, report)

# ==========================================
#        الذكاء الاصطناعي Gemini
# ==========================================

@bot.message_handler(func=lambda message: message.text == '🤖 الذكاء الاصطناعي')
def ai_menu(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn_back = types.KeyboardButton('⬅️ العودة للقائمة الرئيسية')

    markup.add(btn_back)

    msg = bot.send_message(
        message.chat.id,
        "🤖 أرسل سؤالك الآن:",
        reply_markup=markup
    )

    bot.register_next_step_handler(msg, call_gemini)

def call_gemini(message):

    if message.text == '⬅️ العودة للقائمة الرئيسية':

        bot.send_message(
            message.chat.id,
            "🏠 تم الرجوع للقائمة الرئيسية",
            reply_markup=main_menu()
        )

        return

    bot.send_chat_action(message.chat.id, 'typing')

    try:

        response = ai_client.models.generate_content(
            model='gemini-2.5-flash',
            contents=message.text
        )

        bot.send_message(
            message.chat.id,
            response.text
        )

        msg = bot.send_message(
            message.chat.id,
            "✨ أرسل سؤالاً آخر:"
        )

        bot.register_next_step_handler(msg, call_gemini)

    except Exception as e:

        bot.send_message(
            message.chat.id,
            f"❌ حدث خطأ:\n{e}"
        )

# ==========================================
#          رسائل الأقسام الأخرى
# ==========================================

@bot.message_handler(func=lambda message: message.text == '🛡️ الأمن السيبراني')
def cyber(message):

    bot.send_message(
        message.chat.id,
        "🛡️ قسم الأمن السيبراني قيد التطوير..."
    )

@bot.message_handler(func=lambda message: message.text == '🛠️ صنع بوتات تلجرام')
def make_bot(message):

    bot.send_message(
        message.chat.id,
        "🛠️ قسم صناعة البوتات قيد التطوير..."
    )

@bot.message_handler(func=lambda message: message.text == '💁‍♂️ مطورو البوت')
def devs(message):

    bot.send_message(
        message.chat.id,
        "👨‍💻 فريق ROOT—7"
    )

# ==========================================
#           تشغيل البوت
# ==========================================

def start_bot():

    try:
        bot.delete_webhook(drop_pending_updates=True)
        print("Webhook deleted successfully")

    except Exception as e:
        print(e)

    bot.infinity_polling()

# ==========================================
#                MAIN
# ==========================================

if __name__ == "__main__":

    t = threading.Thread(target=start_bot)

    t.start()

    run_flask()
