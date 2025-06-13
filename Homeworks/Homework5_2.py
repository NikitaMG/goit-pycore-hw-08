def generator_numbers(text: str):
    words = text.split()
    for word in words[1:-1]:
        try:
            yield float(word)
        except ValueError:
            continue


def sum_profit(txt, func):
    return sum(func(txt))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

print(sum_profit(text, generator_numbers))
