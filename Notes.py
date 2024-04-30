import json

# Загружаем заметки из файла
def load_notes():
    try:
        with open('Notes.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = dict()
    return data

# Сохраняем заметки в файл
def save_note(data):
    with open('Notes.json', 'w', encoding='utf-8') as saveFile:
        json.dump(data, saveFile, ensure_ascii=False, indent=4)

# Печать заметок
def printNotes(data, keys):
    pass

# Запрашиваем у пользователя данные
def input_title():
    pass

def input_text():
    pass

# Добавляем новую заметку
def add_note(data: dict):
    pass

# Редактируем заметку
def edit_note(data):
    pass

# Удаляем заметку
def del_note(data):
    pass

# Поиск заметки по дате
def dateSearch_note(data):
    pass

# Интерфейс пользователя
def interface():
    pass

if __name__ == '__main__':
    interface()