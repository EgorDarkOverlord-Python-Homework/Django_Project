"""
Модуль для класса заданий
"""

class Task:
    """
        Класс задания
        Содержит строку с математической задачей и правильный ответ
    """

    def __init__(self, task_string, correct_answer):
        self.task_string = task_string
        self.correct_answer = correct_answer

    def to_dict(self):
        """
        Преобразование класса в словарь
        """
        return {
            'task_string': self.task_string,
            'correct_answer': self.correct_answer,
        }

    @classmethod
    def from_dict(cls, data):
        """
        Преобразование словаря в класс
        """
        return cls(data['task_string'], data['correct_answer'])
