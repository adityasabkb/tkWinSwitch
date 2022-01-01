# here i will show you how to use the tkWinSwitch module this is not a default module you get with python
#i have created it so you must download the tkWinSwitch.py from the repo before using 

from tkinter import *
from tkWinSwitch import *

root = Tk()
root.geometry("500x500")
############# MAKING THE WIDGET SET NUMBER 1##################
set1 = wiSet()

                                        #button 1 has the functionality to switch from set1 to set2
btn1 = set1.addWi(Button(root,text="button 1",command=lambda :switch(set1,set2) ) ) 

#or you could do btn1 = Button(root,text="button 1",command = lambda :switch(set1,set2))
#and then set1.addWi(btn1) 

#set.addWi(Widget) tells the program that the given widget is part of set1 

# now rather than doing btn1.place(x = 100,y=100)
set1.place(btn1,x=100,y=100)


# now we create a secon widget and add it to set1
l = set1.addWi(Label(text="this is screen 1"))

#now we place l as shown
#instead of doing l.place(x= 150,y = 150)
#we use the following syntax
set1.place(l,x=150,y=150)

#note this items are supposed to be place but are not for that we will do set1.create at the end

############# MAKING THE WIDGET SET NUMBER 1##################

#created set2
set2 = wiSet()

                                        #button 2 has the functionality to switch from set2 to set1
btn2 = set2.addWi(Button(root,text="button 2",command=lambda :switch(set2,set1))) #created btn2
# btn2 is part of set2 therefore we did set2.addWi

#you can also use grid and pack method 
set2.grid(btn2,0,0)
#or you could say set2.grid(btn2,row= 0,y = 0)

l2 = set2.addWi(Label(text="this is screen 2 and uses grid"))
set2.grid(l2,1,0)


# in case you wanted to pack a widget you colud do:
# <set>.pack(<widget>,<extra arguments eg. fill = BOTH,expand = True,etc..>)
#say i have setx and want to pack y with fill = BOTH and expand = TRUE, in that case I do:
#setx.pack(y,fill = BOTH ,expand = TRUE)

################################################

#finally creating set1 as default start
set1.create()


root.mainloop()
