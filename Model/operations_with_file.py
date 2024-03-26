import csv


def read_file() -> list:
    with (open('notes.csv', "r", encoding="utf-8") as file):
        reader = list(csv.reader(file, delimiter=";"))[1:]
    return reader


def add_to_file(note: list[str]):
    with open('notes.csv', "a", encoding="utf-8", newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(note)


def save_to_file(notes: list[list[str]]):
    with open('notes.csv', "w", encoding="utf-8", newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(['ID', 'Headline', 'Body', 'Date_time'])
        for i, line in enumerate(notes, 1):
            line[0] = str(i)
            writer.writerow(line)
