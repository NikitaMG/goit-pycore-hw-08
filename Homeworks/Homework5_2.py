def generator_numbers(text: str):
    for word in text.split():

        try:
            yield float(word)
        except ValueError:
            continue


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."


def sum_profit(txt, func):
    return sum(func(txt))


print(sum_profit(text,generator_numbers))
