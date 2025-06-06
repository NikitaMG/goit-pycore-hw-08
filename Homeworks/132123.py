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
