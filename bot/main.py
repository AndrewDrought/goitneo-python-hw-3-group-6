import functions
from address_book import AddressBook


def main():
    address_book = AddressBook()
    print("Вітаємо в боті-помічнику!")
    while True:
        user_input = input("Введіть команду: ")
        command, args = functions.parse_input(user_input)

        if command in ["close", "exit"]:
            print("До побачення!")
            break
        elif command == "hello":
            print("Як я можу вам допомогти?")
        elif command == "add":
            print(functions.add_contact(args, address_book))
        elif command == "change":
            print(functions.change_contact(args, address_book))
        elif command == "phone":
            print(functions.phone(args, address_book))
        elif command == "add-birthday":
            print(functions.add_birthday(args, address_book))
        elif command == "show-birthday":
            name = args[0]
            record = address_book.find(name)
            if record:
                print(record.show_birthday())
            else:
                print("Контакт не знайдено.")
        elif command == "birthdays":
            print(address_book.birthdays())
        elif command == "all":
            functions.all(address_book)
        else:
            print("Невірна команда.")


if __name__ == "__main__":
    main()
