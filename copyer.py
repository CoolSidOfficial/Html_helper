from subprocess import IDLE_PRIORITY_CLASS
import pynput
import time
import pyperclip
import pyautogui
from colorama import Fore, Style,Back 
#################################################################################################################
# we will create four shortcut keys for each entry
#id->ctrl + [
#title->ctrl + ]
#url->ctrl+ alt +;
#html-text->ctrl + m
#############################################################################################
def id_copyer():  #id 
    print(Fore.GREEN+" ID Pasted-"+str(sample[0]))
    paste_it(sample[0])

def title_copyer():  #title
    print(Fore.GREEN+"Title Pasted-"+str(sample[2]))

    paste_it(sample[2])

def url_copyer():   # url 
   print(Fore.GREEN+"URL  Pasted-"+str(sample[3]))
   paste_it(sample[3])



def html_copyer():  # html_text
    print(Fore.GREEN+"Html Data  Pasted -CAN'T PREVIEW ")
    paste_it(sample[1])
    
def paste_it(data_to_p):
    pyperclip.copy(data_to_p)
    pyautogui.hotkey("ctrl","v")    

#########################################################################################

def exiter():
 print(Fore.GREEN+"thx for running me".center(80))
 time.sleep(3)
 exit()

######################################################################################

def log_keys(quant):
  global sample
  sample=quant
  with pynput.keyboard.GlobalHotKeys(
    {"<ctrl>+[" :id_copyer,  # id 
    "<ctrl>+]":title_copyer,
    "<ctrl>+;":url_copyer,
    "<ctrl>+m":html_copyer,
    "<ctrl>+'":exiter,
     }) as listener:
    listener.join()

###############################################################################################


if __name__=="__main__":
    sample= []  # sample data removed for privacy concerns
    log_keys(sample)

#Done