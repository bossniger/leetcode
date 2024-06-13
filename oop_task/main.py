class User:
    users = {}

    def __init__(self, name, id_number, age=None, surname=None):
        if id_number in self.users:
            raise ValueError("Пользователь с этим айдишником уже существует")
        self.name = name
        self.id_number = id_number
        self.age = age
        self.surname = surname
        self.users[id_number] = self

    def change_parameter(self, id_number, parameter, value):
        if id_number != self.id_number:
            print("Нельзя изменить ваш параметр для другого пользователя")
            return
        if parameter == 'name':
            self.name = value
        elif parameter == 'age':
            self.age = value
        elif parameter == 'surname':
            self.surname = value
        else:
            print("Неверный параметр")


def main():
    user1 = User('Egor', 13, 24, 'Belyakovich')
    print(User.users)
    user1.change_parameter(13,'name', 'rogE')
    print(user1.name)

main()