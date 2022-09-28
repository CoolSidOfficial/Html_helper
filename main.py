 ################ --custom--#########################################################
from titlename import title
from extractor import path_checker, opener     
import copyer 
######################################################################################
import pynput 
import pyautogui
import time
from os import system
from colorama import Fore,Back,init,Style
#############################################################################################################################
init()
########################################################################################
def logger(path='',read=False):
   ''' this  will try to save the  file path in the file named lastfile.txt  
   '''
   if read:
      try:
       with open("lastfile.txt","r") as file:
         return file.readline()
      except:
         print(Fore.RED+Back.BLUE+"Recent file does not exist upload a new one".center(80))
         time.sleep(5)
         starter()
   else:    
        with open("lastfile.txt","w")as file:
          file.write(path)
        

#############################################################################################################################
def starter():
  '''This  function will ask if the user want to open a recent  file or open another excel file 
  ,recent file path will be decide by  taken  the last  file oned '''
  
  system("cls")    # in linux we need to modify it to "clear"
  print(Fore.RED+title)
  print(Fore.GREEN+Style.BRIGHT+"Choose an option from below \n[1] Open recent excel file\n[2]Upload another excel file".center(23)  )
  c1=input(Fore.LIGHTBLUE_EX+"[#>>>]")
  if c1=="1" or c1=="one" :
   file_path=logger(read=True)   #this will return final_path    
   return opener(file_path)   #this will open finalpath, opener function available in extract.py
  elif c1=="2" or c1=="two":
    final_path=path_checker()
    logger(final_path)     # this will save file path 
    return opener(final_path)
  elif c1=="exit" : 
    print("Thanks for using our program ")
    print("Exitting")
    time.sleep(5)
    exit()
  else :
      print("Wrong input :(( Please try again")
      time.sleep(1)
      starter()
 

#############################################################################################################################
if __name__=="__main__":
 final_list= starter()   #this will create a list
 system("cls")  
 print(Fore.BLUE+Style.BRIGHT+'''These are the shortcut keys that you can use to paste your texts
 \n[1]id->ctrl + [
\n[2]title-text>ctrl + ]
\n[3]url->ctrl+ alt +;
\n[4]html-text->ctrl + m 
 ''')
 print(Fore.GREEN+"".center(130,"-"))
 print(Fore.BLACK+Style.BRIGHT+Back.BLACK+ "YOU CAN PASTE NOW ".center(90))
 copyer.log_keys(final_list) # sending list to copy 





