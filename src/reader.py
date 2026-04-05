import csv
import sys


def read_files(file_paths: list[str]) -> list[dict[str, str]]:
    """Читает CSV-файлы и объединяет данные в список."""
    file_data_list: list[dict[str, str]] = []

    for file_path in file_paths:
        try:
            # Открываем файл и читаем его построчно как словари
            with open(file_path, newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)

                # Добавляем строки в общий список
                file_data_list.extend(reader)

        except FileNotFoundError:
            print(f'Файл не найден: {file_path}', file=sys.stderr)
            sys.exit(1)

    return file_data_list
