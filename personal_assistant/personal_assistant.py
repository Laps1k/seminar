import json
import os
import csv
from datetime import datetime

def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return []

def save_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def create_item(item_type):
    title = input(f"Введите заголовок {item_type}: ")
    content = input(f"Введите содержимое {item_type}: ")
    timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    new_item = {
        "id": len(load_data(f'{item_type.lower()}s.json')) + 1,
        "title": title,
        "content": content,
        "timestamp": timestamp
    }

    items = load_data(f'{item_type.lower()}s.json')
    items.append(new_item)
    save_data(f'{item_type.lower()}s.json', items)
    print(f"{item_type} успешно создана!")

def view_items(item_type):
    items = load_data(f'{item_type.lower()}s.json')
    if items:
        for item in items:
            print(f"ID: {item['id']}, Заголовок: {item['title']}, Дата: {item['timestamp']}")
    else:
        print(f"Нет {item_type.lower()}.")

def view_item_details(item_type):
    item_id = int(input(f"Введите ID {item_type.lower()}а для просмотра: "))
    items = load_data(f'{item_type.lower()}s.json')
    item = next((i for i in items if i['id'] == item_id), None)
    if item:
        print(f"Заголовок: {item['title']}\nСодержимое: {item['content']}\nДата: {item['timestamp']}")
    else:
        print(f"{item_type} не найден.")

def edit_item(item_type):
    item_id = int(input(f"Введите ID {item_type.lower()}а для редактирования: "))
    items = load_data(f'{item_type.lower()}s.json')
    item = next((i for i in items if i['id'] == item_id), None)
    if item:
        new_title = input(f"Текущий заголовок: {item['title']}. Введите новый заголовок: ")
        new_content = input(f"Текущее содержимое: {item['content']}. Введите новый текст: ")
        item['title'] = new_title
        item['content'] = new_content
        item['timestamp'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        save_data(f'{item_type.lower()}s.json', items)
        print(f"{item_type} успешно отредактирован!")
    else:
        print(f"{item_type} не найден.")

def delete_item(item_type):
    item_id = int(input(f"Введите ID {item_type.lower()} для удаления: "))
    items = load_data(f'{item_type.lower()}s.json')
    item = next((i for i in items if i['id'] == item_id), None)
    if item:
        items.remove(item)
        save_data(f'{item_type.lower()}s.json', items)
        print(f"{item_type} успешно удален!")
    else:
        print(f"{item_type} не найден.")

def export_items_to_csv(item_type):
    items = load_data(f'{item_type.lower()}s.json')
    if items:
        with open(f'{item_type.lower()}s_export.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'title', 'content', 'timestamp'])
            writer.writeheader()
            writer.writerows(items)
        print(f"{item_type} успешно экспортированы в CSV.")
    else:
        print(f"Нет {item_type.lower()} для экспорта.")

def import_items_from_csv(item_type):
    try:
        with open(f'{item_type.lower()}s_import.csv', 'r', newline='') as f:
            reader = csv.DictReader(f)
            items = [row for row in reader]
            items = [{**item, 'id': int(item['id']), 'timestamp': item['timestamp']} for item in items]
            save_data(f'{item_type.lower()}s.json', items)
            print(f"{item_type} успешно импортированы из CSV.")
    except FileNotFoundError:
        print(f"Файл для импорта {item_type.lower()} не найден.")

def manage_items(item_type):
    while True:
        print(f"\nУправление {item_type.lower()}:")
        print("1. Создать")
        print("2. Просмотреть список")
        print("3. Просмотреть подробности")
        print("4. Редактировать")
        print("5. Удалить")
        print("6. Экспорт")
        print("7. Импорт")
        print("8. Назад")

        choice = input("Ваш выбор: ")

        if choice == '1':
            create_item(item_type)
        elif choice == '2':
            view_items(item_type)
        elif choice == '3':
            view_item_details(item_type)
        elif choice == '4':
            edit_item(item_type)
        elif choice == '5':
            delete_item(item_type)
        elif choice == '6':
            export_items_to_csv(item_type)
        elif choice == '7':
            import_items_from_csv(item_type)
        elif choice == '8':
            break
        else:
            print("Неверный выбор!")


def calculator():
    print("Калькулятор:")
    while True:
        try:
            expression = input("Введите выражение (или 'выход' для выхода): ")
            if expression.lower() == 'выход':
                break
            else:
                result = eval(expression)
                print(f"Результат: {result}")
        except Exception as e:
            print(f"Ошибка: {e}")


def main_menu():
    while True:
        print("\nДобро пожаловать в Персональный помощник!")
        print("1. Управление заметками")
        print("2. Управление задачами")
        print("3. Управление контактами")
        print("4. Управление финансовыми записями")
        print("5. Калькулятор")
        print("6. Выход")

        choice = input("Ваш выбор: ")

        if choice == '1':
            manage_items('Note')
        elif choice == '2':
            manage_items('Task')
        elif choice == '3':
            manage_items('Contact')
        elif choice == '4':
            manage_items('Finance')
        elif choice == '5':
            calculator()
        elif choice == '6':
            print("Ня, пока!(.")
            break
        else:
            print("Неправильно! Попробуй еще раз!)")

if __name__ == "__main__":
    main_menu()