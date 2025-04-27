from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

def rel(*parts: str) -> Path:
  """Возвращает абсолютный путь BASE_DIR / parts..."""
  return BASE_DIR.joinpath(*parts)