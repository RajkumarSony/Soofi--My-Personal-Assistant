
from tools.tools_module import *
import wolframalpha

appId = 'TKAPVA-Q2GP6VU62E'
client = wolframalpha.Client(appId)

question = ""
answer =""
def ask_quesion(inputType,self):
    global answer
    speak('Thank you.... Now I am ready to give, your answer. Please ask me,')
    speak('I can answer to computational and geographical questions, So, what question do you want to ask now...')
    
    global question
    
    if inputType in ['userInput']:
        question = prompt(text='Give me Question', title='Say Something..' , default='').lower()
    else:
        question = takeCommand(self).lower()
    if question != None:
        speak("The question is,"+question)
        speak('Please wait....')

        res = client.query(question)
        
        try:
            answer = next(res.results).text
        except:
            print('Invalid Question!')
            speak("Sorry, The given question is not valid. Please, try again!")
            return
    else:
        ask_quesion(inputType,self)

    if question in ['close edit mode' , 'close' , 'exit' , 'quit','return','back']:
        speak("Edit mode is successfully closed...")
    else:
    # print(answer)
        speak("The answer of this question is,"+answer)
        ask_quesion(inputType,self)

