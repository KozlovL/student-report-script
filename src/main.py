from tabulate import tabulate

from src.cli import parse_args
from src.reader import read_files
from src.utils import get_report


def main() -> None:
    """Основная функция скрипта."""
    # Парсим аргументы командной строки
    args = parse_args()

    # Читаем данные из CSV
    file_data = read_files(args.files)

    # Получаем объект отчета
    report = get_report(args.report)

    # Строим отчет
    result = report.build(file_data)

    # Выводим в консоль таблицу
    print(tabulate(result, headers='keys', tablefmt='grid'))


if __name__ == '__main__':
    main()
