import json
import sys
import inspect

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

print(inspect.signature(load_json).return_annotation)

def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def update_values(tests, values_dict):
    for test in tests:
        test_id = test['id']
        if test_id in values_dict:
            test['value'] = values_dict[test_id]
        if 'values' in test:
            update_values(test['values'], values_dict)

def main(values_path, tests_path, report_path):
    values_data = load_json(values_path)
    tests_data = load_json(tests_path)
    
    values_dict = {entry['id']: entry['value'] for entry in values_data['values']}
    
    update_values(tests_data['tests'], values_dict)
    
    save_json(tests_data, report_path)

if __name__ == '__main__':
    values_path = 'values.json'
    tests_path = 'tests.json'
    report_path = 'report.json'
    
    main(values_path, tests_path, report_path)
