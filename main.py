import webbrowser
import pyautogui
import time
import schedule

person = input("Enter Name Of The Person: ")
msg = input("Enter Message To Be Delivered: ")
hourtest = str(input("Enter Time"))


def sendmsg():


    webbrowser.open('https://web.whatsapp.com/')
    time.sleep(10)
    pyautogui.click(142, 179)
    pyautogui.typewrite(person)
    time.sleep(2)
    pyautogui.click(179, 337)
    pyautogui.click(569, 842)
    pyautogui.typewrite(msg)
    pyautogui.click(1402, 826)



schedule.every().day.at(hourtest).do(sendmsg)

while True:
    schedule.run_pending()
    time.sleep(1)




