from View import text


def main_menu() -> int:
    for n, item in enumerate(text.main_menu):
        if n == 0:
            print('=' * (len(text.main_menu[1]) + 5))
            print('\t' * 2 + item)
            print('=' * (len(text.main_menu[1]) + 5))

        else:
            print(f' {n}. {item}')

    print('=' * (len(text.main_menu[1]) + 5))
    while True:
        choice = input('\nВыберите пункт меню: ')
        if choice.isdigit() and 0 < int(choice) < len(text.main_menu):
            return int(choice)
        print(f'Введите пункт меню от 1 до {len(text.main_menu) - 1}')


def sort_var(notes: list[list[str]]) -> list[list[str]]:
    for i, item in enumerate(text.sort_notes):
        if i == 0:
            print(item)
        else:
            print(f' {i}. {item}')
    choice = int(input('\nВыберите пункт: '))
    if choice == 1:
        return notes
    if choice == 2:
        return sorted(notes, key=lambda x: x[3], reverse=True)


def show_all_notes(notes: list[list[str]]):
    max_size = list(map(lambda x: len(max(x, key=len)), list(zip(*notes))))
    if notes:
        print('\n' + '=' * (sum(max_size) - max_size[2] + 7))
        print(f'{"ID":>3}  {"Заголовок":<{max_size[1]}}  {"Текст":<{max_size[3]}}')
        for note in notes:
            print(f'{note[0]:>3}. {note[1]:<{max_size[1]}}  {note[2]:<{max_size[3]}}')
        print('=' * (sum(max_size) - max_size[2] + 7) + '\n')


def show_note(notes: list[list[str]]) -> list[str]:
    show_all_notes(notes)
    choice = int(input("Введите ID заметки: "))
    if 0 < int(choice) < len(notes) - 1:
        for note in notes:
            if choice == int(note[0]):
                print('=' * (len(note[1]) + len(note[2]) + len(note[3]) + 5))
                print(f' {note[1]}: {note[2]} {note[3]}')
                print('=' * (len(note[1]) + len(note[2]) + len(note[3]) + 5) + '\n')
                return note

    else:
        print_message("Введенный ID не существует!")


def add_note() -> list[str]:
    message = text.create_note
    note = []
    for item in message:
        field = input(item)
        note.append(field)
    return note


def change_note(note_for_change: list[str]) -> list[str]:
    message = text.change_note
    for i, item in enumerate(message):
        item = input(item)
        note_for_change[i] = item if item else note_for_change[i]
    return note_for_change


def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')
