def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        # except ValueError:
        #     return "Напишіть ім'я і телефон."
        except KeyError:
            return "Контакт не знайдено."
        except IndexError:
            return "Введіть ім'я користувача."
        except Exception as e:
            return str(e)
    return inner
