import field


class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = field.Name(name)
        self.phones = [field.Phone(phone)] if phone else []
        self.birthday = field.Birthday(birthday) if birthday else None

    def add_phone(self, phone):
        self.phones.append(field.Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return "Телефон видалено"
        return "Телефон не знайдено"

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return "Телефон оновлено"
        return "Старий телефон не знайдено"

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return "Телефон не знайдено"

    def add_birthday(self, birthday):
        self.birthday = field.Birthday(birthday)

    def show_birthday(self):
        return str(self.birthday)

    def __str__(self):
        phones = '; '.join(p.value for p in self.phones)
        birthday = f", день народження: {self.birthday.value}" if self.birthday else ""
        return f"Ім'я контакту: {self.name.value}, телефони: {phones}{birthday}"
