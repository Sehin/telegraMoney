from classes import TelegramBot
import time

class TelegraMoneyBot(TelegramBot.TelegramBot):

    def polling(self):
        while 1:

            for message in self.getMessages():
                # -----------------------------
                # ОСНОВНАЯ ОБРАБОТКА СОБЩЕНИЙ!!!
                # -----------------------------
                print(message.text)
                self.parseMessage(message)

            time.sleep(self.repeatRequestTime)

    def parseMessage(self, message):
        # Проход по листу состояния пользователей
        state = self._getUserFromStateList(message.chatId)
        if (state['state']==None):
            if message.text == '/start':
                self.sendMessage(message.chatId, 'Привет! Я помогу тебе считать твои финансы.\nДля начала стоит создать категорию (/category)\nДля вывода списка всех категорий - /allcategories')

        # Часть парсинга, когда есть состояние
        elif state['state'] == 'someState':

            state['state'] = None