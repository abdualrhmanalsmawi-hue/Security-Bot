import telebot
import os
import threading
from telebot import types
from google import genai
from flask import Flask

TOKEN ='8586434472:AAF4lOQjf8WnwvKHyePxHS4JDKrZeH5HIgI'
bot = telebot.TeleBot(TOKEN)

# تعريف مفتاح الذكاء الاصطناعي والعميل لـ Gemini
GEMINI_API_KEY = "AQ.Ab8RN6Izye9nO-FUxhx34rpmDjUQVB4YDZWKpjJuB6dL6Jbr2w"
ai_client = genai.Client(api_key=GEMINI_API_KEY)

# كود Flask لحماية السيرفر من الإغلاق في Render بسبب المنافذ
app = Flask('')

@app.route('/')
def home():
    return "Al-Emperor Bot is running online! 🚀"

def run_flask():
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)
    
# معرف المالك الرئيسي
ADMIN_ID = 1036157698

# ═ { قائمة المستخدمين الدائمة والمحفوظة للأبد } ═
# يا إمبراطور، أي مستخدم جديد يأتيك إشعاره، قم بوضعه هنا في هذا الكشف ليبقى محفوظاً داخل الكود ولن يتم صفيره أبداً!
PERMANENT_USERS = [
    {"id": 1036157698, "name": "الامبراطور", "username": "@AL22009"},
    {"id": 5941829727, "name": "نصرالله", "username": "@لا يوجد يوزر"},
    {"id": 8113210715, "name": "-", "username": "@Scworld30"},
    {"id": 8799974075, "name": "..", "username": "@لا يوجد يوزر"}
]

# مصفوفة مؤقتة لتخزين الجلسة الحالية حتى لا تتكرر الإشعارات
session_users = []

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username if message.from_user.username else "لا يوجد"

    # التحقق هل المستخدم موجود في القائمة الدائمة أو الجلسة المؤقتة
    is_permanent = any(user["id"] == user_id for user in PERMANENT_USERS)
    
    if not is_permanent and user_id not in session_users:
        session_users.append(user_id)
        
        # إرسال إشعار فوري للمالك لكي يقوم بنسخ البيانات وإضافتها للكود عند تحديث GitHub
        alert = (f"🔔 **مستخدم جديد دخل البوت الآن!**\n"
                 f"⚠️ (قم بإضافته إلى القائمة الدائمة في الكود على GitHub)\n\n"
                 f"👤 **الاسم:** {first_name}\n"
                 f"🆔 **الآيدي:** `{user_id}`\n"
                 f"🧷 **اليوزر:** @{username}")
        bot.send_message(ADMIN_ID, alert, parse_mode="Markdown")
            
    # إنشاء لوحة التحكم بالشكل الاحترافي الموزع
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_ai = types.KeyboardButton('🤖 الذكاء الاصطناعي')
    btn_cyber = types.KeyboardButton('🛡️ الأمن السيبراني')
    btn_make = types.KeyboardButton('🛠️ صنع بوتات تلجرام')
    btn_dev = types.KeyboardButton('💁‍♂️ مطورو البوت')
    
    markup.add(btn_ai, btn_cyber)
    markup.add(btn_make)
    markup.add(btn_dev)
            
    test = f"أهلاً بك يا {first_name} في فريق ROOT—7 🙋‍♂️\nإختر من القائمة أدناه لتجربة النظام:" 
    bot.send_message(message.chat.id, test, reply_markup=markup)

# كود حساب وعرض كشوفات المستخدمين بالتفصيل للمالك فقط
@bot.message_handler(commands=['stats'])
def get_starts(message):
    if message.from_user.id == ADMIN_ID:
        total_users = len(PERMANENT_USERS)
        
        if total_users == 0:
            bot.send_message(message.chat.id, "📋 قائمة البيانات فارغة حالياً ولا يوجد زوار.")
            return

        # بناء التقرير المنظم والشامل للإمبراطور مستخرج من الكود الثابت مباشرة
        report = f"📊 **إحصائيات وكشف مستخدمي البوت الكلية**\n"
        report += f"👥 **العدد الإجمالي للمشتركين الثابتين:** `{total_users}`\n"
        report += f"═ { '═' * 15 } ═\n"
        report += "📋 **كشف بيانات المشتركين المحفوظة للأبد:**\n\n"
        
        for index, user in enumerate(PERMANENT_USERS, 1):
            report += f"{index}️⃣ **الاسم:** {user['name']}\n🆔 **الآيدي:** `{user['id']}`\n🧷 **اليوزر:** {user['username']}\n\n"
        
        bot.send_message(message.chat.id, report, parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, "❌ هذا الأمر مخصص لمالك النظام فقط.")

# ==========================================
#         🤖 محرك الذكاء الاصطناعي
# ==========================================
@bot.message_handler(func=lambda message: message.text == '🤖 الذكاء الاصطناعي')
def ai_welcome_msg(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton('⬅️ العودة للقائمة الرئيسية')
    markup.add(btn_back)

    msg = bot.send_message(message.chat.id, "🤖 مرحباً بك في محرّك الذكاء الاصطناعي الخاص بفريق ROOT—7!\nاكتب سؤالك أو استفسارك الآن وسأجيبك فوراً:", reply_markup=markup)
    bot.register_next_step_handler(msg, call_gemini_ai)

def call_gemini_ai(message):
    if message.text == '⬅️ العودة للقائمة الرئيسية':
        send_welcome(message)
        return

    bot.send_chat_action(message.chat.id, 'typing')
    
    try:
        response = ai_client.models.generate_content(
            model='gemini-2.5-flash',
            contents=message.text,
        )
        bot.send_message(message.chat.id, response.text, parse_mode="Markdown")
        
        msg = bot.send_message(message.chat.id, "✨ اسألني عن أي شيء آخر، أو اضغط على زر العودة بالأسفل:")
        bot.register_next_step_handler(msg, call_gemini_ai)
        
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ حدث خطأ أثناء الاتصال بمحرك الذكاء الاصطناعي: {e}")

# دالة مخصصة لتنظيف الاتصال وبدء الـ Polling
def start_bot_polling():
    try:
        bot.delete_webhook(drop_pending_updates=True)
        print("[Telegram] Webhook deleted successfully. Starting Polling...")
    except Exception as e:
        print(f"[Telegram] Error deleting webhook: {e}")
        
    bot.polling(none_stop=True)

if __name__ == "__main__":
    t = threading.Thread(target=start_bot_polling)
    t.start()
    run_flask()
