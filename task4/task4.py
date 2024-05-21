import sys



def min_moves(nums):
    # Шаг 1: Сортируем массив
    nums.sort()
    
    # Шаг 2: Находим медиану
    n = len(nums)
    median = nums[n // 2] if n % 2 == 1 else (nums[n // 2 - 1] + nums[n // 2]) // 2
    
    # print(median)
    
    # Шаг 3: Считаем сумму абсолютных разностей от медианы
    summ = sum(abs(num - median) for num in nums)
    
    return summ


def main():

    file = sys.argv[1]
    with open(file, 'r') as f:
        nums = [int(line.strip()) for line in f]

    result = min_moves(nums)
    print(result)

if __name__ == "__main__":
    main()
