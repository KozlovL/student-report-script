from src.reports.base import BaseReport
from src.reports.median_coffee import MedianCoffeeReport

# Константа, содержащая доступные отчёты
REPORTS: dict[str, type[BaseReport]] = {
    'median-coffee': MedianCoffeeReport,
}


def get_report(name: str) -> BaseReport:
    """Возвращает объект отчета по имени."""
    # Создаем экземпляр класса отчета
    return REPORTS[name]()
