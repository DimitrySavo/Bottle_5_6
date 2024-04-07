from bottle import post, request
import re

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADRESS')
    if(is_valid_email(mail)):
        return f"Thanks! The andwer will be sent to the mail {mail}"
    else:
        return "Invalid email adress"