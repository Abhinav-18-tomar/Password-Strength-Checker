import re 
from common_passwords import common


def check(usrInput):
        score=0
        if common(usrInput)==True:
            return "ERROR! Common Password"
    
        if len(usrInput)>=8:
            score+=1

        if re.search("[A-Z]",usrInput):
            score+=1

        if re.search("[a-z]",usrInput):
            score+=1

        if re.search("[1-9]",usrInput):
            score+=1

        if re.search("[~!@#$%^&*_]",usrInput):
            score+=1


        if score<=2:
         return "Very weak"

        elif score==3:
         return "weak"

        elif score==4:
         return "good"

        else:
         return "Excellent"



    