
import pyautogui as oto
import time as zaman


print("5")
zaman.sleep(1)
print("4")
zaman.sleep(1)
print("3")
zaman.sleep(1)
print("2")
zaman.sleep(1)
print("1")
zaman.sleep(1)






oto.click(886,1058) #write ur google positon!!!!!
zaman.sleep(2)


oto.typewrite("Video link")
oto.press("enter")
zaman.sleep(3)


a = 1
i = 0
b = 0

oto.click(423,435) 

zaman.sleep(2)
while b < 22:
    b += 1
    oto.click(1910,1007) #for scroll screen
    zaman.sleep(0.4)




oto.click(240,356)
zaman.sleep(4)
while a == 1:
    i +=1
    i = str(i)
    oto.typewrite("Comment"+ i) #write ur commet
    oto.click(1128,419)
    zaman.sleep(2)
    oto.click(259,349)
    i = int(i)
    zaman.sleep(3)
    
    


