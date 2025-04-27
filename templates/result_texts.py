from typing import Dict

def build_result_text(animal: Dict[str, str]) -> str:
    return (
        f"<b>Твоё тотемное животное в Московском зоопарке — "
        f"{animal['name']}</b>\n\n"
        f"{animal['description']}\n\n"
        "🐾 <b>Программа опеки</b>\n"
        "Ты можешь стать опекуном своего тотемного зверя! "
        "Нажми кнопку «узнать больше», чтобы посмотреть подробности и оформить поддержку."
    )
