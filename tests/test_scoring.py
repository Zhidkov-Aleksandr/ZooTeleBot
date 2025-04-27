import pytest

from bot.services.scoring import choose_totem


@pytest.mark.parametrize(
    "answers, expected",
    [
        ([["tiger"], ["tiger"]], {"tiger"}),
        ([["bear", "bear"], ["wolf"]], {"bear"}),
    ],
)
def test_choose_totem_dominant(answers, expected):
    """Победитель — животное с наибольшим числом «голосов»."""
    assert choose_totem(answers) in expected


def test_choose_totem_tie_break(monkeypatch):
    """При равенстве choose_totem случайно выбирает одного из лидеров."""
    answers = [["tiger"], ["bear"]]

    # фиксируем random.choice
    monkeypatch.setattr("bot.services.scoring.random.choice", lambda x: x[0])
    assert choose_totem(answers) in {"tiger", "bear"}
