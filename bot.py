from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8552954802:AAERtD5w0Im-OO_5u0Qky4du6ZIktt0iikI"
DEPOSIT_ADDRESS = "0x65F06E1c8e6CE17998e642A18c3E95b255CF7d96"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Welcome to PROFIT LOOP\n\n"
        "💰 Daily Profit: 4%\n"
        "⏳ Duration: 30 Days\n"
        "🔒 Capital Lock: 30 Days\n\n"
        "📥 Deposit Address:\n"
        f"{DEPOSIT_ADDRESS}\n\n"
        "⚠️ ONLY SEND POL\n\n"
        "Commands:\n"
        "/deposit\n"
        "/withdraw\n"
        "/support"
    )

async def deposit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"📥 Send POL to:\n{DEPOSIT_ADDRESS}\n\nONLY SEND POL"
    )

async def withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💸 Withdrawals are MANUAL.\nContact admin with TX history."
    )

async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛠 Support: Contact Admin on Telegram"
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("deposit", deposit))
app.add_handler(CommandHandler("withdraw", withdraw))
app.add_handler(CommandHandler("support", support))

print("Bot running...")
app.run_polling()
