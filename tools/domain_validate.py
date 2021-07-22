
import re

def isValidDomain(str): 
    regex = "^((?!-)[A-Za-z0-9-]"+"{1,63}(?<!-)\\.)"+"+[A-Za-z]{2,6}"

    p = re.compile(regex)

    if (str == None):
        return False
        
    if(re.search(p, str)):
        return True
    else:
        return False
    
def isValidEmail(email):

    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if(re.search(regex,email)):  
        return True  
          
    else:  
        return False 