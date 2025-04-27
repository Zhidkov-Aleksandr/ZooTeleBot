def test_animals_links_https(animals):
    """Все guardian_link должны начинаться с https://"""
    bad = [a["guardian_link"] for a in animals.values()
           if not a["guardian_link"].startswith("https://")]
    assert not bad, f"невалидные ссылки: {bad}"


def test_animals_images_exist(animals):
    """Проверяем, что для каждого животного указан существующий файл изображения."""
    from pathlib import Path
    root = Path(__file__).resolve().parents[1]

    missing = [a["image"] for a in animals.values()
               if not (root / a["image"]).exists()]

    assert not missing, f"отсутствуют файлы изображений: {missing}"
