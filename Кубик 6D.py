import random

def throw_dice():
    """
    Бросает кубик и возвращает результат (от 1 до 6).
    """
    return random.randint(1, 6)

def choose_outcome(dice_result):
    """
    Выбирает, выпадет ли результат броска или нет.
    Возвращает True (выпадет) или False (не выпадет).
    """
    outcomes = {
        1: random.choice([True, False]),
        2: random.choice([True, False]),
        3: random.choice([True, False]),
        4: random.choice([True, False]),
        5: random.choice([True, False]),
        6: random.choice([True, False])
    }
    return outcomes[dice_result]

def play_game():
    """
    Основная логика игры.
    """
    results = {}  # Словарь для хранения статистики по выпавшим результатам
    all_results = set() # Множество для отслеживания уникальных выпавших результатов

    attempts = 0  # Счетчик попыток

    while len(all_results) < 6:
        attempts += 1
        dice_result = throw_dice()
        outcome = choose_outcome(dice_result)

        print(f"Попытка {attempts}: Выпало число {dice_result}. Результат - {outcome}")

        if outcome:  # Если выпало (True)
            if dice_result not in results:
                results[dice_result] = 1
                all_results.add(dice_result) # Добавляем в set для отслеживания
            else:
                results[dice_result] += 1  # Увеличиваем счетчик выпадений

        else:  # Если не выпало (False)
            print("Перебрасываем кубик...") # Указываем что нужно перебросить

        print("Текущая статистика:", results)
        print("-" * 20)

    print("\nВсе 6 вариантов броска выпали!")
    print(f"Общее количество попыток: {attempts}")
    print("Итоговая статистика:", results)



# Запуск игры
play_game()