import telebot
import os
from telebot import types

TOKEN ='8711639465:AAGHtPQ1J4ft1mDzNkhvfYy7bDZNUlNYcGQ'
bot = telebot.TeleBot(TOKEN)

# كود الرسالة الترحيبة للمستخدم
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
        bot.send_message(ADMIN_ID,alert, parse_mode="Markdown")
            
    test = "فريق ROOT—7 يرحب بكم 🙋‍♂️" 
    bot.send_message(message.chat.id,test)

# كود حساب عدد المستخدمين الذين زاروا البوت
@bot.message_handler(commands = ['stats'])
def get_starts(message):
    if message.from_user.id == ADMIN_ID:
        file_name = "users.txt"
        if os.path.exists(file_name):
            with open(file_name, "r") as f:
                total_users = len(f.read().splitlines())
                bot.send_message(message.chat.id,f"** إحصائيات البوت الكلية 📊**\n\n👥 عدد المستخدمين من بداية الانشاء: `{total_users}`")

        else:
            bot.send_message(message.chat.id, "❌ هاذا الأمر مخصص لمالك النظام فقط. ")
bot.polling(none_stop=True)
