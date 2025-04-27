"""Общие фикстуры для всех тестов."""
from pathlib import Path
import json
import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="session")
def animals():
    path = PROJECT_ROOT / "data" / "animals.json"
    return json.loads(path.read_text(encoding="utf-8"))


@pytest.fixture(scope="session")
def quiz_questions():
    path = PROJECT_ROOT / "data" / "quiz.json"
    return json.loads(path.read_text(encoding="utf-8"))
