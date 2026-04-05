import pytest
from src.reports.median_coffee import MedianCoffeeReport

@pytest.mark.parametrize(
    'input_data, expected_output',
    (
        pytest.param(
            [
                {'student': 'Алиса', 'coffee_spent': '10'},
                {'student': 'Алиса', 'coffee_spent': '20'},
                {'student': 'Боб', 'coffee_spent': '15'},
                {'student': 'Боб', 'coffee_spent': '25'},
            ],
            [
                {'student': 'Боб', 'median_coffee': 20},
                {'student': 'Алиса', 'median_coffee': 15},
            ],
            id='two_students_sorted'
        ),
        pytest.param(
            [
                {'student': 'Чарли', 'coffee_spent': '30'},
            ],
            [
                {'student': 'Чарли', 'median_coffee': 30},
            ],
            id='single_student'
        ),
        pytest.param(
            [],
            [],
            id='empty_data'
        ),
        pytest.param(
            [
                {'student': 'Дана', 'coffee_spent': '5'},
                {'student': 'Дана', 'coffee_spent': '5'},
                {'student': 'Дана', 'coffee_spent': '5'},
            ],
            [
                {'student': 'Дана', 'median_coffee': 5},
            ],
            id='all_same_values'
        ),
    )
)
def test_median_coffee_report_build(input_data, expected_output):
    """Проверяем корректность построения отчёта MedianCoffeeReport."""
    report = MedianCoffeeReport()
    result = report.build(input_data)
    assert result == expected_output
