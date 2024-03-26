from datetime import datetime
import Model.operations_with_file as file
import View.view as view

date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))


def next_id() -> str:
    notes = file.read_file()
    return str(len(notes) + 1) if notes else '1'


def new_note():
    global date
    note_field = view.add_note()
    note = [next_id(), note_field[0], note_field[1], date]
    file.add_to_file(note)


def change_note():
    global date
    reader = file.read_file()
    note_fields = view.show_note(reader)
    changed_note = view.change_note(note_fields[1:3])
    for line in reader:
        if line == note_fields:
            line[1] = changed_note[0]
            line[2] = changed_note[1]
            line[3] = date
    file.save_to_file(reader)


def delete_note():
    reader = file.read_file()
    del_note = view.show_note(reader)
    for i, line in enumerate(reader):
        if line == del_note:
            reader.pop(i)
    file.save_to_file(reader)
