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
TOKEN ='8711639465:AAGHtPQ1J4ft1mDzNkhvfYy7bDZNUlNYcGQ'
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
'
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
