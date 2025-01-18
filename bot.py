from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('VK_ACCESS_TOKEN')
GROUP_ID = os.getenv('ГРУППА_ИД')
API_VERSION = os.getenv('API_ВЕРСИЯ')

print(f"Токен: {TOKEN}")
print(f"ID группы: {GROUP_ID}")
print(f"Версия API: {API_VERSION}")


from dotenv import load_dotenv
import os

load_dotenv()

print(f"Токен VK: {os.getenv('VK_ACCESS_TOKEN')}")
print(f"ID группы: {os.getenv('GROUP_ID')}")
input("Нажми Enter для продолжения...")


from dotenv import load_dotenv  # Импортируем load_dotenv
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import os

# Загружаем переменные из .env
load_dotenv()

# Получаем токен и ID группы из переменных окружения
TOKEN = os.getenv('VK_ACCESS_TOKEN')
GROUP_ID = os.getenv('GROUP_ID')

# Проверяем, загрузился ли токен
print(f"Токен: {TOKEN}")
if not TOKEN:
    print("❗ Ошибка: Токен не загружен. Проверь .env файл.")
    input("Нажми Enter для выхода...")
    exit()

vk_session = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        vk.messages.send(
            user_id=event.user_id,
            message="Привет! Я бот и готов к работе 😊",
            random_id=0
        )
