from servo_controller import ServoController
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

MOVE = range(1)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    reply_keyboard = [["MOVE!"]]
    await update.message.reply_text(
            "Pulsa el botón",
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=True
            ),
        )
    return MOVE

async def move(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
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
    reply_keyboard = [["MOVE!"]]
    await update.message.reply_text(
        "Pulsa el botón",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True
        ),
    )
    return move

def main() -> None:
    application = Application.builder().token("5858370145:AAGZjnn5IAQR8GNoHd0bZ_nhMDli10bkBEo").build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            MOVE: [
                MessageHandler(filters.Regex("MOVE!"), move),
            ],
        },
        fallbacks=[CommandHandler("cancel", move)],
    )
    application.add_handler(conv_handler)
    application.run_polling()

if __name__ == "__main__":
    main()