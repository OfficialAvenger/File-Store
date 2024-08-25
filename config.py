#(©)t.me/CodeFlix_Bots




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "21756679"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "df14cb5cdc1e0fa9ce68e317abe8ab64")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002235235558"))
# NAMA OWNER
OWNER = os.environ.get("OWNER", "ProSangram")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6485380150"))
#Port
PORT = os.environ.get("PORT", "8030")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Bikash:Bikash@bikash.yl2nhcy.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001949485656"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001653929459"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://graph.org//file/9e75429027a83369f28b6.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://graph.org//file/7d2ae65e0f4d7e6b3089f.jpg")

HELP_TXT = "<b>ᴛʜɪs ɪs ᴀɴ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ @Red_Wine_Op\n\n ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/AvengerOwner>ᴀᴠᴇɴɢᴇʀ ᴏᴡɴᴇʀ</a></b>"
ABOUT_TXT = "<b>◈ ᴄʀᴇᴀᴛᴏʀ: <a https://t.me/AvengerOwner>ᴀᴠᴇɴɢᴇʀ ᴏᴡɴᴇʀ</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/Red_Wine_Op>ʀᴇᴅ ᴡɪɴᴇ ɢʀᴏᴜᴘ</a>\n◈ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/AvengerNews>ᴀᴠᴇɴɢᴇʀ ɴᴇᴡs</a></b>"
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʏ!! {first}\n\n ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.</b>")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "6485380150 6485380150").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>ʜᴇʟʟᴏ {first}\n\nᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʀʏ ᴀɢᴀɪɴ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @Red_Wine_Op</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>ʜᴇʟʟᴏ ᴜsᴇʀ\n\n<u>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs</u>-> @Red_Wine_Op\n-> @AvengerNews\n-> @Movies_Bull\n-> @Kalakar_Sangram\n-> @AvengerOwner</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(5191566338)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
