import pytest
import sys
from src.main import main
from src.utils import REPORTS


@pytest.mark.parametrize(
    'files_content, expected_order',
    [
        pytest.param(
            [
                ('students_single.csv',
                 'student,coffee_spent\n'
                 'Алиса,100\n'
                 'Алиса,150\n'
                 'Боб,200\n'
                 'Боб,50\n'
                 'Чарли,300\n'
                 'Чарли,100\n'
                 )
            ],
            ['Чарли', 'Боб', 'Алиса'],
            id='single_file_six_records'
        ),
        pytest.param(
            [
                ('file1.csv',
                 'student,coffee_spent\n'
                 'Алиса,100\n'
                 'Алиса,150\n'
                 'Боб,200\n'
                 'Боб,50\n'
                 ),
                ('file2.csv',
                 'student,coffee_spent\n'
                 'Чарли,300\n'
                 'Чарли,100\n'
                 )
            ],
            ['Чарли', 'Боб', 'Алиса'],
            id='two_files_six_records'
        ),
        pytest.param(
            [
                ('empty.csv', '')
            ],
            [],
            id='empty_file'
        ),
    ]
)
def test_main_correct(csv_files, capsys, build_argv, files_content, expected_order):
    """Проверяем работу скрипта с корректными данными (по 6 записей)."""
    file_paths = csv_files(files_content)
    report_name = 'median-coffee'

    # Строим argv через фикстуру
    sys.argv = build_argv(files=file_paths, report=report_name)

    # Запускаем main
    main()

    # Проверяем вывод в консоль
    captured = capsys.readouterr()
    output = captured.out

    for student in expected_order:
        assert student in output, f'{student} отсутствует в выводе'

    if expected_order:
        assert 'median_coffee' in output

@pytest.mark.parametrize(
    'files, report, extra_args',
    [
        pytest.param(
            ['nonexistent.csv'], 'median-coffee', None, id='file_not_found'
        ),
        pytest.param(
            None, 'unknown-report', None, id='report_not_found'
        ),
        pytest.param(
            None, None, None, id='no_arguments'
        ),
        pytest.param(
            [], 'median-coffee', None, id='files_without_value'
        ),
        pytest.param(
            ['students.csv'], None, None, id='report_without_value'
        ),
    ]
)
def test_main_invalid(monkeypatch, csv_files, mock_sys_exit, build_argv, files, report, extra_args):
    """Проверяем, что main вызывает SystemExit при некорректных аргументах."""
    # Создадим валидный файл для тестов, где он нужен
    if files and 'students.csv' in files:
        csv_files([('students.csv',
                    'student,coffee_spent\n'
                    'Алиса,100\n'
                    'Алиса,150\n'
                    'Боб,200\n'
                    'Боб,50\n'
                    'Чарли,300\n'
                    'Чарли,100\n')])

    argv = build_argv(files=files, report=report, extra_args=extra_args)
    monkeypatch.setattr(sys, 'argv', argv)

    with pytest.raises(SystemExit):
        main()
