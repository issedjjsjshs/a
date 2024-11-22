from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "29079918")) #لا تغير هاذة القيمة
API_HASH = getenv("API_HASH", "71b391620d815580a5d3a571efa4f211")#لا تغير هاذة القيمة
BOT_TOKEN = getenv("BOT_TOKEN", "7847311283:AAGAiDS9DBGMrVlxOUVY_XAclKwMjy9s9R8")
SESSION_NAME = getenv("SESSION_NAME", "AgCIVfMALNM8vUP9teFaYem58oq7CpSToO5x3tbYmZ0kg8FVuEnEt2yXCAHCPxK8XWXZENz1m3BTFj7nJBBz1h9eXppTNKcajV3lA7V1XsULHUBxfXZiSPHuFD648BjLkZGC4rAL3oexnbHei70VXDFOsI07CROjWpxI-DPgOxPM7zEfSzSMFviK4jyRFVguf37_S97x93yQPdo1RiPnnJKd8lVm_ERnTeGWtvHgjkN_7UXo6iGVnuozyGquF-jhmTkLHf2iJo6SqrSO_ubfAY7ot-KAVm-1dV_0Z5nONOhVYYIcAq05ZYLjWReu3peLkimIFCTxGTZo5fcVwxPNib8YO6znnAAAAAGDpgDoAA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "ijhghjf") # @ هنا ضع يوزر حسابك بدون 
ALIVE_NAME = getenv("ALIVE_NAME", "تيو") # هنا ضع اسم حسابك
BOT_USERNAME = getenv("BOT_USERNAME", "isshskbot") # @ هنا ضع يوزر البوت بدون 
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/X02lx/RrRRR") 
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main") #لا تغير هاذة القيمة
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60")) #لا تغير هاذة القيمة
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "iFlne") # @ هنا ضغ يوزر كروبك بدون 
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "iFlne") # @ هنا ضغ يوزر قناتك بدون

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "6503661800").split()))
                                             #هنا ضع ايدي المطور فوق و الاعلئ
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6503661800").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
