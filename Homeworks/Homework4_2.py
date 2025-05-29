def get_cats_info(path):
    result = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                info = line.strip().split(",")
                if len(info) == 3:
                    ID, name, age = info
                    result.append({"ID": ID, "name": name, "age": int(age)})
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
    return result



data = get_cats_info(r'C:\Users\nikit\Python\1\Homeworks\cats.txt')
print(data)
