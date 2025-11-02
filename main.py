from telegram import Update, InputMediaPhoto
from telegram.ext import (
    AIORateLimiter,
    Application,
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler,
)

from cache.buttons import REPLY_MARKUP
from config import TOKEN
from utils import get_buffer, get_position, make_move


async def start(u: Update, c: CallbackContext) -> int:
    c.user_data["chat_id"] = u.message.chat_id

    c.user_data["message_id"] = (
        await u.message.reply_text("👋", reply_markup=REPLY_MARKUP.START)
    ).message_id

    return STATE2


async def preparation(u: Update, c: CallbackContext) -> int:
    await u.callback_query.answer()

    get_position(c.user_data)

    buffer = get_buffer(c.user_data)
    caption = "Сделано ходов: 0"

    await u.callback_query.edit_message_media(
        InputMediaPhoto(buffer, caption, show_caption_above_media=True),
        REPLY_MARKUP.POSITIONS[15],
    )

    return STATE3


async def next_move(u: Update, c: CallbackContext) -> int:
    await u.callback_query.answer()
    answer = int(u.callback_query.data)

    win = make_move(c.user_data, answer)

    if win:
        await c.bot.delete_message(
            c.user_data["chat_id"],
            c.user_data["message_id"],
        )

        await c.bot.send_message(
            c.user_data["chat_id"],
            f"Победа! Сделано ходов: {c.user_data['moves']}",
        )

        return ConversationHandler.END

    buffer = get_buffer(c.user_data)
    caption = f"Сделано ходов: {c.user_data['moves']}"

    await u.callback_query.edit_message_media(
        InputMediaPhoto(buffer, caption, show_caption_above_media=True),
        REPLY_MARKUP.POSITIONS[answer],
    )

    return STATE3


async def stop(u: Update, c: CallbackContext) -> int:
    await c.bot.delete_message(
        c.user_data["chat_id"],
        c.user_data["message_id"],
    )

    await u.message.reply_text("Прохождение прервано")

    return ConversationHandler.END


if __name__ == "__main__":
    application = (
        Application.builder().rate_limiter(AIORateLimiter()).token(TOKEN).build()
    )

    conversation = ConversationHandler(
        [CommandHandler("start", start)],
        {
            (STATE2 := 2): [CallbackQueryHandler(preparation)],
            (STATE3 := 3): [CallbackQueryHandler(next_move)],
        },
        [CommandHandler("stop", stop)],
    )

    application.add_handler(conversation)

    application.run_polling(drop_pending_updates=True)
