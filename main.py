# # from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
# # from telegram import InlineKeyboardButton, InlineKeyboardMarkup
# #
# # updater = Updater(token="1012120777:AAF_eafnxtr9c2y4T6Bc2Fuika5R7taDIUM", use_context=True)
# # dp = updater.dispatcher
# #
# # aboutus = 'في أواخر عام 2019 تأسست تيرا' \
# #           ' للاتصالات وتكنولوجيا المعلومات كشركة متخصصة في مجال البرمجة' \
# #           ' والتقنية الحديثة في سبيل إحداث نقلة نوعية في عالم التكنولوجيا' \
# #           ' بما يواكب التطور الذي تشهده الدول في هذا المجال الرقمي، ' \
# #           'ومن أجل عالمنا العربي نحن نعمل على مدار الساعة لتكون تيرا أحد ' \
# #           'أكثر المجالات الرقمية أمانًا وخصوصية إدراكًا منّا أن ما يهم شريك ' \
# #           'نجاحنا هيّ جودة الخدمة المقدمة له، ولذلك نحن نسعى أيضًا لتطوير' \
# #           ' سياستنا بما يتوافق ويواكب بيئة العمل المتجددة على الدوام.'
# #
# # def start(update, context):
# #     update.message.reply_text(text="Mr: "+update.message.chat.first_name+" مرحبا بك كيف يمكننا خدمتك ")
# #     keyboard = [[InlineKeyboardButton("عن الشركة", callback_data='about_us')],
# #                 [InlineKeyboardButton("خدماتنا", callback_data='our_services')],
# #                 [InlineKeyboardButton("حساباتنا", callback_data='social_media')],
# #                 [InlineKeyboardButton("طرق التواصل معنا", callback_data='Connect')]]
# #     replymarkup = InlineKeyboardMarkup(keyboard)
# #     update.message.reply_text('الرجاء اختيار إحدى الخيارات التالية:', reply_markup=replymarkup)
# #
# #
# #
# # def button(update, context):
# #     query = update.callback_query
# #     query.answer()
# #     if query.data == 'about_us':
# #         query.edit_message_text(text=aboutus)
# #
# #     else :
# #         query.edit_message_text(text="Selected option: {}".format(query.data))
# #
# #
# # dp.add_handler(CommandHandler('start', start))
# # dp.add_handler(CallbackQueryHandler(button))
# # updater.start_polling()


import time

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters
import logging

aboutus = 'في أواخر عام 2019 تأسست تيرا' \
          ' للاتصالات وتكنولوجيا المعلومات كشركة متخصصة في مجال البرمجة' \
          ' والتقنية الحديثة في سبيل إحداث نقلة نوعية في عالم التكنولوجيا' \
          ' بما يواكب التطور الذي تشهده الدول في هذا المجال الرقمي، ' \
          'ومن أجل عالمنا العربي نحن نعمل على مدار الساعة لتكون تيرا أحد ' \
          'أكثر المجالات الرقمية أمانًا وخصوصية إدراكًا منّا أن ما يهم شريك ' \
          'نجاحنا هيّ جودة الخدمة المقدمة له، ولذلك نحن نسعى أيضًا لتطوير' \
          ' سياستنا بما يتوافق ويواكب بيئة العمل المتجددة على الدوام.'

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


logger = logging.getLogger(__name__)

# Stages
FIRST, SECOND = range(2)
# Callback data
ONE, TWO, THREE, FOUR , FIVE, SIX = range(6)

def start(update, context):
    """Send message on `/start`."""
    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    # Build InlineKeyboard where each button has a displayed text
    # and a string as callback_data
    # The keyboard is a list of button rows, where each row is in turn
    # a list (hence `[[...]]`).
    keyboard = [
         [InlineKeyboardButton("عن الشركة", callback_data=str(THREE))],
         [InlineKeyboardButton("خدماتنا", callback_data=str(TWO))],
         [InlineKeyboardButton("حساباتنا", callback_data=str(ONE))],
         [InlineKeyboardButton("طرق التواصل معنا", callback_data=str(FOUR))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    update.message.reply_text(
        "أهلا وسهلا بك يرجى إختيار إحدى الخيارات التالية",
        reply_markup=reply_markup
    )
    # Tell ConversationHandler that we're in state `FIRST` now
    return FIRST


def start_over(update, context):
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    keyboard = [
        [InlineKeyboardButton("عن الشركة", callback_data=str(THREE))],
        [InlineKeyboardButton("خدماتنا", callback_data=str(TWO))],
        [InlineKeyboardButton("حساباتنا", callback_data=str(ONE))],
        [InlineKeyboardButton("طرق التواصل معنا", callback_data=str(FOUR))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Instead of sending a new message, edit the message that
    # originated the CallbackQuery. This gives the feeling of an
    # interactive menu.
    query.edit_message_text(
        text="أهلا وسهلا بك يرجى إختيار إحدى الخيارات التالية",
        reply_markup=reply_markup
    )
    return FIRST


def one(update, context):
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton("تويتر", url="https://twitter.com/tera_cit") ],
        [InlineKeyboardButton("انستقرام", url="https://www.instagram.com/tera.cit/")],
        [InlineKeyboardButton("سناب شات", url="https://snapchat.com/add/tera_cit")],
        [InlineKeyboardButton("لينكدان", url="https://sa.linkedin.com/company/tera-cit")],
        [InlineKeyboardButton("الصفحة الرئيسية", callback_data=str(FIVE))],
        [InlineKeyboardButton("إغلاق الجلسة", callback_data=str(SIX))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="First CallbackQueryHandler, Choose a route",
        reply_markup=reply_markup
    )
    return FIRST


def two(update, context):
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton("طلب سعر", url="https://docs.google.com/forms/d/e/1FAIpQLSc6VDhCO-LbswyJblOJ_GaFdKptzNk2CCCx0ciMMSUphMWZsw/viewform")],
        [InlineKeyboardButton("طلب استشارة", url="https://docs.google.com/forms/d/e/1FAIpQLSf3KNI-cu0t2tF_tNGmLmQSe59hF1gwnbF4Ik282_leFaMZzg/viewform")],
        [InlineKeyboardButton("الصفحة الرئيسية", callback_data=str(FIVE)),
         InlineKeyboardButton("إغلاق الجلسة", callback_data=str(SIX))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="الرجاء اختيار نوع الخدمة المرغوبة",
        reply_markup=reply_markup
    )
    return FIRST


def three(update, context):
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton("الصفحة الرئيسية", callback_data=str(ONE)),
         InlineKeyboardButton("إغلاق الجلسة", callback_data=str(TWO))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text=aboutus,
        reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return SECOND


def four(update, context):
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton("الصفحة الرئيسية", callback_data=str(FIVE)),
         InlineKeyboardButton("إغلاق الجلسة", callback_data=str(SIX))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="يمكنك التواصل معنا عبر إحدى الطرق التالية:  هاتف: 0120215654  جوال: 058288555  البريد الإلكتروني: info@tera-cit.com",
        reply_markup=reply_markup
    )
    return FIRST



def end(update, context):
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over"""
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text="شكرا لك و نتطلع لخدمة مستقبلاً ^_^"
    )
    return ConversationHandler.END




def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater("1192608890:AAGb6_BWp3cYbOoXZFjib3GZKBpAa2mcGEc", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Setup conversation handler with the states FIRST and SECOND
    # Use the pattern parameter to pass CallbackQueries with specific
    # data pattern to the corresponding handlers.
    # ^ means "start of line/string"
    # $ means "end of line/string"
    # So ^ABC$ will only allow 'ABC'
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [CallbackQueryHandler(one, pattern='^' + str(ONE) + '$'),
                    CallbackQueryHandler(two, pattern='^' + str(TWO) + '$'),
                    CallbackQueryHandler(three, pattern='^' + str(THREE) + '$'),
                    CallbackQueryHandler(four, pattern='^' + str(FOUR) + '$'),
                    CallbackQueryHandler(start_over, pattern='^' + str(FIVE) + '$'),
                    CallbackQueryHandler(end, pattern='^' + str(SIX) + '$')],
            SECOND: [CallbackQueryHandler(start_over, pattern='^' + str(ONE) + '$'),
                     CallbackQueryHandler(end, pattern='^' + str(TWO) + '$')],
        },
        fallbacks=[CommandHandler('start', start)]
    )



    # Add ConversationHandler to dispatcher that will be used for handling
    # updates
    dp.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
