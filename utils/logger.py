"""
Единая точка настройки логирования.
- setup_logging() выполняется один раз (вызывается из bot/__init__.py).
- get_logger(name) / setup_logger(name) ⇒ logging.getLogger(name)
  оставлены для обратной совместимости.
"""
import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

# ── директория logs ──────────────────────────────────────────────
LOG_DIR = Path(__file__).resolve().parents[1] / "logs"
LOG_DIR.mkdir(exist_ok=True)

# ── общие параметры ──────────────────────────────────────────────
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
FMT = "[%(asctime)s] [%(levelname)8s] %(name)s: %(message)s"
DATEFMT = "%d.%m.%Y %H:%M:%S"
FILE_MAX_BYTES = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 3


def setup_logging() -> None:
    """Глобальная настройка root-логгера (без повторной инициализации)."""
    root = logging.getLogger()
    if root.handlers:           # уже настроено
        return

    root.setLevel(LOG_LEVEL)

    # Console
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(logging.Formatter(FMT, datefmt=DATEFMT))
    root.addHandler(ch)

    # Rotating file
    fh = RotatingFileHandler(
        LOG_DIR / "bot.log",
        maxBytes=FILE_MAX_BYTES,
        backupCount=BACKUP_COUNT,
        encoding="utf-8",
    )
    fh.setFormatter(logging.Formatter(FMT, datefmt=DATEFMT))
    root.addHandler(fh)

    # Потише лишние библиотеки
    logging.getLogger("aiogram.event").setLevel("WARNING")
    logging.getLogger("aiohttp.access").setLevel("WARNING")


# ── совместимость со старым кодом ───────────────────────────────
def get_logger(name: str) -> logging.Logger:          # новое имя
    return logging.getLogger(name)


def setup_logger(name: str) -> logging.Logger:        # старое имя
    return logging.getLogger(name)
