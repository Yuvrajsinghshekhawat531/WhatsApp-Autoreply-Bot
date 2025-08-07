import google.generativeai as gg
import keyboard

gg.configure(api_key='AIzaSyBuSUve8b2gf6C8jNkmgyUJnvysU6m5j5A')
model=gg.GenerativeModel("gemini-1.5-flash")

running=True
def stop():
    global running
    running=False

keyboard.add_hotkey("Delete",stop)
while running:
   
    a= input("You ::")
    output=model.generate_content(f"''{a}'' answer in sort average 20 words")
    b=output.text
    print(f"Bot ::{b}")
