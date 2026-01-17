from vkbottle.bot import Bot, Message
from config import TOKEN
import random

bot = Bot(token=TOKEN)

@bot.on.message(text="/start")
async def start_handler(message: Message):
    await message.answer("Привет! Я умный бот на vkbottle")

@bot.on.message(text="/stop")
async def stop_handler(message: Message):
    await message.answer("Пока! Я умный бот на vkbottle")

@bot.on.message(text="/emoji")
async def emoji_handler(message: Message):
    emoji = ["😁", "😂", "😎", "😜", "😉", "😮", "😊", "🙄"]
    await message.answer(f"Вот такой эмодзи сегодня: {random.choice(emoji)}")

@bot.on.message(text="/dice")
async def stop_handler(message: Message):
    dice = random.randint(1, 6)
    await message.answer(f"Тебе выпало: {dice}")

@bot.on.message(text="/coin")
async def stop_handler(message: Message):
    result = random.choice(["Орёл", "Решка"])
    await message.answer(f"Выпало: {result}")

@bot.on.message(text="/8ball")
async def stop_handler(message: Message):
    answesrs = [
        "Да",
        "Нет",
        "Возможно",
        "Спроси позже",
        "100% да",
        "Я сомневаюсь"
    ]
    await message.answer("🎱 " + random.choice(answesrs))

@bot.on.message(text="/help")
async def stop_handler(message: Message):
    await message.answer(
        "Команды бота:\n\n"
        "/start - Старт бота\n"
        "/stop - Пока\n"
        "/emoji - Случайный смайлик\n"
        "/dice - Бросить кубик\n"
        "/coin - Подбросить монетку\n"
        "/8ball - Магический шар\n"
        "/help - Список команды"
    )

bot.run_forever()