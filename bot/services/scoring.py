import random
from collections import Counter
from typing import List

def choose_totem(answers: List[List[str]]) -> str:
    """
    answers – список списков весов (id животных), выбранных пользователем.
    Возвращает id животного-победителя.
    """
    flat = [item for sub in answers for item in sub]
    if not flat:
        return ""

    counts = Counter(flat)
    max_score = max(counts.values())
    leaders = [a for a, v in counts.items() if v == max_score]
    return random.choice(leaders)