# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Создать контакт
# 5. Изменить контакт
# 6. Найти контакт
# 7. Удалить контакт
# 8. Выход

phone_book = []
path = 'Telefon_guide_1.txt'


def open_file(path):
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for contact in data:
            cont = []
            for field in contact.split(';'):
                cont.append(field.strip())
            phone_book.append(cont)


def save_file(path):
    with open(path, 'w', encoding='UTF-8') as file:
        text = ''
        for contact in phone_book:
            text += f'{contact[0]};{contact[1]};{contact[2]}\n'
        file.write(text)


def show_contacts(phone_book):
    for i, contact in enumerate(phone_book, 1):
        print(f'{i}. {contact[0]:<20}{contact[1]:<20}{contact[2]:<15}')


def add_contact():
    name = input('Введите имя и фамилию: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    phone_book.append(list([name, phone, comment]))


def search_contact(phone_book):
    search = input('Введите ключевой элемент: ')
    for contact in phone_book:
        for field in contact:
            if search in field:
                print(contact)


def change_contact(phone_book):
    search = input('Введите изменяемый элемент: ')
    change = input('Введите изменение: ')
    for i, contact in enumerate(phone_book):
        for j, field in enumerate(contact):
            if search in field:
                phone_book[i][j] = change


def delete_contact(phone_book):
    search = input('Введите удаляемый элемент: ')
    for contact in phone_book:
        for field in contact:
            if search in field:
                phone_book.remove(contact)


while True:
    number = int(input('Введите пункт меню: '))
    if number == 1:
        open_file(path)
        print('Файл успешно загружен')
    elif number == 2:
        save_file(path)
        print('Файл успешно сохранён')
    elif number == 3:
        show_contacts(phone_book)
    elif number == 4:
        add_contact()
    elif number == 5:
        change_contact(phone_book)
    elif number == 6:
        search_contact(phone_book)
    elif number == 7:
        delete_contact(phone_book)
    elif number == 8:
        break

print('До свидания')