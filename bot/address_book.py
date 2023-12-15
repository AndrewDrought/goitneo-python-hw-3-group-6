import datetime
from collections import UserDict
import pickle


def load_address_book(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)

    except FileNotFoundError:
        return AddressBook()


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, "Запис не знайдено")

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return "Запис видалено"
        return "Запис не знайдено"

    def birthdays(self):
        today = datetime.datetime.today().date()
        birthdays = []

        for name, record in self.data.items():
            if record.birthday:
                birthday = datetime.datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
                birthday_this_year = birthday.replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                delta_days = (birthday_this_year - today).days

                if 0 <= delta_days < 7:
                    day_of_week = birthday_this_year.strftime('%A')
                    if day_of_week in ['Saturday', 'Sunday']:
                        day_of_week = 'Monday'
                    birthdays.append((delta_days, day_of_week, name))

        birthdays.sort()

        return "\n".join(f"{day_of_week}: {name}" for delta_days, day_of_week, name in birthdays)



    def save_address_book(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.data, file)
