import pytest
from src.reader import read_files

@pytest.mark.parametrize(
    'files_content, expected_rows',
    (
        pytest.param(
            [
                ('математика.csv', 'имя,балл\nАлиса,90\nБоб,80'),
                ('физика.csv', 'имя,балл\nЧарли,85\nДана,95')
            ],
            [
                {'имя': 'Алиса', 'балл': '90'},
                {'имя': 'Боб', 'балл': '80'},
                {'имя': 'Чарли', 'балл': '85'},
                {'имя': 'Дана', 'балл': '95'}
            ],
            id='multiple_files_correct_data'
        ),
        pytest.param(
            [
                ('empty.csv', '')
            ],
            [],
            id='empty_file'
        )
    )
)
def test_read_files(csv_files, files_content, expected_rows):
    """Проверяем чтение CSV-файлов с корректными данными и пустыми файлами."""
    file_paths = csv_files(files_content)
    result = read_files(file_paths)
    assert result == expected_rows


@pytest.mark.parametrize(
    'file_path',
    (
        pytest.param('no_such_file.csv', id='file_not_found'),
        pytest.param('', id='empty_file_path')
    )
)
def test_read_files_file_not_found(mock_sys_exit, file_path):
    """Проверяем, что read_files вызывает sys.exit при отсутствии файла."""
    with pytest.raises(SystemExit):
        read_files([file_path])
    assert mock_sys_exit['code'] == 1
