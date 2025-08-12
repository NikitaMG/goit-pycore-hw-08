from collections import UserDict
import datetime

from Homeworks.Homework5_4 import input_error


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if len(value)!=10:
            raise ValueError ("Phone must contain 10 characters")
        elif not self.is_correct(value):
            raise ValueError("Phone number is not correct!")

        super().__init__(value)

    def is_correct(self, value):
        return isinstance(value, str) and value.isdigit() and len(value) == 10


class Birthday(Field):
    def __init__(self, value):
        try:
            reformated_date = datetime.datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

        super().__init__(reformated_date)

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthday(self, birthday: str):
        self.birthday = Birthday(birthday)

    def show_birthday(self):
        if self.birthday:
            return str(self.birthday)
        else:
            return "Birthday date does not set"

    def add_phone(self, phone_number: str):
        number = Phone(phone_number)
        self.phones.append(number)

    def remove_phone(self, phone_number: str):
        phone = self.find_phone(phone_number)
        if phone:
            self.phones.remove(phone)
            return True
        return None

    def edit_phone(self, old_number, new_number):
        if not self.find_phone(old_number):
            raise ValueError(f"Phone number {old_number} not found")

        try:
            new_phone = Phone(new_number)
        except ValueError:

            raise ValueError(f"Invalid new phone number: {new_number}")

        self.remove_phone(old_number)
        self.add_phone(new_number)
        return True

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        today = datetime.date.today()
        final_date = today + datetime.timedelta(days=7)

        result = []

        for i in self.data.values():
            if i.birthday:
                birthday_date = i.birthday.value
                this_year_birthday = birthday_date.replace(year=today.year)

                if this_year_birthday < today:
                    this_year_birthday = this_year_birthday.replace(year=today.year + 1)

                if today <= this_year_birthday <= final_date:
                    weekends = this_year_birthday.weekday()
                    if weekends == 5:
                        new_date = this_year_birthday + datetime.timedelta(days=2)
                    elif weekends == 6:
                        new_date = this_year_birthday + datetime.timedelta(days=1)
                    else:
                        new_date = this_year_birthday

                    result.append({"name": i.name.value, "birthday": new_date.strftime("%d.%m.%Y")})

        return result

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())


@input_error
def add_birthday(args, book: AddressBook):
    if len(args) != 2:
        raise ValueError("Not correct usage, try: add-birthday [name] [DD.MM.YYYY]")

    name, birthdays_str = args

    contact = book.find(name)
    if not contact:
        return f"Contact {name} does not exist!"

    contact.add_birthday(birthdays_str)
    return f"Birthday date for {name} added: {birthdays_str}"


@input_error
def show_birthday(args, book: AddressBook):
    if not args:
        return "Enter contact`s name"
    name = args[0]
    contact = book.find(name)
    if not contact:
        return f"contact {name} does not exist!"
    return contact.show_birthday()


@input_error
def birthdays(args, book: AddressBook):
    result = book.get_upcoming_birthdays()
    if not result:
        return "There are no birthdays in the 7 days"
    birthday_output = []
    for i in result:
        birthday_output.append(f"{i['name']}: {i['birthday']}")
    return '\n'.join(birthday_output)


@input_error
def change_contact(args, book: AddressBook):
    if len(args) != 3:
        raise ValueError("Not correct usage, try: change [name] [old_phone] [new_phone]")
    name, old_phone, new_phone = args
    contact = book.find(name)
    if not contact:
        return f"Contact {name} does not exist!"
    contact.edit_phone(old_phone, new_phone)
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError


def show_all(contacts):
    if not contacts:
        return "Contact list is empty."
    result = "Contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()


def parse_input(user_input):
    cmd, *args = user_input.strip().split()
    return cmd.lower(), args


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_birthday(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":

            print(birthdays(args, book))
        else:
            print("Invalid command.")
