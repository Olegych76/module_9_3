first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Первая генераторная сборка
first_result = (len(line1) - len(line2) for line1, line2 in zip(first, second) if len(line1) != len(line2))

# Вторая генераторная сборка
second_result = (not bool(len(first[i]) - len(second[i])) for i in range(min(len(first), len(second))))

# Вывод результатов
print(list(first_result))
print(list(second_result))

