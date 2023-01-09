from servo_controller import ServoController
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hi!')

async def dice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_dice()

async def servo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Moving...')
    servo = ServoController(17, 90)
    servo.example3(5)
    servo.stop()
    await update.message.reply_text('Done.')

def main():
    app = Application.builder().token('5838289235:AAFv22bEgZK9Q5TRNPdQ9h1fp5w9A4aNusE').build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('servo', servo))
    app.add_handler(CommandHandler('dice', dice))
    app.run_polling()

if __name__ == '__main__':
    main()