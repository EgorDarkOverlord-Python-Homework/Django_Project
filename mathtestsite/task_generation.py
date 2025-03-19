"""
Модуль для генерации заданий
"""

import random
from enum import Enum
from . import task

class Difficulty(Enum):
    """
    Перечисление - сложность
    """
    EASY = 'easy'
    MEDIUM = 'medium'
    HARD = 'hard'

class TaskGenerator:
    """
    Генератор заданий
    """
    def generate_task(self, difficulty):
        """
        Генерирует задание
        """
        index = random.randint(0, 3)
        if index == 0:
            return self.generate_sum(difficulty)
        if index == 1:
            return self.generate_substract(difficulty)
        if index == 2:
            return self.generate_multiply(difficulty)
        return self.generate_divide(difficulty)

    def generate_sum(self, difficulty):
        """
        Генерирует задание с суммой
        """
        term1 = None
        term2 = None
        if difficulty == Difficulty.EASY.value:
            term1 = random.randint(0, 10)
            term2 = random.randint(0, 10)
        elif difficulty == Difficulty.MEDIUM.value:
            term1 = random.randint(10, 100)
            term2 = random.randint(10, 100)
        elif difficulty == Difficulty.HARD.value:
            term1 = random.randint(100, 1000)
            term2 = random.randint(100, 1000)
        sum_res = term1 + term2
        return task.Task(f"{term1} + {term2}", sum_res)

    def generate_substract(self, difficulty):
        """
        Генерирует задание с разностью
        """
        minuend = None
        subtrahend = None
        if difficulty == Difficulty.EASY.value:
            minuend = random.randint(10, 20)
            subtrahend = random.randint(0, 10)
        elif difficulty == Difficulty.MEDIUM.value:
            minuend = random.randint(100, 200)
            subtrahend = random.randint(10, 100)
        elif difficulty == Difficulty.HARD.value:
            minuend = random.randint(1000, 2000)
            subtrahend = random.randint(100, 1000)
        difference = minuend - subtrahend
        return task.Task(f"{minuend} - {subtrahend}", difference)

    def generate_multiply(self, difficulty):
        """
        Генерирует задание с умножением
        """
        mult1 = None
        mult2 = None
        if difficulty == Difficulty.EASY.value:
            mult1 = random.randint(0, 10)
            mult2 = random.randint(0, 10)
        elif difficulty == Difficulty.MEDIUM.value:
            mult1 = random.randint(10, 100)
            mult2 = random.randint(0, 10)
        elif difficulty == Difficulty.HARD.value:
            mult1 = random.randint(10, 100)
            mult2 = random.randint(10, 100)
        multiply = mult1 * mult2
        return task.Task(f"{mult1} * {mult2}", multiply)

    def generate_divide(self, difficulty):
        """
        Генерирует задание с делением
        """
        quotient = None
        divisor = None
        if difficulty == Difficulty.EASY.value:
            quotient = random.randint(0, 10)
            divisor = random.randint(1, 10)
        elif difficulty == Difficulty.MEDIUM.value:
            quotient = random.randint(10, 100)
            divisor = random.randint(1, 10)
        elif difficulty == Difficulty.HARD.value:
            quotient = random.randint(10, 100)
            divisor = random.randint(10, 100)
        dividend = quotient * divisor
        return task.Task(f"{dividend} / {divisor}", quotient)
