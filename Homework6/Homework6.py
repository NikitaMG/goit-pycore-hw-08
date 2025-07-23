from collections import UserDict


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


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

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

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())
