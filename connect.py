# #
Connect_Version = '1.0'
import os, telebot
def cls(): os.system('clear')
#
print('Welcome to Delfi!')
print('\n\n    Press enter for start use')
input()
while True:
    cls()
    print('Enter request data in fields')
    print()
    hhtp_token = input('    Hhtp Token of Bot(telegram): ')
    print()
    usr_id = input('    User ID: ')
    cls()
    try:
        print('Connecting to telegram bot')
        error = 'TELEGRAM_BOT_CONNECT'
        tk = telebot.TeleBot(hhtp_token)
        cls()
        break
    except:
        cls()
        print(f'Error was occured, here a error code(traceback indifier): {error}')
        input()


