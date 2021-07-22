
import datetime
from tools.speaker import speak
def get_current_date():
    now = datetime.datetime.today().now()
    day = now.strftime("%a , %d  %b ' %Y")
    # print(day)
    return day

def get_current_time():
    Current_Date = str(datetime.datetime.today())
    hh = int(Current_Date[11:13])

    if (hh  >= 12):
        hh = hh % 12
        if(hh < 10):
            hh = "0"+str(hh)
        else:
            hh = str(hh)
    elif (hh <10):
        hh = "0"+str(hh)
    else:
        hh = str(hh)
            
    mm = int(Current_Date[14:16])
    if (mm  < 10):
        mm = "0"+str(mm)
    # print(str(hh)+":"+str(mm))
    return str(hh)+" : "+str(mm)

def get_meridien():
    Current_Date = str(datetime.datetime.today())
    hh = int(Current_Date[11:13])
    # print('Current Date: ' + str(hh))
    if ( hh >= 0 and hh < 12 ):
        return "AM"
    else:
        return "PM"

def say_time(self): 

    time = str(datetime.datetime.now()) 

    hour = time[11:13] 
    min = time[14:16] 
    speak("Sir, The time is " + str(hour) + " Hours and " + str(min) + " Minutes")      
