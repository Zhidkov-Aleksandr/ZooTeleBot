from pathlib import Path
from aiogram.types import FSInputFile

PROJECT_ROOT = Path(__file__).resolve().parents[2]   # <корень проекта>

def animal_image(rel_path: str) -> FSInputFile:
    """
    rel_path – путь из animals.json, например 'media/images/tiger.jpg'
    Возвращает FSInputFile для aiogram.
    """
    abs_path = PROJECT_ROOT / rel_path
    return FSInputFile(abs_path)