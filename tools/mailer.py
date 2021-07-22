
from tools.domain_validate import isValidEmail
from tools.tools_module import *
from tools.notifyer import notification
from pyautogui import *
import smtplib

email = ""
msg = ""

def send_email(inputType,self):
    speak("It's my pleasure, Now Email Service is ready. Please try to enter the email id...")
    
    global email
    global msg
    try:
        # if inputType in ['userInput']:
        #     email = prompt(text='Enter E-mail Id', title='Say Something..' , default='').lower()
        # else:
        #     email = takeCommand(self).lower()
        email = prompt(text='Enter E-mail Id', title='Say Something..' , default='').lower()
    
    except:
        speak("Sorry, I am not able to understand...")
        send_email(inputType,self)

    try:
        if (isValidEmail(email)):
            speak("Enter the message, what do you want to send...")
            if inputType in ['userInput']:
                msg = prompt(text='Enter Message', title='Say Something..' , default='').lower()
            else:
                msg = takeCommand(self).lower()
        else:
            speak('Sorry, Your email id is invalid... please try again..')
            # send_email(inputType,self)

    except:
        speak("Sorry, I am not able to understand...")
        send_email(inputType,self)
    try:
        if msg != "":
            speak("Please wait...")
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login('rk.sony4848@gmail.com', 'zdkubbozpxwahvpm')
            server.sendmail('rk.sony4848@gmail.com', email, msg)
            speak("Your email has been sent successfully...")
            print("Email Sent!")
            server.close()
            notification("Email Sent!","You email has been sent to "+email+". Successfully!")
        else:
            return
    except Exception:
        speak("Connection not able establish, due to network issue Or password is not correct...Try again!")
        return
        # send_email(inputType,self)
    