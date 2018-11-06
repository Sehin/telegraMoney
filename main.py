from classes.DBWorker import DBWorker
from classes.TelegraMoneyBot import TelegraMoneyBot

def main():
    dbWorker = DBWorker()
    bot = TelegraMoneyBot(dbWorker, '513541660:AAFOKu6tSYuW489hcEURnJ57TtfmfpfEjE4')
    bot.polling()
    pass

if __name__=='__main__':
    main()