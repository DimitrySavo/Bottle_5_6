from bottle import post, request

@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADDRESS')
    return f"Thanks! The andwer will be sent to the mail {mail}"