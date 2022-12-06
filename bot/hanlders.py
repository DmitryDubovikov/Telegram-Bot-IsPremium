import abc
import telegram as tg
import telegram.ext as tg_ext
import typing as tp
from bot import messages

# Define a few command handlers. These usually take the two arguments update and
# context.

class BaseHandler(abc.ABC):

    def __init__(self) -> None:
        self.user: tp.Optional[tg.User] = None

    async def __call__(self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        self.user = update.effective_user
        self.messages = messages.get_messages(self.user)
        await self.handle(update, context)

    @abc.abstractmethod
    async def handle(self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        raise NotImplemented


class StartHandler(BaseHandler):
    async def handle(self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        """Send a message when the command /start is issued."""
        await update.message.reply_text(self.messages.start())


class HelpHandler(BaseHandler):
    async def handle(self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        """Send a message when the command /help is issued."""
        await update.message.reply_text(self.messages.help())


class EchoHandler(BaseHandler):
    async def handle(self, update: tg.Update, context: tg_ext.ContextTypes.DEFAULT_TYPE) -> None:
        """Echo the user message."""
        await update.message.reply_text(self.messages.echo(update.message.text))



def setup_handlers(application: tg_ext.Application) -> None:

    # on different commands - answer in Telegram
    application.add_handler(tg_ext.CommandHandler("start", StartHandler()))
    application.add_handler(tg_ext.CommandHandler("help", HelpHandler()))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(
        tg_ext.MessageHandler(tg_ext.filters.TEXT & ~tg_ext.filters.COMMAND, EchoHandler())
        )
