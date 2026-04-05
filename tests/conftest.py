import sys

import pytest

from src.utils import REPORTS
from tests.constants import FILE_ARG, MAIN_PATH, REPORT_ARG, TEST_FILES


@pytest.fixture
def valid_files():
    """Фикстура, возвращающая валидные файлы."""
    return TEST_FILES

@pytest.fixture
def valid_report():
    """Фикстура, возвращающая валидные файлы."""
    return list(REPORTS.keys())[0]

@pytest.fixture
def build_argv():
    """Функция для построения списка argv для тестов CLI."""
    def _build(files=None, report=None, extra_args=None):
        """
        files: список файлов
        report: название отчета
        extra_args: список дополнительных/некорректных аргументов
        """
        argv = [MAIN_PATH]
        if files is not None:
            argv.append(FILE_ARG)
            argv.extend(files)
        if report is not None:
            argv.append(REPORT_ARG)
            argv.append(report)
        if extra_args:
            argv.extend(extra_args)
        return argv
    return _build

@pytest.fixture
def csv_files(tmp_path):
    """Фикстура для создания временных CSV-файлов с содержимым."""
    def _create(files_content):
        """
        files_content: список кортежей (имя_файла, содержимое)
        Возвращает список путей к созданным файлам.
        """
        paths = []
        for filename, content in files_content:
            file_path = tmp_path / filename
            file_path.write_text(content, encoding='utf-8')
            paths.append(str(file_path))
        return paths
    return _create

@pytest.fixture
def mock_sys_exit(monkeypatch):
    """Фикстура для перехвата sys.exit."""
    exit_called = {}
    def fake_exit(code):
        exit_called['code'] = code
        raise SystemExit(code)
    monkeypatch.setattr(sys, 'exit', fake_exit)
    return exit_called
