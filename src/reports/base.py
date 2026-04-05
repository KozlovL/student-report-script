from abc import ABC, abstractmethod
from typing import Any


class BaseReport(ABC):
    """Абстрактный класс отчёта."""
    @abstractmethod
    def build(self, data: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Метод, реализующий создание отчёта."""
