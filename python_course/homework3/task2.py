# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def print_personal_data(**kwargs):
    print(kwargs)


def main():
    personal_data = {'First name': None,
                     'Last name': None,
                     'Year of birth': None,
                     'City': None,
                     'email': None,
                     'Phone number': None}
    for key in personal_data.keys():
        print(f"Enter person's {key}: ")
        personal_data[key] = input()
    print_personal_data(**personal_data)


if __name__ == '__main__':
    main()
