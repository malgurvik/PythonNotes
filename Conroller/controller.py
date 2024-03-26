from View import view, text
from Model import note_operations as n_op, operations_with_file as file


def start_app():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                view.show_all_notes(view.sort_var(file.read_file()))
            case 2:
                view.show_note(file.read_file())
            case 3:
                n_op.new_note()
                view.print_message(text.add_successful)
            case 4:
                n_op.change_note()
                view.print_message(text.change_successful)
            case 5:
                n_op.delete_note()
                view.print_message(text.delete_successful)
            case 6:
                view.print_message(text.goodbye)
                break
