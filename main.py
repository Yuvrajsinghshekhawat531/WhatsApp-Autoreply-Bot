import pyautogui as pa
import time
import pyperclip as pc
import google.generativeai as gg
import keyboard
import pyttsx3 as py
a=py.init()
a.setProperty('rate',125)
def say(text):
    a.say(text)
    
    a.runAndWait()



gg.configure(api_key='AIzaSyDqfiIwwj890uYADBVk6o59xM1Jyxuysm0')
modal=gg.GenerativeModel("gemini-1.5-flash")

pa.click(600,1051)

time.sleep(0.1)

running=True

def stop():
    global running
    running= False

keyboard.add_hotkey("delete",stop)


while running:
    
    pa.moveTo(717,179)
    # pa.mouseDown()
    pa.dragTo(729,992,duration=1,button="left")
    time.sleep(0.1)
    pa.hotkey('ctrl','c')
    time.sleep(0.1)
    pa.click(1303,552)

    sentence= pc.paste()



    result= modal.generate_content(f"""I will provide you a short message received from a friend or relative.you also translate all messages in indi.Your job is to reply in the same tone and language is hindi and the language of message is in but write replay in english only.The reply should be:- Short (between 10 to 20 words)- Casual and natural- No refusal, no expectation, no extra words like "no", "yes", "okay", etc.Message: {sentence}Reply:""")
    
    pc.copy(result.text)
    pa.click(1116,962)    
    time.sleep(0.1)
    pa.hotkey('ctrl','v')
    say(f"I send {result.text}")
    time.sleep(1)
    pa.hotkey('enter')
    
    say("If you want to close me than press DELETE button")
    time.sleep(18)
   
    

