import config.config as config
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from paylink import short

TOKEN = config.TOKEN


def link_creator(url):

    if url.startswith('https://www.youtube.com/'):
        x = url.split('/')
        link = "https://www.youtubepi.com/" + x[3]
        link = short(link)['data'][-1]['short_url']

        link = '<a href="' + link + '">' + 'DOWNLOAD' + '</a>'
        return (link)
    else:
        if url.startswith('https://youtu.be'):
            x = url.split('/')
            link = "https://www.youtubepi.com/" + "watch?v=" + x[3]
            link = short(link)['data'][-1]['short_url']

            link = '<a href="' + link + '">' + 'DOWNLOAD' + '</a>'
            return (link)
        else:
            return False


async def start_commmand(update, context):
    await update.message.reply_text('Benvenuto: Inserisci un link youtube')


async def all(update, context):
    testo = update.message.text
    link = link_creator(testo)
    if link == False:
        await update.message.reply_text("<b>Inserisci un link YouTube valido!!!</b>", parse_mode="HTML")
    else:

        await update.message.reply_text(link, parse_mode="HTML", disable_web_page_preview=True)


if __name__ == '__main__':
    print('Starting a bot....')
    application = Application.builder().token(TOKEN).build()

    # Commands
    application.add_handler(CommandHandler('start', start_commmand))
    application.add_handler(MessageHandler(
        filters.BaseFilter(""), all))

    # Run bot
    application.run_polling(1.0)
