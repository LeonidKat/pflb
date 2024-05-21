import sys

array_length = int(sys.argv[1])
interval_length = int(sys.argv[2])



def find_cyclic_path_and_intervals(arr_length, m):
    arr = list(range(1, arr_length + 1))
    n = len(arr)
    path = []
    intervals = []
    
    # Начинаем с первого элемента массива
    current_index = 0
    
    while True:
        # Добавляем начальный элемент интервала в путь
        path.append(arr[current_index])
        
        # Формируем текущий интервал
        interval = []
        for i in range(m):
            interval.append(arr[(current_index + i) % n])
        
        # Добавляем интервал в список интервалов
        intervals.append(interval)
        
        # Переходим к следующему интервалу, который начинается с последнего элемента текущего интервала
        current_index = (current_index + m - 1) % n
        
        # Проверяем, не вернулись ли мы к началу
        if current_index == 0:
            break
    
    return path, intervals

path, intervals = find_cyclic_path_and_intervals(array_length, interval_length)

#print("Path:", path)
first_elements = [array[0] for array in intervals]
result = int(''.join(map(str, first_elements)))
print(result)
