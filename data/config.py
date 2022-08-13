import os

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))  # Bot token
ADMINS = str(os.environ.get("ADMINS")).split() # adminlar ro'yxati
IP = str(os.environ.get("ip"))  # Xosting ip manzili

