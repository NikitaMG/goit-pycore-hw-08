from collections import deque

goals = [
    {"type": "fast", "task": "finish course"},
    {"type": "slow", "task": "take photos"},
    {"type": "fast", "task": "100 words"},
    {"type": "slow", "task": "new outfit"}
]
task_line = deque()
for task in goals:
    if task["type"] == "fast":
        task_line.appendleft(task)
    else:
        task_line.append(task)
print(task_line)


def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1


for num in count_up_to(10):
    print(num)
    print(max)


def complicated(x: int, y: int) -> int:
    return x + y


def logger(func):
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result

    return inner


complicated = logger(complicated)
print(complicated(2, 3))

numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # [1, 4, 9, 16]

numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)  # 👉 [2, 4, 6]

values = [0, 0, 1, 0]
print(any(values))  # 👉 True
