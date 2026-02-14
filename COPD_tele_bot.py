import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# 1. Environment variables load karein
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# 2. Logging Setup (Real-time monitoring ke liye)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 3. Bot Functions
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/start command handler"""
    await update.message.reply_text("Bot Active Hai! Main 24/7 chalne ke liye ready hoon.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Normal messages handle karne ke liye"""
    user_input = update.message.text
    # Yahan aap apna logic (AI ya Database) baad mein add kar sakte hain
    await update.message.reply_text(f"Received: {user_input}")

if __name__ == '__main__':
    if not TOKEN:
        print("Error: BOT_TOKEN nahi mila! .env file check karein.")
    else:
        # 4. Application Build
        app = ApplicationBuilder().token(TOKEN).build()
        
        # 5. Handlers Add Karein
        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        
        print("Bot is starting...")
        # 6. Polling Mode (Local testing ke liye)
        app.run_polling()
