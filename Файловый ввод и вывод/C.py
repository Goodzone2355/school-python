with open('E:/Python/Файловый ввод и вывод/C.txt', 'r') as f_in:
    # Читаем числа из файла и сохраняем их в список
    numbers = [int(line) for line in f_in.readlines()]

# Инициализируем переменные для хранения текущей и максимальной длины цепочки
current_length = 1
max_length = 1

# Итерируемся по списку чисел, начиная со второго элемента
for i in range(1, len(numbers)):
    if numbers[i] == numbers[i-1]:
        # Если текущее число равно предыдущему, увеличиваем текущую длину цепочки на 1
        current_length += 1
    else:
        # Иначе, обновляем максимальную длину цепочки и сбрасываем текущую длину
        max_length = max(max_length, current_length)
        current_length = 1

# Обработка краевого случая, когда все числа в файле одинаковые
max_length = max(max_length, current_length)

with open('E:/Python/Файловый ввод и вывод/C1.txt', 'w') as f_out:
    f_out.write(str(max_length))