import math, sys

def read_circle_data(filename):
    # Функция для чтения данных о круге из файла
    with open(filename, 'r') as file:  # Открытие файла на чтение
        xc, yc = map(float, file.readline().strip().split())  # Считывание первой строки (координаты центра)
        r = float(file.readline().strip())  # Считывание второй строки (радиус)
    return xc, yc, r  # Возврат координат центра и радиуса круга

def read_points_data(filename):
    # Функция для чтения координат точек из файла
    with open(filename, 'r') as file:  # Открытие файла на чтение
        lines = file.readlines()  # Считывание всех строк из файла
        # Преобразование строк в список кортежей с координатами точек
        points = [tuple(map(float, line.strip().split())) for line in lines]
    return points  # Возврат списка координат точек

def determine_point_position(xc, yc, r, xt, yt):
    # Функция для определения положения точки относительно окружности
    distance = math.sqrt((xt - xc) ** 2 + (yt - yc) ** 2)  # Вычисление расстояния между точкой и центром окружности
    if math.isclose(distance, r):  # Проверка, лежит ли точка на окружности
        return "0"  # Возврат значения "0", если точка лежит на окружности
    elif distance < r:  # Проверка, находится ли точка внутри окружности
        return "1"  # Возврат значения "1", если точка внутри окружности
    else:  # Если точка не лежит на окружности и не внутри неё
        return "2"  # Возврат значения "2", если точка снаружи окружности

def main():
    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    xc, yc, r = read_circle_data(circle_file)  # Чтение данных о круге из файла
    points = read_points_data(points_file)  # Чтение координат точек из файла

    if not 1 <= len(points) <= 100:  # Проверка количества точек на соответствие диапазону
        print("Ошибка: количество точек должно быть от 1 до 100.")  # Вывод сообщения об ошибке
        return  # Завершение выполнения программы

    for point in points:  # Перебор всех точек
        result = determine_point_position(xc, yc, r, *point)  # Определение положения каждой точки относительно окружности
        print(result)  # Вывод результата

if __name__ == "__main__":  # Проверка, запущен ли скрипт напрямую
    main()  # Вызов главной функции программы
