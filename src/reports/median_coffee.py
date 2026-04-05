from collections import defaultdict
from statistics import median
from typing import Any

from src.reports.base import BaseReport


class MedianCoffeeReport(BaseReport):
    """Класс отчёта для медианы трат на кофе."""
    def build(self, data: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Метод, реализующий создание отчёта для медианы трат на кофе."""

        # Словарь, где ключи - имена студентов, значения - списки трат на кофе
        student_coffee_spent_dict: dict[str, list] = defaultdict(list)

        # Собираем траты по каждому студенту
        for row in data:
            # Сохраняем имя студента
            student = row['student']
            # Сохраняем трату на кофе
            coffee_spent = int(row['coffee_spent'])
            # Добавляем по ключу студента трату на кофе
            student_coffee_spent_dict[student].append(coffee_spent)

        # Список словарей, где каждый словарь содержит студента и медиану трат на кофе
        result: list[dict[str, str | int]] = []

        # Считаем медиану
        for student, values in student_coffee_spent_dict.items():
            result.append({
                'student': student,
                'median_coffee': int(median(values))
            })

        # Сортируем по убыванию
        result.sort(key=lambda x: x['median_coffee'], reverse=True)

        return result
