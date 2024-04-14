from bottle import post, request, response
import re
import json
import pdb
import os
from datetime import date

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]{2,7})+$"
    return bool(re.match(pattern, email))

@post('/home', method='post')
def my_form():
    if os.path.getsize('jsonQuestions.json') > 0:
        questions = json.load(open('jsonQuestions.json', 'r'))
    else:
        questions = {}

    question = request.forms.get('QUEST')
    mail = request.forms.get('ADRESS')
    name = request.forms.get('USERNAME')
    today = date.today()
    if(name == "" or mail == "" or question == ""):
        return "Please, fill all the fields"
    elif(any(char.isdigit() for char in question) or len(question) < 3):
        return "Invalid question"
    elif(not is_valid_email(mail)):
        return "Invalid email adress"
    else:
        if mail in questions:
            if question in questions[mail]:
                return "This question was already asked"
            else:
                questions[mail].append(question)
                json.dump(questions, open('jsonQuestions.json', 'w'))
        else:
            questions[mail] = [question]
            json.dump(questions, open('jsonQuestions.json', 'w'))
        return f"Thanks, {name}! The answer will be sent to the mail {mail}. Access date: {today}"