#-------------------------------------------------------------------------------
# Name:        Simple Calculator 1.0
# Purpose:
#
# Author:      NTFL
#
# Created:     27.04.2023
# Copyright:   (c) NTFL Software 2023
# Licence:     <GNU License>
#-------------------------------------------------------------------------------


# определяем функцию для добавления
def add(x, y):
    return x + y

# определить функцию для вычитания
def subtract(x, y):
    return x - y

# определяем функцию умножения
def multiply(x, y):
    return x * y

# определяем функцию для деления
def divide(x, y):
    return x / y

# получить пользовательский ввод для операции
operation = input("Введите операцию, которую вы хотите выполнить (+, -, *, /): ")

try:
    # получить пользовательский ввод для чисел
    x = float(input("Введите первое число:"))
    y = float(input("Введите второе число: "))

    # выполнить выбранную операцию
    if operation == "+":
        result = add(x, y)

    elif operation == "-":
        result = subtract(x, y)

    elif operation == "*":
        result = multiply(x, y)

    elif operation == "/":
        result = divide(x, y)

    else:
        print("Выбрана неверная операция")
        result = None

    # ошибка типа переменной
except ValueError as v:
    print("Ошибка типа переменной: ", v)

try:
    # распечатать результат
    if result is not None:
        print("Результат: ", result)

    # ошибка вычисления результата
except NameError as n:
    print("Ошибка вычисления результата: ", n)


