"""
Модуль для отображения страниц
"""

from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import  task_generation

def index(request):
    """
    Главная страница
    """
    return render(request, "index.html")

def start(request):
    """
    Страница старта с настройками теста
    """
    if request.method == "POST":
        request.session['difficulty'] = request.POST.get("difficulty")
        request.session['task_count'] = int(request.POST.get("task_count"))
        request.session['task_number'] = 1
        request.session['tasks'] = []
        request.session['answers'] = []
        request.session.modified = True
        return HttpResponseRedirect("test")

    return render(request, "start.html")

def test(request):
    """
    Страница с задачей
    """
    difficulty = request.session['difficulty']
    task_count = request.session['task_count']
    task_number = request.session['task_number']
    tasks = request.session['tasks']

    if request.method == "POST":
        task_number += 1
        request.session['task_number'] = task_number
        request.session['answers'].append(int(request.POST.get("answer")))
        request.session.modified = True

        if task_number - 1 == task_count:
            return HttpResponseRedirect("score")

    if len(tasks) < task_number:
        task_generator = task_generation.TaskGenerator()
        task = task_generator.generate_task(difficulty)
        request.session['tasks'].append(task.to_dict())
        request.session.modified = True

    context = {
        "task_number": task_number,
        "task_count": task_count,
        "task": tasks[task_number - 1],
    }

    return render(request, "test.html", context=context)

def score(request):
    """
    Страница с итогами теста
    """
    task_count = int(request.session['task_count'])
    tasks = request.session['tasks']
    answers = request.session['answers']
    correct = []

    for i in range(task_count):
        correct.append(answers[i] == tasks[i]["correct_answer"])

    correct_count = correct.count(True)

    context = {
        "task_count": task_count,
        "correct_count": correct_count,
        "stats": zip(tasks, answers, correct)
    }

    return render(request, "score.html", context=context)
