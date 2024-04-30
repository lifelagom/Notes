import json
import datetime

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
    for key in keys:
        if key in data.keys():
            print(f'{key}. {data[key]['title']}\n{data[key]['text']}\nДата создания/изменения: {data[key]['date']}\n')

# Запрашиваем у пользователя данные
def input_title():
    return input('Введите заголовок заметки: ')

def input_text():
    return input('Введите текст заметки: ')

# Добавляем новую заметку
def add_note(data: dict):
    date = datetime.datetime.now().strftime('%d-%m-%y (%H:%M:%S)')
    data[str(len(data)+1)] = {'title': input_title(), 'text': input_text(), 'date': date}
    save_note(data)
    print('Заметка успешно сохранена')

# Редактируем заметку
def edit_note(data):
    id = input('Введите номер заметки для редактирования: ')
    if id in data.keys():
        print(data[id])
        data[id]['title'] = input_title()
        data[id]['text'] = input_text()
        data[id]['date'] = datetime.datetime.now().strftime('%d-%m-%y (%H:%M:%S)')
        save_note(data)
        print('Заметка успешно сохранена')
    else:
        print('Заметка с таким номером не найдена!')

# Удаляем заметку
def del_note(data):
    id = input("Введите номер заметки для удаления: ")
    if id in data.keys():
        del data[id]
        save_note(data)
        print('Заметка №'+id+' успешно удалена!')
    else: print('Заметка с таким номером не найдена!')

# Поиск заметки по дате
def dateSearch_note(data):
    date = input('Введите дату для фильтрации заметок в формате(dd-mm-yy): ')
    print()
    noteList = []
    for i in range(1, len(data)+1):
        if date in data[str(i)]["date"]:
            noteList.append(str(i))
    printNotes(data, noteList)

# Интерфейс пользователя
def interface():
    data = load_notes()

if __name__ == '__main__':
    interface()