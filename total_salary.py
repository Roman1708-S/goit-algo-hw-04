def total_salary(path):
    """
    Аналізує файл із заробітними платами та повертає загальну та середню суму.
    
    Args:
        path (str): Шлях до текстового файлу із зарплатами.
        
    Returns:
        tuple: Кортеж (загальна_сума, середня_зарплата) або (0, 0) у разі помилки.
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
            if not lines:
                print("Файл порожній.")
                return (0, 0)
            
            total = 0
            count = 0
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue  # Пропускаємо порожні рядки
                
                try:
                    name, salary = line.split(',')
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"Некоректний рядок у файлі: '{line}'. Пропускаємо.")
                    continue
            
            if count == 0:
                print("Не знайдено жодного коректного запису.")
                return (0, 0)
            
            average = total / count
            return (total, average)
    
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return (0, 0)
    except PermissionError:
        print(f"Немає доступу до файлу '{path}'.")
        return (0, 0)
    except Exception as e:
        print(f"Виникла непередбачена помилка: {e}")
        return (0, 0)


# Використання функції
total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")