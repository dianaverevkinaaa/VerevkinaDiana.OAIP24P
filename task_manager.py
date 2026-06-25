import json
import os
from datetime import datetime

DATA_FILE = "projects.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        return {"projects": []}

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def show_projects():
    data = load_data()
    projects = data.get("projects", [])

    if not projects:
        print("\n❌ Проектов нет.")
        return

    print("\n" + "=" * 50)
    print("📁 СПИСОК ПРОЕКТОВ")
    print("=" * 50)

    for i, project in enumerate(projects, start=1):
        status_emoji = {
            "Планирование": "📋",
            "В работе": "🔄",
            "Готов": "✅"
        }.get(project.get("status", "Планирование"), "📋")

        print(f"{i}. {project['name']} {status_emoji} [{project.get('status', 'Планирование')}]")
        print(f"   Задач: {len(project.get('tasks', []))}")

    print("=" * 50)


def create_project():
    name = input("\nВведите название проекта: ").strip()

    if not name:
        print("❌ Название не может быть пустым.")
        return

    data = load_data()
    projects = data.get("projects", [])

    for project in projects:
        if project["name"].lower() == name.lower():
            print("❌ Проект с таким названием уже существует.")
            return

    new_project = {
        "name": name,
        "status": "Планирование",
        "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "tasks": []
    }

    projects.append(new_project)
    data["projects"] = projects
    save_data(data)

    print(f"✅ Проект «{name}» создан!")


def add_task():
    data = load_data()
    projects = data.get("projects", [])

    if not projects:
        print("\n❌ Нет проектов. Сначала создайте проект.")
        return

    print("\n📁 Выберите проект:")
    for i, project in enumerate(projects, start=1):
        print(f"{i}. {project['name']}")

    try:
        choice = int(input("\nВведите номер проекта: "))
        if choice < 1 or choice > len(projects):
            print("❌ Неверный номер.")
            return
    except ValueError:
        print("❌ Введите число.")
        return

    project = projects[choice - 1]

    task_name = input("Введите название задачи: ").strip()
    if not task_name:
        print("❌ Название задачи не может быть пустым.")
        return

    task_description = input("Введите описание задачи (необязательно): ").strip()

    task = {
        "name": task_name,
        "description": task_description,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "completed": False
    }

    project["tasks"].append(task)
    save_data(data)

    print(f"✅ Задача «{task_name}» добавлена в проект «{project['name']}»!")


def show_tasks():
    data = load_data()
    projects = data.get("projects", [])

    if not projects:
        print("\n❌ Нет проектов.")
        return

    print("\n📁 Выберите проект:")
    for i, project in enumerate(projects, start=1):
        print(f"{i}. {project['name']}")

    try:
        choice = int(input("\nВведите номер проекта: "))
        if choice < 1 or choice > len(projects):
            print("❌ Неверный номер.")
            return
    except ValueError:
        print("❌ Введите число.")
        return

    project = projects[choice - 1]
    tasks = project.get("tasks", [])

    if not tasks:
        print(f"\n❌ В проекте «{project['name']}» нет задач.")
        return

    print(f"\n📋 ЗАДАЧИ В ПРОЕКТЕ: {project['name']}")
    print("=" * 50)

    for i, task in enumerate(tasks, start=1):
        status = "✅ Готово" if task.get("completed", False) else "⏳ В процессе"
        print(f"{i}. {task['name']} — {status}")
        if task.get("description"):
            print(f"   📝 {task['description']}")
        print(f"   🕐 Создана: {task.get('created', 'неизвестно')}")
        print()

    print("=" * 50)


def change_project_status():
    data = load_data()
    projects = data.get("projects", [])

    if not projects:
        print("\n❌ Нет проектов.")
        return

    print("\n📁 Выберите проект:")
    for i, project in enumerate(projects, start=1):
        print(f"{i}. {project['name']} [{project.get('status', 'Планирование')}]")

    try:
        choice = int(input("\nВведите номер проекта: "))
        if choice < 1 or choice > len(projects):
            print("❌ Неверный номер.")
            return
    except ValueError:
        print("❌ Введите число.")
        return

    project = projects[choice - 1]

    print(f"\nТекущий статус: {project.get('status', 'Планирование')}")
    print("\nДоступные статусы:")
    print("1. Планирование")
    print("2. В работе")
    print("3. Готов")

    try:
        status_choice = int(input("\nВыберите статус (1-3): "))
        statuses = {1: "Планирование", 2: "В работе", 3: "Готов"}
        if status_choice not in statuses:
            print("❌ Неверный выбор.")
            return
    except ValueError:
        print("❌ Введите число.")
        return

    project["status"] = statuses[status_choice]
    save_data(data)

    print(f"✅ Статус проекта «{project['name']}» изменён на «{project['status']}»!")


def show_menu():
    print("\n" + "=" * 50)
    print("📊 УПРАВЛЕНИЕ ПРОЕКТАМИ И ЗАДАЧАМИ")
    print("=" * 50)
    print("1. 📁 Показать проекты")
    print("2. ➕ Создать проект")
    print("3. 📝 Добавить задачу")
    print("4. 📋 Показать задачи в проекте")
    print("5. 🔄 Изменить статус проекта")
    print("6. 🚪 Выйти")
    print("=" * 50)


def main():
    print("\n🐍 Управление проектами и задачами")
    print("Данные сохраняются в файл: projects.json")

    while True:
        show_menu()
        choice = input("Выберите действие (1-6): ").strip()

        if choice == "1":
            show_projects()
        elif choice == "2":
            create_project()
        elif choice == "3":
            add_task()
        elif choice == "4":
            show_tasks()
        elif choice == "5":
            change_project_status()
        elif choice == "6":
            print("\n👋 До свидания!")
            break
        else:
            print("❌ Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()