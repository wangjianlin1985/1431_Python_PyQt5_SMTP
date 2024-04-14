# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
from smtp.Mail import MailConfig
from smtp.SmtpUtil import Smtp

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    smtp=Smtp()
    smtp.loginSmtp()
    smtp.sendMessage("test","text","test@qq.com")
    #smtp.sendFile('smtpIcon.png','D:/pythonProject/smpt/res/smtpIcon.png',"2097557613@qq.com")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
