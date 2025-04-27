import pytest

from bot.services.scoring import choose_totem

@pytest.mark.parametrize(
    "answers, expected",
    [
        # все голоса за одно животное
        ([["tiger"], ["tiger"]], "tiger"),
        # несколько весов одного животного сильнее остальных
        ([["bear", "bear"], ["wolf"]], "bear"),
    ],
)
def test_choose_totem_dominant(answers, expected):
    assert choose_totem(answers) == expected


def test_choose_totem_tie_break(monkeypatch):
    """
    При равенстве баллов функция случайно выбирает
    одно из лидирующих животных.
    """
    answers = [["tiger"], ["bear"]]

    # подменяем random.choice, чтобы детерминировать поведение
    monkeypatch.setattr("bot.services.scoring.random.choice", lambda x: x[0])
    result = choose_totem(answers)
    assert result in {"tiger", "bear"}
