from servo_controller import ServoController
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hi!')

async def dice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_dice()

async def move(update: Update, context: ContextTypes.DEFAULT_TYPE):
    angle = '90'
    try:
        f = open('last_angle.txt', 'r')
        angle = f.readline()
        angle = angle.replace('\n', '')
        f.close()
    except:
        await update.message.reply_text('Can not read file')
    servo = ServoController(17, int(angle))
    if int(angle) == 45:
        new_angle = 135
    elif int(angle) == 135:
        new_angle = 45
    else:
        new_angle = 45
    print(new_angle)
    servo.stop()
    servo.degree(new_angle)
    try:
        f = open('last_angle.txt', 'w')
        f.write(str(new_angle))
        f.close()
    except:
        await update.message.reply_text('Can not write file')

async def servo1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Moving...')
    servo = ServoController(17, 90)
    servo.degree(0)
    servo.degree(45)
    servo.degree(90)
    servo.degree(135)
    servo.degree(180)
    servo.degree(135)
    servo.degree(90)
    servo.degree(45)
    servo.degree(0)
    servo.stop()
    await update.message.reply_text('Done.')

async def servo3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Moving...')
    servo = ServoController(17, 90)
    for i in range(0, 5):
        servo.degree(0)
        servo.degree(180)
    servo.stop()
    await update.message.reply_text('Done.')

async def servo4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Moving...')
    servo = ServoController(17, 90)
    for i in range(0, 5):
        servo.degree(90)
        servo.degree(45)
        servo.degree(135)
        servo.degree(0)
        servo.degree(180)
        servo.degree(45)
        servo.degree(135)
        servo.degree(90)
    servo.stop()
    await update.message.reply_text('Done.')

def main():
    app = Application.builder().token('5838289235:AAFv22bEgZK9Q5TRNPdQ9h1fp5w9A4aNusE').build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('servo1', servo1))
    app.add_handler(CommandHandler('move', move))
    app.add_handler(CommandHandler('servo3', servo3))
    app.add_handler(CommandHandler('servo4', servo4))
    app.add_handler(CommandHandler('dice', dice))
    app.run_polling()

if __name__ == '__main__':
    main()