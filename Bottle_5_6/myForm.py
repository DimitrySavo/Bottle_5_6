from bottle import post, request, response
import re
import pdb
from datetime import date

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]{2,7})+$"
    return bool(re.match(pattern, email))

@post('/home', method='post')
def my_form():
    questions = {}

    question = request.forms.get('QUEST')
    mail = request.forms.get('ADRESS')
    name = request.forms.get('USERNAME')
    today = date.today()
    pdb.set_trace()
    if(name == "" or mail == "" or questions == ""):
        return "Please, fill all the fields"
    elif(not is_valid_email(mail)):
        return "Invalid email adress"
    else:
        questions[mail] = question
        return f"Thanks, {name}! The answer will be sent to the mail {mail}. Access date: {today}"