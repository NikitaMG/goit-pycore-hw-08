from collections import UserDict
import datetime
import pickle

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
        if not self.is_correct(value):
            raise ValueError("Phone number is not correct!")
        super().__init__(value)

    def is_correct(self, value):
        return isinstance(value, str) and value.isdigit() and len(value) == 10


class Birthday(Field):
    def __init__(self, value: str):
        try:
            p_date = datetime.datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

        if p_date.year < 1900 or p_date.year >= datetime.datetime.today().year:
            raise ValueError("Incorrect Year!")

        super().__init__(value)

    def __str__(self):
        return self.value

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthday(self, birthday: str):
        self.birthday = Birthday(birthday)

    def show_birthday(self):
        return self.birthday

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

        self.add_phone(new_number)
        self.remove_phone(old_number)
        return True

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        birthday = str(self.birthday) if self.birthday else "No birthday"
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, Birthday: {birthday}"


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
                birthday_date = datetime.datetime.strptime(i.birthday.value,"%d.%m.%Y").date()
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


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f"Error {e}"
        except IndexError:
            return "Enter a name."
        except KeyError:
            return "No such contact in the list."
        except AttributeError:
            return "No such contact in the list."

    return inner


@input_error
def add_birthday(args, book: AddressBook):
    name, birthdays_str = args
    contact = book.find(name)
    contact.add_birthday(birthdays_str)
    return True


@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    contact = book.find(name)
    return contact.show_birthday()


@input_error
def birthdays(args, book: AddressBook):
    return book.get_upcoming_birthdays()


@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone = args
    contact = book.find(name)
    contact.edit_phone(old_phone, new_phone)
    return True


@input_error
def show_phone(args, book: AddressBook):
    name = args[0]
    contacts = book.find(name)
    return [phone.value for phone in contacts.phones]


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


def show_all(book: AddressBook):
    if not book.data:
        return "No contacts!"
    return "\n".join(str(record) for record in book.data.values())


def parse_input(user_input):
    cmd, *args = user_input.strip().split()
    return cmd.lower(), args


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if not user_input:
            continue
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

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


if __name__ == "__main__":
    main()
