import pytest


def test_question_count(quiz_questions):
    """В викторине должно быть ровно 10 вопросов."""
    assert len(quiz_questions) == 10, "Количество вопросов не равно 10"


def test_question_ids_unique_sequential(quiz_questions):
    ids = [q["id"] for q in quiz_questions]
    assert ids == list(range(1, 11)), "ID вопросов должны быть 1‒10 без пропусков"


@pytest.mark.parametrize("field", ["question", "answers"])
def test_fields_presence(quiz_questions, field):
    """Каждый объект вопроса содержит обязательные поля."""
    assert all(field in q for q in quiz_questions), f"нет поля {field}"


def test_each_answer_has_weights(quiz_questions):
    for q in quiz_questions:
        assert all("weights" in ans and ans["weights"] for ans in q["answers"]), (
            f"в вопросе id={q['id']} есть ответ без 'weights'"
        )
