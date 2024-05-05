from bottle import post, request, response
import re
import json
import pdb
import os
from datetime import date

#функция, которая возвращает булевое значение в зависимости от прохождения паттерна
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]{2,7})+$" 
    return bool(re.match(pattern, email))

@post('/home', method='post')
def my_form():

    if os.path.exists('jsonQuestions.json') and os.path.getsize('jsonQuestions.json') > 0: #если файл не пустой и существует - читается в словарь
        questions = json.load(open('jsonQuestions.json', 'r'))
    else:
        questions = {} #если файл пустой - просто создается пустой словарь

    #Инициализация переменных
    question = request.forms.get('QUEST')
    mail = request.forms.get('ADRESS')
    name = request.forms.get('USERNAME')
    today = date.today()

    
    if(name == "" or mail == "" or question == ""): #Проверка на пустоту полей ввода
        return "Please, fill all fields"
    elif(all(char.isdigit() for char in question[:-1])): #Если пароль состоит только из цифр
        return "Question cant contain only digits"
    elif(len(question) < 3): #Если длинна вопроса меньше 3х символов 
        return "Question is to short. Minimum length is 4 symbols"
    elif(not is_valid_email(mail)): #Если емаил неправильно написан
        return "Invalid email adress"
    elif(question[-1] != '?'): #Если вопрос не заканчивается на знак вопроса
        return "Question should ends with questionmark"
    else:
        if mail in questions: #Если емаил уже есть в словаре с вопросами
            if question in questions[mail]: #Если такой вопрос уже задавали
                return "This question was already asked"
            else: #Если вопрос не задан - он вносится в словарь
                
                questions[mail].append(question)
                json.dump(questions, open('jsonQuestions.json', 'w'))
        else: # Если емаила нет - он вносится в словарь
            questions[mail] = [question]
            json.dump(questions, open('jsonQuestions.json', 'w'))
        return f"Thanks, {name}! The answer will be sent to the mail {mail}. Access date: {today}"