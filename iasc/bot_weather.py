import telebot
import requests
import logging

# Налаштування логування
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

import os
import telebot

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")  # читаем переменную окружения
OWM_API_KEY = os.getenv("OWM_API_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def get_weather(city):
    logging.info(f"Отримання погоди для міста: {city}")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OWM_API_KEY}&units=metric&lang=ru"
    response = requests.get(url)
    
    if response.status_code != 200:
        logging.warning(f"Помилка HTTP: {response.status_code}")
        return None
    
    data = response.json()
    if data.get("cod") != 200:
        logging.warning(f"Відповідь API містить помилку: {data.get('message')}")
        return None

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    weather_report = (
        f"Погода в городе {city}:\n"
        f"Температура: {temp}°C\n"
        f"Состояние: {desc}\n"
        f"Влажность: {humidity}%\n"
        f"Скорость ветра: {wind_speed} м/с"
    )
    logging.info(f"Успішно отримано прогноз для {city}")
    return weather_report

@bot.message_handler(commands=["start"])
def send_welcome(message):
    logging.info(f"/start від {message.from_user.id}")
    bot.reply_to(message, "Привет! Напиши название города, и я скажу погоду.")

@bot.message_handler(commands=['help'])
def send_help(message):
    logging.info(f"/help від {message.from_user.id}")
    help_text = (
        "Привіт! Я бот, який може повідомити погоду у вашому місті.\n\n"
        "Команди:\n"
        "/start - запустити бота\n"
        "/help - отримати цю довідку\n"
        "Просто надішліть назву міста, і я скажу погоду там."
    )
    bot.send_message(message.chat.id, help_text)

@bot.message_handler(func=lambda message: True)
def send_weather(message):
    city = message.text.strip()
    logging.info(f"Запит погоди від {message.from_user.id}: '{city}'")
    weather = get_weather(city)
    if weather:
        bot.reply_to(message, weather)
    else:
        bot.reply_to(message, "Не удалось получить данные о погоде. Проверьте название города.")
        logging.error(f"Не вдалося отримати погоду для: {city}")

if __name__ == "__main__":
    logging.info("Бот запущен...")
    bot.infinity_polling()
