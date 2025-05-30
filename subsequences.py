def min_subarray_length(arr):
    target = set(range(1, 27))
    freq = [0] * 27
    left = 0
    count = 0
    min_len = float('inf')
    
    for right in range(len(arr)):
        num = arr[right]
        if 1 <= num <= 26:
            if freq[num] == 0:
                count += 1
            freq[num] += 1
            
        while count == 26 and left <= right:
            min_len = min(min_len, right - left + 1)
            num_left = arr[left]
            if 1 <= num_left <= 26:
                freq[num_left] -= 1
                if freq[num_left] == 0:
                    count -= 1
            left += 1
    
    return min_len if min_len != float('inf') else "NONE"

# Чтение данных из файла
with open('data_prog_contest_problem_2.txt', 'r') as f:
    data = f.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))

# Вычисление результата
result = min_subarray_length(arr)
print(result)