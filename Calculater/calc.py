import tkinter as tk
import math
import time

root=tk.Tk()
root.title("Simple Calculator")
root.iconbitmap("calc.ico")

root.geometry("400x400")

e=tk.Entry(root,font="Calibri 15",width="35",borderwidth=5)
e.grid(row=0,column=0,columnspan=4,ipadx=10,ipady=15)
#Function
global i #to get track Number of operators : i=0 means there is no operator i=1 mean already operators
i=0
def Buttonclick(number):
    global i
    if i!=3:
        current=e.get()
        e.delete(0,tk.END)
        e.insert(0,str(current)+str(number))
    
def Buttonclear():
    global i
    e.delete(0,tk.END)
    i=0


def Buttonoperator(symb):
    global f,op,i
    if i==0:
        try:            
            op=symb
            i=1
            first=float(e.get())
            f=first
            e.delete(0,tk.END)
        
        except ValueError :
            Buttonclear()
    elif i==1:
        try:
            Buttonequal()
            first=float(e.get())
            f=first
            e.delete(0,tk.END)
            op=symb
            i=1
        except:
            op=symb

#calculation
def Buttonequal():
    global f,op,i
    if i==1:
        try :
            second=float(e.get())
            e.delete(0,tk.END)
            if op=="+" :
                temp=f+second
                if math.modf(temp)[0]==0:
                    result=int(temp)
                else:
                    result=float(temp)
                e.insert(0,result )
                op="$"
                i=0

            if op=="-" :
                temp=f-second
                if math.modf(temp)[0]==0:
                    result=int(temp)
                else:
                    result=float(temp)
                e.insert(0,result )
                op="$"
                i=0

            if op=="*" :
                temp=f*second
                if math.modf(temp)[0]==0:
                    result=int(temp)
                else:
                    result=float(temp)
                e.insert(0,result )
                op="$"
                i=0


            if op=="/" :
                temp=f/second
                if math.modf(temp)[0]==0:
                    result=int(temp)
                else:
                    result=float(temp)
                e.insert(0,result )
                op="$"
                i=0
        except ZeroDivisionError:
            i=3
            e.insert(0,"Can Not Divide By Zero")
           
        except Exception  :
            pass
            


#define Buttons
b1=tk.Button(root,text="1",padx=25,pady=25,borderwidth=5,relief="raised",command=lambda :Buttonclick(1))
b2=tk.Button(root,text="2",padx=25,pady=25,borderwidth=5,relief="raised",command=lambda :Buttonclick(2))
b3=tk.Button(root,text="3",padx=25,pady=25,borderwidth=5,relief="raised",command=lambda :Buttonclick(3))
b4=tk.Button(root,text="4",padx=25,pady=25,borderwidth=5,relief="raised",command=lambda :Buttonclick(4))
b5=tk.Button(root,text="5",padx=25,pady=25,borderwidth=5,relief="raised",command=lambda :Buttonclick(5))
b6=tk.Button(root,text="6",padx=25,pady=25,borderwidth=5,relief="raised",command=lambda :Buttonclick(6))
b7=tk.Button(root,text="7",padx=25,pady=25,borderwidth=5,relief="raised",command=lambda :Buttonclick(7))
b8=tk.Button(root,text="8",padx=25,pady=25,borderwidth=5,relief="raised",command=lambda :Buttonclick(8))
b9=tk.Button(root,text="9",padx=25,pady=25,borderwidth=5,relief="raised",command=lambda :Buttonclick(9))
b0=tk.Button(root,text="0",padx=25,pady=25,borderwidth=5,relief="raised",command=lambda :Buttonclick(0))

b_add=tk.Button(root,text="+",padx=25,pady=25,borderwidth=5,relief="raised",command=lambda :Buttonoperator("+"))
b_sub=tk.Button(root,text="-",padx=25,pady=25,borderwidth=5,relief="raised",command=lambda :Buttonoperator("-"))
b_mul=tk.Button(root,text="*",padx=25,pady=25,borderwidth=5,relief="raised",command=lambda :Buttonoperator("*"))
b_div=tk.Button(root,text="/",padx=25,pady=25,borderwidth=5,relief="raised",command=lambda :Buttonoperator("/"))
b_clr=tk.Button(root,text="C",padx=23,pady=25,borderwidth=5,relief="raised",command= Buttonclear)
b_equal=tk.Button(root,text="=",padx=25,pady=25,borderwidth=5,relief="raised",command=Buttonequal)

#place buttons

b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
b_mul.grid(row=3,column=3)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b_div.grid(row=2,column=3)

b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)
b_clr.grid(row=1,column=3)

b_add.grid(row=4,column=0)
b0.grid(row=4,column=1)
b_sub.grid(row=4,column=2)
b_equal.grid(row=4,column=3)


root.mainloop()