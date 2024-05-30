import json
import sys

# Получение путей к файлам от пользователя
values_file_path = sys.argv[1]
tests_file_path = sys.argv[2]
report_file_path = sys.argv[3]

# Загрузка значений из JSON файла
with open(values_file_path, 'r', encoding='utf-8') as file:
    values = json.load(file)['values']

# Загрузка тестов из JSON файла
with open(tests_file_path, 'r', encoding='utf-8') as file:
    tests = json.load(file)['tests']

# Создание маппинга значений
value_map = {item['id']: item['value'] for item in values}

# Рекурсивная функция для применения значений
def apply_values(tests):
    for test in tests:
        if 'values' in test:
            apply_values(test['values'])
        if test['id'] in value_map:
            test['value'] = value_map[test['id']]

# Применение значений
apply_values(tests)

# Вывод результата в файл
with open(report_file_path, 'w', encoding='utf-8') as file:
    json.dump({'tests': tests}, file, indent=2, ensure_ascii=False)

print(f"Результаты сохранены в файл: {report_file_path}")
