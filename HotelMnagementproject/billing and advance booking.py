from tkinter import *
import tkinter.messagebox as tmg

root=Tk()
root.geometry("500x500")
root.maxsize(500,500)


can_widget=Canvas(root,width=10000 , height=10000)
can_widget.pack()
m=PhotoImage(file=".sgif")
can_widget.create_image(0, 0, anchor=NW, image=m)
#the line goes from the point x1,y1 to x2,y2
#can_widget.create_line(0,0,800,200,fill="red")
#can_widget.create_line(0,200,800,0,fill="grey")


can_widget.create_rectangle(15,10,470,430)

frame=Frame(can_widget ,width=800,height=800, borderwidth=10,relief=RAISED)

frame.place(x=100,y=150)

'''frame=Frame(root ,width=500,height=500, borderwidth=10,relief=RAISED)
frame.place(x=100,y=150)'''


l=Label(root,text="Booking!!",bg='red',relief=RAISED,font="comicsansms 16 bold")
l.place(x=120,y=100)

import pandas as pd
#menu
def show_records():
    a=pd.read_csv(r"records.txt")
    print(a)
def quit():
    b = tmg.askquestion("sure", "you want to exit!!")
    print(b)
    if b=='yes':
        import sys; sys.exit()

        print("Exit Click, so let's stop")

counter=0
def Save():
    global counter
    a=(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emailvalue.get(),paymentmodevalue.get(),foodservicevalue.get()}")
    print(a)
    a=tmg.Message("")
mymenu = Menu(root)
m1=Menu(mymenu,tearoff=0)
m1.add_command(label="File",command=show_records)
#m1.add_Seperator()
m1.add_command(label="Save",command=Save)
m1.add_command(label="Print",command=show_records)
root.config(menu=mymenu)
mymenu.add_cascade(label="File1",menu=m1)
#2nd menu

m2=Menu(mymenu,tearoff=0)
m2.add_command(label="File",command=show_records)
#m1.add_Seperator()
m2.add_command(label="Exit",command=quit)
m2.add_command(label="Print",command=show_records)
root.config(menu=mymenu)
mymenu.add_cascade(label="File1",menu=m1)




#event handler
def ali(event):
   print(f"you clicked on the event!! at {event.x},{event.y}")
def quit(event):
    b = tmg.askquestion("sure", "you want to exit!!")
    print(b)
    if b=='yes':
        import sys; sys.exit()
        print("Exit Click, so let's stop")





#widget for exit
widget=Button(frame,text="exit")
widget.grid()



widget.bind('<Button-1>',quit)
#widget.bind('<Double-1>',quit)






#defgetvals
counter=0
def getvals():
    c=tmg.showinfo("booked bill",100*int(daysvalue.get()))
    print(c)
    global counter

    a=(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emailvalue.get(),daysvalue.get(),100*int(daysvalue.get()),foodservicevalue.get()}")
    print(a)



    with open("records.txt","a") as f:
        f.write(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emailvalue.get(),daysvalue.get(),100*int(daysvalue.get()),foodservicevalue.get()}\n")
        if foodservicevalue.get()==1:
            counter+=1
        else:
            counter+=1
            print("booked!!")
        f.write(f"{'booked',counter}")






#Label(name outside box)
name=Label(frame,text="Name").grid(row=1,column=2,pady=4)
phone=Label(frame,text="phone").grid(row=2,column=2,pady=4)
gender=Label(frame,text="gender").grid(row=3,column=2,pady=4)
email=Label(frame,text="email").grid(row=4,column=2,pady=4)
Days=Label(frame,text="days").grid(row=5,column=2,pady=4)
# bill=Label(frame,text="bill").grid(row=6,column=2,pady=4)




#initialize variable values
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=IntVar()
emailvalue=StringVar()
daysvalue=StringVar()
foodservicevalue=IntVar()
# billvalue=IntVar()

#entry
nameentry=Entry(frame,textvariable=namevalue)
phoneentry=Entry(frame,textvariable=phonevalue)
#genderentry=Entry(frame,textvariable=gendervalue)

#gendervalue.set(1)
#Label(frame,text="what would u like to have sir?", justify=LEFT,padx=14,font="lucida 19 bold").grid()
radio=Radiobutton(frame,text="Male",padx=14,variable=gendervalue,value=1).place(x=100,y=90)
radio=Radiobutton(frame,text="Female",padx=14,variable=gendervalue,value=2).place(x=160,y=90)
emailentry=Entry(frame,textvariable=emailvalue)
# paymentmodeentry=Entry(frame,textvariable=paymentmodevalue)
# billentry=Entry(frame,textvariable=billvalue)
daysentry=Entry(frame,textvariable=daysvalue)



#entry pack
nameentry.grid(row=1,column=3,padx=30)
phoneentry.grid(row=2,column=3,padx=30)
#genderentry.grid(row=3,column=3,padx=30)
emailentry.grid(row=4,column=3,padx=30)
daysentry.grid(row=5,column=3,padx=30)
# billentry.grid(row=6,column=3,padx=30)


#button
Button(frame,text="Submit",command=getvals).grid(row=11,column=3)


#checkbox
# foodservice=Checkbutton(frame,text="Accept!!",variable=foodservicevalue).grid(row=9,column=3)





root.mainloop()
