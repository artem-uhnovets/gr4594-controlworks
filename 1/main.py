""" 
json формат
   0            1                    2                     3
{"id":"001", "title":"some_title", "body": "some_text", "create": "date_time"}
"{id:001, title:some_title, body: some_text, create: date_time}"
"""

import datetime
import os
from pathlib import Path

os.chdir('C:/Users/uhnov/OneDrive/Рабочий стол/УЧЕБА GB/PYTHON/ControlWorks/1')
print(os.getcwd())

clear = lambda: os.system('cls')
clear()

def horiz_line(text):
    print(('=' * ((len(text)*2)-1)) if type(text) == str else ('=' * max(list(map(lambda a: len(a),text)))))
    print(*text)
    print(('=' * ((len(text)*2)-1)) if type(text) == str else ('=' * max(list(map(lambda a: len(a),text)))))

def save_notes(notes_list):
    with open('task1.txt', 'w', encoding='utf-8') as f:
        f.writelines(list(map(lambda note: f'{note}\n', notes_list)))

def modify_note(notes_list):
    search_id = input('\nВведите id заметки - ')
    search_flag = False
    for i in range(len(notes_list)):
        note = notes_list[i].replace('{{','').replace('}}','')
        id = note.split(',')[0].split(':')[1]
        title = note.split(',')[1].split(':')[1]
        body = note.split(',')[2].split(':')[1]
        create = note.split(',')[3].split(':')[1]
        if search_id == id:
            search_flag = True
            print('По указаному id найдена заметка:')
            print(notes_list[i])
            print('Оставьте строку пустой если хотите оставить старую запись')
            while True:
                is_id_exist = False
                id_new = input('Введите новый id - ')
                if id_new == '':
                    id_new = note.split(',')[0].split(':')[1]
                    break
                else:                    
                    for note in notes_list:
                        note = note.replace('{{','').replace('}}','')
                        id_from_list = note.split(',')[0].split(':')[1]
                        if id_from_list == id_new:
                            is_id_exist = True
                    if is_id_exist:
                        print('Такой id уже есть!')
                    else:
                        break
            if title_new := input('Введите новый заголовок - ') == '':
                title_new = title
            if body_new := input('Введите новое тело заметки - ') == '':
                body_new = body
            create_new = create
            note_new = f'{{id:{id_new}, title:{title_new}, body:{body_new}, create:{create_new}}}'
            notes_list[i] = note_new
    if search_flag == False:
        horiz_line('Ничего не найдено!')
    else:
        return notes_list

def delete_note(notes_list):
    search_id = input('\nВведите id заметки - ')
    search_flag = False
    for i in range(len(notes_list)):
        note = notes_list[i].replace('{{','').replace('}}','')
        id = note.split(',')[0].split(':')[1]
        if search_id == id:
            search_flag = True
            print('По указаному id найдена заметка:')
            print(notes_list[i])
            notes_list.pop(i)
    if search_flag == False:
        horiz_line('Ничего не найдено')
    return notes_list

def add_note(notes_list):
    if not notes_list:
        id = input('Введите id - ')
    else:
        print('id должен быть уникален')
        while True:
            is_id_exist = False
            id = input('Введите id - ')
            for note in notes_list:
                note = note.replace('{{','').replace('}}','')
                id_from_list = note.split(',')[0].split(':')[1]
                if id_from_list == id:
                    is_id_exist = True
            if is_id_exist:
                print('Такой id уже есть!')
            else:
                break
    title = input('Введите заголовок - ')
    body = input('Введите тело заметки - ')
    create = datetime.datetime.now()
    note_new = f'{{id:{id}, title:{title}, body:{body}, create:{create}}}'
    notes_list.append(note_new)
    return notes_list

def print_notes(notes_list):
    if not notes_list:
        print('Заметок нет, файл пуст!')
    else:
        notes_list.sort(key=sort_key_date)
        for i in range(len(notes_list)):
            print(f'{i+1}. {notes_list[i]}')

def sort_key_date(note):
    return note.split(',')[3].split(':')[1]

def menu_main_info(option=None):
    menu_main_list = ['1. Показать все заметки',
                      '2. Добавить',
                      '3. Удалить',
                      '4. Редактировать',
                      '5. Сохранить в файл',
                      '6. Выход',
                      '7. Главное меню']
    if (option is not None) and (option in range(1, 7)):
        horiz_line(' '.join((menu_main_list[option - 1].split())[1:]))
    else:
        horiz_line(' '.join((menu_main_list[5].split())[1:]))
        print(*map(lambda a: f'\n{a} ', menu_main_list[:6]))

def get_notes():
    try:
        with open('task1.txt', 'r', encoding='utf-8') as f:
            # notes_all_list = list(map(lambda a: a[:-1], f.readlines))
            notes_all_list = f.read().splitlines()
    except:
        print('Создание нового файла')
        file = Path('task1.txt')
        file.touch(exist_ok=True)
    return notes_all_list


def menu_main():
    notes_list = get_notes()
    while True:
        menu_main_info()
        match user_action := input("\nВыберите функцию, через цифру - ").lower():
            case '1' | 'показать' | 'show':
                menu_main_info(1)
                print_notes(notes_list)
            case '2' | 'добавить' | 'add':
                menu_main_info(2)
                notes_list = add_note(notes_list)
            case '3' | 'удалить' | 'del' | 'delete':
                menu_main_info(3)
                notes_list = delete_note(notes_list)
            case '4' | 'редактировать' | 'modify' | 'edit':
                menu_main_info(4)
                notes_list = modify_note(notes_list)
            case '5' | 'сохранить' | 'save' | 'ыфму':
                menu_main_info(5)
                save_notes(notes_list)
            case '6' | 'выход' | 'quit' | 'exit' | 'ds[jl':
                menu_main_info(6)
                break
            case _:
                horiz_line('!!!Нет такой функции!!!')

menu_main()