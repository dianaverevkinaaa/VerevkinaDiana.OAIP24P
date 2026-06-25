import os
import shutil
from pathlib import Path

NOTES_FILE = "my_notes.txt"
BACKUP_DIR = "backup_notes"


def show_menu():
    print("\n" + "=" * 40)
    print("МЕНЕДЖЕР ЗАМЕТОК")
    print("1. Показать все заметки")
    print("2. Добавить заметку")
    print("3. Удалить заметку по номеру")
    print("4. Очистить все заметки")
    print("5. Сделать резервную копию")
    print("6. Выйти")
    print("=" * 40)


def read_all_notes():
    if not os.path.exists(NOTES_FILE):
        print("Файл с заметками пока не создан.")
        return []

    with open(NOTES_FILE, "r", encoding="utf-8") as file:
        notes = file.readlines()

    return [note.strip() for note in notes]


def show_notes():
    notes = read_all_notes()
    if not notes:
        print("Заметок нет.")
        return

    print("\n--- Ваши заметки ---")
    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note}")
    print("---------------------")


def add_note():
    note_text = input("Введите текст заметки: ").strip()
    if not note_text:
        print("Заметка не может быть пустой.")
        return

    with open(NOTES_FILE, "a", encoding="utf-8") as file:
        file.write(note_text + "\n")  # .write() записывает строку [reference:8]

    print("✅ Заметка добавлена!")


def delete_note():
    notes = read_all_notes()
    if not notes:
        print("Нет заметок для удаления.")
        return

    show_notes()
    try:
        num = int(input("Введите номер заметки для удаления: "))
        if num < 1 or num > len(notes):
            print("❌ Неверный номер.")
            return
    except ValueError:
        print("❌ Введите число.")
        return

    deleted = notes.pop(num - 1)

    with open(NOTES_FILE, "w", encoding="utf-8") as file:
        for note in notes:
            file.write(note + "\n")

    print(f"✅ Заметка «{deleted}» удалена!")


def clear_all_notes():
    if not os.path.exists(NOTES_FILE):
        print("Файл с заметками уже пуст.")
        return

    confirm = input("Вы уверены, что хотите удалить ВСЕ заметки? (да/нет): ")
    if confirm.lower() != "да":
        print("Операция отменена.")
        return

    os.remove(NOTES_FILE)
    print("🗑️ Все заметки удалены!")


def backup_notes():
    if not os.path.exists(NOTES_FILE):
        print("Нет файла с заметками для резервного копирования.")
        return

    backup_path = Path(BACKUP_DIR)
    backup_path.mkdir(exist_ok=True)

    backup_file = backup_path / f"backup_{NOTES_FILE}"

    shutil.copy2(NOTES_FILE, backup_file)

    if os.path.exists(backup_file):
        print(f"✅ Резервная копия создана: {backup_file}")
    else:
        print("❌ Ошибка при создании резервной копии.")


def main():
    while True:
        show_menu()
        choice = input("Выберите действие (1-6): ").strip()

        if choice == "1":
            show_notes()
        elif choice == "2":
            add_note()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            clear_all_notes()
        elif choice == "5":
            backup_notes()
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("❌ Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()