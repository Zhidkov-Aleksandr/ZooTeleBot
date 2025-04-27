# Telegram-бот «Тотемное животное» 
# 🦒 🐘 🦁 

#
Викторина Московского зоопарка: ответь на 10 вопросов и узнай, кто ты сегодня — Тигр, Жираф или, может быть, Кролик.

## Возможности
* Дружелюбное /start-приветствие и inline-кнопки.  
* 10 настраиваемых вопросов ( `data/quiz.json` ).  
* Алгоритм «взвешивания» ответов → выбор животного-тотема.  
* Фото и описание тотема + кнопки:
  * «Узнать больше» о программе опеки;
  * «Поделиться результатом».  
* Сбор контактов (`/contact`) и отзывов (`/feedback <текст>`).  
* Логи, простые текстовые хранилища данных, готовность к Webhook.  
* Тесты pytest.

## Быстрый старт

```bash
# Python 3.13+
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

export BOT_TOKEN="ВАШ_TELEGRAM_TOKEN"  # Windows: set BOT_TOKEN=...

python -m bot.main
