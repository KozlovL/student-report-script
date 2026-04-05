import sys
import pytest
from src.cli import parse_args
from src.utils import REPORTS
from tests.constants import TEST_FILES

def test_parse_args_correct(monkeypatch, build_argv, valid_files, valid_report):
    """Проверяем корректный парсинг аргументов через parse_args."""
    argv = build_argv(files=valid_files, report=valid_report)
    # Подменяем sys.argv для имитации командной строки
    monkeypatch.setattr(sys, 'argv', argv)
    
    parsed = parse_args()
    
    # Проверяем, что parse_args вернул правильные значения
    assert parsed.files == valid_files
    assert parsed.report == valid_report

@pytest.mark.parametrize(
    'files, report, extra_args',
    (
        pytest.param(
            None,
            list(REPORTS.keys())[0],
            None,
            id='missing_files',  # отсутствие --files
        ),
        pytest.param(
            TEST_FILES,
            None,
            None,
            id='missing_report',  # отсутствие --report
        ),
        pytest.param(
            TEST_FILES,
            list(REPORTS.keys())[0],
            ['--unknown'],
            id='unknown_arg',  # неизвестный аргумент
        ),
        pytest.param(
            [],
            list(REPORTS.keys())[0],
            None,
            id='empty_files',  # пустой список файлов
        ),
        pytest.param(
            TEST_FILES,
            'unknown_report',
            None,
            id='invalid_report',  # неизвестный отчет
        ),
    )
)
def test_parse_args_invalid(monkeypatch, build_argv, files, report, extra_args):
    """Проверяем, что parse_args вызывает SystemExit при некорректных аргументах."""
    argv = build_argv(files=files, report=report, extra_args=extra_args)
    monkeypatch.setattr(sys, 'argv', argv)

    with pytest.raises(SystemExit):
        parse_args()