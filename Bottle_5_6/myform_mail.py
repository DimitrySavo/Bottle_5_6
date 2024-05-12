import re

pattern = r"^[a-zA-Z0-9]{1}[a-zA-Z0-9_.+,*%$#!-]{0,254}@[a-zA-Z0-9-]{1,64}(\.[a-z0-9-]{2,7})+$" 

def check_mail(mail):
    return bool(re.match(pattern, mail))