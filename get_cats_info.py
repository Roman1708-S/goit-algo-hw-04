from pathlib import Path


def get_cats_info(path):
    """
    Читає файл з інформацією про котів та повертає список словників.

    Args:
        path: Шлях до текстового файлу з даними про котів.

    Returns:
        list: Список словників з ключами "id", "name", "age".
    """
    cats_list = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # Пропускаємо порожні рядки

                try:
                    cat_id, name, age = line.split(',')
                    cat_info = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    cats_list.append(cat_info)
                except ValueError:
                    print(f"Некоректний рядок: '{line}'. Пропускаємо.")
                    continue

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return []
    except Exception as e:
        print(f"Виникла непередбачена помилка: {e}")
        return []

    return cats_list


# Визначаємо шлях до файлу відносно скрипта
base_path = Path(__file__).parent
file_path = base_path / "cats_file.txt"

cats_info = get_cats_info(file_path)
print(cats_info)