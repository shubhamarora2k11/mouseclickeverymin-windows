#30 min

import time
from time import gmtime, strftime
c=0

while c<=30:
    pyautogui.click(100, 100)
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    time.sleep(60)
    
    c+=1


 
 
	
