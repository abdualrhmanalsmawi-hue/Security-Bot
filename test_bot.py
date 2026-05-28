import os
import threading
from flask import Flask
import telebot
from google import genai

# 1. إعداد خادم ويب Flask وهمي لإرضاء خوادم Render وفتح المنفذ (Port)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running perfectly!"

def run_flask():
    # Render يمرر المنفذ تلقائياً عبر متغير البيئة PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

# 2. إعداد التوكنات والمفاتيح بأمان (تمنع حظر جيت هاب وتحمي بياناتك)
# تأكد من وضع المفاتيح الحقيقية هنا أو عبر الـ Environment Variables في ريندر
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7963364506:AAElSg7V_U4w_XlA97-0vR8f-Xq0bXz978c") 
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "ضع_مفتاح_جيميني_الجديد_هنا")

bot = telebot.TeleBot(BOT_TOKEN)
ai_client = genai.Client(api_key=GEMINI_API_KEY)

# حالات المستخدمين لتتبع المحادثة مع جيميني
user_states = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # كود الترحيب والأزرار الخاص بك
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = telebot.types.KeyboardButton("🤖 اسأل الذكاء الاصطناعي")
    markup.add(btn)
    bot.reply_to(message, f"👋 أهلاً بك يا {message.from_user.first_name} في فريق ROOT-7!\nإختر من القائمة أدناه لتجربة النظام:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "🤖 اسأل الذكاء الاصطناعي")
def ai_mode(message):
    user_states[message.chat.id] = 'AI_MODE'
    bot.reply_to(message, "🤖 مرحباً بك في محرك الذكاء الاصطناعي لجيميني!\nاكتب سؤالك أو استفسارك الآن وسأجيبك فوراً:")

@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'AI_MODE')
def handle_ai_request(message):
    if message.text == " العودة للقائمة الرئيسية":
        user_states[message.chat.id] = None
        bot.reply_to(message, "تمت العودة للقائمة الرئيسية.")
        return

    try:
        # إرسال الطلب إلى موديل جيميني المستقر
        response = ai_client.models.generate_content(
            model='gemini-2.5-flash',
            contents=message.text
        )
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, f" حدث خطأ أثناء الاتصال بمحرك الذكاء الاصطناعي:\n{str(e)}")

# 3. تشغيل النظام عبر الـ Threads الموازية لمنع التعارض
if __name__ == "__main__":
    # تشغيل سيرفر ويب Flask في الخلفية لفتح البورت فوراً لـ Render
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    # تنظيف اتصالات التليجرام وبدء استقبال الرسائل
    try:
        bot.delete_webhook(drop_pending_updates=True)
    except:
        pass
        
    print("🚀 Server is live and Bot is listening...")
    bot.polling(none_stop=True, skip_pending_updates=True)
