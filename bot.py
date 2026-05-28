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
    
# كود الرسالة الترحيبية للمستخدم
ADMIN_ID = 1036157698
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username

    file_name = "users.txt"
    if not os.path.exists(file_name): 
        with open(file_name, "w") as f:
            pass
    with open(file_name, "r") as f:
        exiting_users = f.read().splitlines()

    if str(user_id) not in exiting_users:
        with open(file_name, "a") as f:
            f.write(f"{user_id}\n")
            alert = ( f" مستخدم جديد دخل البوت الآن !**🔔 \n\n"
            f"👤 الاسم : {first_name}\n"
            f"🆔 الآيدي : `{user_id}`\n"
            f"🧷 اليوزر : @{username if username else 'لا يوجد يوزر '}" )
        bot.send_message(ADMIN_ID, alert, parse_mode="Markdown")
            
    # إنشاء لوحة التحكم بشكل صريح لإجبار الأزرار على الظهور
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    # تعريف الأزرار الثلاثة منفصلة بشكل صحيح
    btn_ai = types.KeyboardButton('🤖 الذكاء الاصطناعي')
    btn_cyber = types.KeyboardButton('🛡️ الأمن السيبراني')
    btn_make = types.KeyboardButton('🛠️ صنع بوتات تلجرام ')
    btn_dev = types.KeyboardButton('💁‍♂️ مطورو البوت')
    
    # توزيع الأزرار: أول زرين بجانب بعضهما، والزر الثالث في سطر منفصل بالأسفل
    markup.add(btn_ai, btn_cyber)
    markup.add(btn_make)
    markup.add(btn_dev)
            
    test = f"أهلاً بك يا {first_name} في فريق ROOT—7 🙋‍♂️\nإختر من القائمة أدناه لتجربة النظام:" 
    bot.send_message(message.chat.id, test, reply_markup=markup)

# كود حساب عدد المستخدمين الذين زاروا البوت
@bot.message_handler(commands=['stats'])
def get_starts(message):
    if message.from_user.id == ADMIN_ID:
        file_name = "users.txt"
        if os.path.exists(file_name):
            with open(file_name, "r") as f:
                total_users = len(f.read().splitlines())
                bot.send_message(message.chat.id, f"** إحصائيات البوت الكلية 📊**\n\n👥 عدد المستخدمين من بداية الانشاء: `{total_users}`")
        else:
            bot.send_message(message.chat.id, "❌ لا توجد بيانات حالياً.")
    else:
        bot.send_message(message.chat.id, "❌ هذا الأمر مخصص لمالك النظام فقط. ")

# ==========================================
#         🤖 محرك الذكاء الاصطناعي
# ==========================================
@bot.message_handler(func=lambda message: message.text == '🤖 اسأل الذكاء الاصطناعي')
def ai_welcome_msg(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton('⬅️ العودة للقائمة الرئيسية')
    markup.add(btn_back)

    msg = bot.send_message(message.chat.id, "🤖 مرحباً بك في محرّك الذكاء الاصطناعي لجيميني!\nاكتب سؤالك أو استفسارك الآن وسأجيبك فوراً:", reply_markup=markup)
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
        # 🔥 الأمر السحري لحذف أي Webhook قديم مسبب للتعارض وحل المشكلة تماماً!
        bot.delete_webhook(drop_pending_updates=True)
        print("[Telegram] Webhook deleted successfully. Starting Polling...")
    except Exception as e:
        print(f"[Telegram] Error deleting webhook: {e}")
        
    bot.polling(none_stop=True)

if __name__ == "__main__":
    # 1. تشغيل البوت في خيط مستقل
    t = threading.Thread(target=start_bot_polling)
    t.start()
    
    # 2. تشغيل Flask في الخيط الأساسي ليمسك الـ Port فوراً في Render
    run_flask()
