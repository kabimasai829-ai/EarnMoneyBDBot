from telegram import (
    Update,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = 8845526256:AAEq9zBWy0Jlw-5A1fV-q2OVqa9IGod20AE

ADMIN_IDS = [
    8265796059,
    8394671293,
    8245026674,
]

CHANNEL_USERNAME = @EarnMoneyBD721_bot

GIFT, NUMBER = range(2)

keyboard = [
    ["🎁 Gift Code", "💰 My Wallet"],
    ["📱 Instagram Sell", "📘 Facebook Sell"],
    ["📧 Gmail Sell", "👥 Referral"],
    ["📢 Join Channel", "📅 Meeting"],
]

reply_markup = ReplyKeyboardMarkup(
    keyboard,
    resize_keyboard=True
)
