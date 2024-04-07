from bottle import post, request, response
import re
from datetime import date

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADRESS')
    name = request.forms.get('USERNAME')
    today = date.today()
    if(name == "" or mail == ""):
        return "Please, fill all the fields"
    elif(not is_valid_email(mail)):
        return "Invalid email adress"
    else:
        return f"Thanks, {name}! The answer will be sent to the mail {mail}. Access date: {today}"