def total_salary(path):
    total_sum = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                info = line.strip().split(",")
                if len(info) == 2:
                    try:
                        salary = int(info[1])
                        total_sum += salary
                        count += 1
                    except ValueError:
                        print(f"Не вдалося перетворити зарплату: {info[1]}")

    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return 0, 0
    
    average_salary = total_sum / count
    return total_sum, average_salary


total, average = total_salary(r'C:\Users\nikit\Python\1\Homeworks\employee_info.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
