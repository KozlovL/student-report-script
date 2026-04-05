import argparse

from src.utils import REPORTS


def parse_args() -> argparse.Namespace:
    """Обрабатывает аргументы командной строки."""
    parser = argparse.ArgumentParser(description='Формирование отчетов по студентам')
    parser.add_argument(
        '--files',
        nargs='+',
        required=True,
        help='Список CSV-файлов для обработки'
    )
    parser.add_argument(
        '--report',
        required=True,
        choices=REPORTS.keys(),
        help='Название отчета'
    )
    return parser.parse_args()
