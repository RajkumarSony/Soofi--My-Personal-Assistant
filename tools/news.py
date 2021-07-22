
from tools.speaker import speak
import requests      
  
def latest_news(): 
    main_url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=9fbba8b1083d41088c1e1bb686804abb"
  
    page = requests.get(main_url).json() 
    article = page["articles"] 
    results = [] 
      
    for ar in article: 
        results.append(ar["title"]) 

    speak("Hello sir, i collected some Latest news, that are...")    
    print("Latest news, that are...\n") 

    for i in range(len(results)): 
        print(i + 1, results[i])  
        speak(results[i])          

