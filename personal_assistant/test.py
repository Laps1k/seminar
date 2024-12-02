import json
import os
from datetime import datetime

# Проверка наличия файлов
def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return []

def save_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Работа с заметками
def create_note():
    title = input("Введите заголовок заметки: ")
    content = input("Введите содержимое заметки: ")
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    notes = load_data('notes.json')
    note = {"id": len(notes) + 1, "title": title, "content": content, "timestamp": timestamp}
    notes.append(note)
    save_data('notes.json', notes)
    print("Заметка создана!")

def view_notes():
    notes = load_data('notes.json')
    for note in notes:
        print(f"ID: {note['id']} | Заголовок: {note['title']} | Дата: {note['timestamp']}")

def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    notes = load_data('notes.json')
    note = next((n for n in notes if n['id'] == note_id), None)
    if note:
        note['title'] = input(f"Текущий заголовок: {note['title']}. Введите новый заголовок: ")
        note['content'] = input(f"Текущее содержимое: {note['content']}. Введите новое содержимое: ")
        note['timestamp'] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        save_data('notes.json', notes)
        print("Заметка отредактирована!")
    else:
        print("Заметка не найдена.")

def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    notes = load_data('notes.json')
    notes = [note for note in notes if note['id'] != note_id]
    save_data('notes.json', notes)
    print("Заметка удалена.")

# Работа с задачами
def add_task():
    title = input("Введите заголовок задачи: ")
    description = input("Введите описание задачи: ")
    priority = input("Введите приоритет (Высокий, Средний, Низкий): ")
    due_date = input("Введите срок выполнения задачи (ДД-ММ-ГГГГ): ")
    tasks = load_data('tasks.json')
    task = {"id": len(tasks) + 1, "title": title, "description": description, "done": False, "priority": priority, "due_date": due_date}
    tasks.append(task)
    save_data('tasks.json', tasks)
    print("Задача добавлена!")

def view_tasks():
    tasks = load_data('tasks.json')
    for task in tasks:
        print(f"ID: {task['id']} | Заголовок: {task['title']} | Статус: {'Выполнена' if task['done'] else 'Не выполнена'} | Приоритет: {task['priority']} | Срок: {task['due_date']}")

def edit_task():
    task_id = int(input("Введите ID задачи для редактирования: "))
    tasks = load_data('tasks.json')
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        task['title'] = input(f"Текущий заголовок: {task['title']}. Введите новый заголовок: ")
        task['description'] = input(f"Текущее описание: {task['description']}. Введите новое описание: ")
        task['priority'] = input(f"Текущий приоритет: {task['priority']}. Введите новый приоритет: ")
        task['due_date'] = input(f"Текущий срок: {task['due_date']}. Введите новый срок: ")
        save_data('tasks.json', tasks)
        print("Задача отредактирована!")
    else:
        print("Задача не найдена.")

def delete_task():
    task_id = int(input("Введите ID задачи для удаления: "))
    tasks = load_data('tasks.json')
    tasks = [task for task in tasks if task['id'] != task_id]
    save_data('tasks.json', tasks)
    print("Задача удалена.")

# Главное меню
def main_menu():
    while True:
        print("\nДобро пожаловать в Персональный помощник!")
        print("1. Управление заметками")
        print("2. Управление задачами")
        print("6. Выход")

        choice = input("Ваш выбор: ")

        if choice == '1':
            while True:
                print("\n1. Создать заметку")
                print("2. Просмотреть заметки")
                print("3. Редактировать заметку")
                print("4. Удалить заметку")
                print("0. Назад")

                action = input("Ваш выбор: ")

                if action == '1':
                    create_note()
                elif action == '2':
                    view_notes()
                elif action == '3':
                    edit_note()
                elif action == '4':
                    delete_note()
                elif action == '0':
                    break

        elif choice == '2':
            while True:
                print("\n1. Добавить задачу")
                print("2. Просмотреть задачи")
                print("3. Редактировать задачу")
                print("4. Удалить задачу")
                print("0. Назад")

                action = input("Ваш выбор: ")

                if action == '1':
                    add_task()
                elif action == '2':
                    view_tasks()
                elif action == '3':
                    edit_task()
                elif action == '4':
                    delete_task()
                elif action == '0':
                    break

        elif choice == '6':
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main_menu()
