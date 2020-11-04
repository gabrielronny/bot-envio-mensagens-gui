import pyautogui, requests

while True: 
    response = requests.get("http://asdfast.beobit.net/api/?type=word")
    word = response.json()["text"]

    pyautogui.typewrite(word)
    pyautogui.press("enter")
