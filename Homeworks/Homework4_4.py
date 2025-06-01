def parse_input(user_input):
    cmd, *args = user_input.strip().split()
    return cmd.lower(), args


def add_contact(args, contacts):
    if len(args) != 2:
        return "Please enter a name and a phone number  (E.G.: add John 1234567890)."
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Please enter a name and a new phone number (E.G.: change John 0987654321)."
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return f"contact{name} not found."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Please enter only name (E.G.: phone John)."
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return f"Contact with the name {name} not found."


def show_all(contacts):
    if not contacts:
        return "Contact list is empty."
    result = "Contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
