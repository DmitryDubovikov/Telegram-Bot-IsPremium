import abc
import telegram as tg
import telegram.ext as tg_ext


class BaseMessages(abc.ABC):
    
    @abc.abstractmethod
    def start(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    def help(self) -> str:
        raise NotImplemented

    @abc.abstractmethod
    async def echo(self, text: str) -> str:
        raise NotImplemented


class RegularUserMessages(BaseMessages):

    def start(self) -> str:
        return 'Hello!'

    def help(self) -> str:
        return 'You should buy subscription'

    def echo(self, text: str) -> str:
        return f'{text}'


class PremiumUserMessages(RegularUserMessages):

    def start(self) -> str:
        return 'Welcome!'

    def help(self) -> str:
        return 'Our manager is on the way to you with blankets and cocoa!'

    # def echo(self, update: tg.Update, user: tg.User) -> str:
    #     update.message.reply_text(update.message.text)


def get_messages(user: tg.User) -> BaseMessages:
    if user.is_premium:
        return PremiumUserMessages()
    else:
        return RegularUserMessages()

