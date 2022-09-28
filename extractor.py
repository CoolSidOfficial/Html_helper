import os.path 
import time
import openpyxl
from colorama import Fore, Style,Back,init
#############################################################################################################################
def path_checker():
  '''This will just cin the file path and valdiate the input '''
  print(Fore.GREEN+Style.BRIGHT+"Please enter file path to extract  the excel file")
  file_inp=input("[#>>]")
  if file_inp.split('.')[1] !=  "xlsx":
    print(Fore.RED+"YOU CAN ONLY UPLOAD EXCEL FILE (xlsx)".center(80) )
  if file_inp=="":
     print("You have given an empty string")
     time.sleep(3)
     path_checker()
  elif file_inp=="exit":
       print("Thanks for using ,our program" )
       print("Exitting")
       time.sleep()
       exit()
  if  not  os.path.isfile(file_inp) :
     print(Fore.WHITE+Style.BRIGHT+"This file does not exist ".center(80)) 
     time.sleep(1)
     exit()
  return file_inp      # return final  path
##################################################################################################################      
def opener(p):
   data=list()
   book=openpyxl.load_workbook(p)
   sheet=book.active
   print(Fore.GREEN+"Please enter the index  number  to copy the files".center(50))
   load_id=input("#>>>")
   if load_id=="":
       print("Please input some numbers")
       time.sleep(3)
       opener(p)
   for each  in sheet[load_id]:
       data.append(each.value)
   return data

#########################################################################################################################

#############################################################################################################################
if __name__=="__main__":
 final_path=path_checker()
 opener(final_path)
