import os
import telebot

# Telegram Bot Token
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "👋 မင်္ဂလာပါ! mg Zhang (DD MLBB Auto Topup) မှ ကြိုဆိုပါတယ်ခင်ဗျာ။\n\n"
        "💎 MLBB Diamond များကို သက်သာသော ဈေးနှုန်းဖြင့် အလိုအလျောက် ဝယ်ယူနိုင်ပါပြီ။\n\n"
        "စတင်ရန် အောက်ပါ Menu များကို အသုံးပြုနိုင်ပါသည်။"
    )
    bot.reply_to(message, welcome_text)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "ဝယ်ယူလိုသော Diamond ပမာဏနှင့် Player ID ကို ပို့ပေးပါခင်ဗျာ။")

if __name__ == "__main__":
    bot.infinity_polling()
  
