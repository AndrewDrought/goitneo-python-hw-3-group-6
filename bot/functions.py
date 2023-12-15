from bot.record import Record
from exceptions import input_error


# додавання контакту
@input_error
def add_contact(args, address_book):
    name, phone = args
    record = Record(name, phone)
    address_book.add_record(record)
    return "Контакт додано."


# Функція для зміни контакту
@input_error
def change_contact(args, address_book):
    name, phone = args
    if name in address_book:
        record = Record(name, phone)
        address_book.add_record(record)
        return "Контакт оновлено."
    else:
        raise KeyError


# Функція для отримання номера телефону
@input_error
def phone(args, address_book):
    name = args[0]
    record = address_book.find(name)
    if record:
        return ', '.join(phone.value for phone in record.phones)
    else:
        raise KeyError


@input_error
def add_birthday(args, address_book):
    if len(args) < 2:
        raise ValueError("Введіть ім'я та дату народження.")
    name, birthday = args
    record = address_book.find(name)
    if record:
        record.add_birthday(birthday)
        return "Дата народження додана"
    else:
        raise KeyError("Контакт не знайдено.")


# Функція для виведення всіх контактів
def all(address_book):
    print("\n".join(str(record) for record in address_book.values()))


# Парсер введення
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args
