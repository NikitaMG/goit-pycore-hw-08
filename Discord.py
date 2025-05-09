class Discord():
    raise_hours = 20

    def __init__(self, name, last, game, hours):
        self.name = name
        self.last = last
        self.game = game
        self.hours = hours

    def raise_h(self):
        self.hours = (self.hours + Discord.raise_hours)

    def infoo(self):
        return '{} {} {} {}'.format(self.name, self.last + "=", self.game + ' - ', self.hours)


class Worker(Discord):
    def __init__(self, name, last, program, pay):
        self.name = name
        self.last = last
        self.program = program
        self.pay = pay

    def month_pay(self):
        self.pay = (self.pay * 20)

    def worker_info(self):
        return '{} {} {} {}'.format(self.name, self.last + "=", self.program, self.pay)


Nikita = Discord('Nikita', 'Malihin', 'Battlefield', 100)
Philip = Discord('Philip', 'Schedriviy', 'Isaac', 1000)
Gosha = Discord('Gosha', 'Shevchenko', 'Seraph', 200)
Artem = Worker('Artem', 'Ahtareev', 'Exel', 20)
while True:
    accept = input('choose the member: ')
    if accept == 'Nikita':
        print(Nikita.infoo())
    elif accept == 'Philip':
        print(Philip.infoo())
    elif accept == 'Gosha':
        print(Gosha.infoo())
    elif accept == 'Artem':
        Artem.month_pay()
        print(Artem.worker_info())
    else:
        print('only three of us')

    con = input('do u want to get other information?: ')
    if con == 'yes':
        continue
    elif con == 'hours':
        hour = input("chose the name: ")
        if hour == 'Nikita':
            Nikita.raise_h()
            print(Nikita.name, Nikita.game, Nikita.hours, 'hours')
        elif hour == 'Gosha':
            Gosha.raise_h()
            print(Gosha.name, Gosha.game, Gosha.hours, 'hours')
        elif hour == "Philip":
            Philip.raise_h()
            print(Philip.name, Philip.game, Philip.hours, 'hours')
        elif hour == 'Artem':
            print("I don`t know")
        break
    else:
        print('Bye!')
        break
