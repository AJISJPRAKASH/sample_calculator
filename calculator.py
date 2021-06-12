#import python gui tkinter
from tkinter import *
#create a function to do action button click
def btnclick(numbers):
    global opr
    if opr=="0":
        opr=str(numbers)
        txt_ip.set(opr)
    else:
        opr = opr + str(numbers)
        txt_ip.set(opr)
#create a function to do action clear button click
def btnclr():
        global opr
        opr = "0"
        txt_ip.set(opr)


# create a function to do execute  of equal button
def btneql():
    global opr
    clsum = str(eval(opr))
    opr=clsum
    txt_ip.set(clsum)
#create a new window to display
window = Tk()
#Give title name to window
window.title("Calculator")
#Set the window with no resizable
window.resizable(height = 0, width = 0)
opr=""
txt_ip=StringVar()
#create a empty entry to display our calculator output
tst_display=Entry(window,textvariable= txt_ip, font=('calibre',20, 'bold'),bd=30,insertwidth=4,
						bg="SlateBlue1",justify='right').grid(columnspan=4)

#create all buttons
i=18
button1=Button(window,text="1",padx=i,bd=8,fg="black",font=('calibre',20, 'bold'),bg="SlateGray1",command=lambda:btnclick(1))
button2=Button(window,text="2",padx=i,bd=8,fg="black",font=('calibre',20, 'bold'),bg="SlateGray1",command=lambda:btnclick(2))
button3=Button(window,text="3",padx=i,bd=8,fg="black",font=('calibre',20, 'bold'),bg="SlateGray1",command=lambda:btnclick(3))
button4=Button(window,text="4",padx=i,bd=8,fg="black",font=('calibre',20, 'bold'),bg="SlateGray1",command=lambda:btnclick(4))
button5=Button(window,text="5",padx=i,bd=8,fg="black",font=('calibre',20, 'bold'),bg="SlateGray1",command=lambda:btnclick(5))
button6=Button(window,text="6",padx=i,bd=8,fg="black",font=('calibre',20, 'bold'),bg="SlateGray1",command=lambda:btnclick(6))
button7=Button(window,text="7",padx=i,bd=8,fg="black",font=('calibre',20, 'bold'),bg="SlateGray1",command=lambda:btnclick(7))
button8=Button(window,text="8",padx=i,bd=8,fg="black",font=('calibre',20, 'bold'),bg="SlateGray1",command=lambda:btnclick(8))
button9=Button(window,text="9",padx=i,bd=8,fg="black",font=('calibre',20, 'bold'),bg="SlateGray1",command=lambda:btnclick(9))
button0=Button(window,text="0",padx=i,bd=8,fg="black",font=('calibre',20, 'bold'),bg="SlateGray1",command=lambda:btnclick(0))
addbtn=Button(window,text="+",padx=i,bd=8,fg="black",font=('calibre',20, 'bold'),bg="SlateGray1",command=lambda:btnclick('+'))
subtn=Button(window,text="-",padx=i,bd=8,fg="black",font=('calibre',20, 'bold'),bg="SlateGray1",command=lambda:btnclick('-'))
divbtn=Button(window,text="/",padx=i,bd=8,fg="black",font=('calibre',20, 'bold'),bg="SlateGray1",command=lambda:btnclick('/'))
mulbtn=Button(window,text="*",padx=i,bd=8,fg="black",font=('calibre',20, 'bold'),bg="SlateGray1",command=lambda:btnclick('*'))
clbtn=Button(window,text="C",padx=i,bd=8,fg="black",font=('calibre',20, 'bold'),bg="OrangeRed2",command=lambda:btnclr())
eqlbtn=Button(window,text="=",padx=i,bd=8,fg="black",font=('calibre',20, 'bold'),bg="SlateGray1",command=lambda:btneql())


#set the button positions

button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)
addbtn.grid(row=2,column=3)
button4.grid(row=3,column=0)
button5.grid(row=3,column=1)
button6.grid(row=3,column=2)
subtn.grid(row=3,column=3)
button1.grid(row=4,column=0)
button2.grid(row=4,column=1)
button3.grid(row=4,column=2)
mulbtn.grid(row=4,column=3)
clbtn.grid(row=5,column=0)
button0.grid(row=5,column=1)
eqlbtn.grid(row=5,column=2)
divbtn.grid(row=5,column=3)





#run the tkinter event loops
window.mainloop()


