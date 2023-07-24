import tkinter 
def main():
    window = tkinter.Tk()
    window.geometry("300x300")
    l1 = tkinter.Label(window,text="Number1",bg = "red",fg = "cyan",font = ("Arial",14))
    l2 = tkinter.Label(window,text="Number2",bg = "blue",fg = "white",font = ("Arial",14))
    l3 = tkinter.Label(window,text="T_Result",bg = "pink",fg = "blue",font = ("Arial",14))
    e1 = tkinter.Entry(window,width=10,font= ("Arial",14))
    e2 = tkinter.Entry(window,width=10,font= ("Arial",14))
    e3 = tkinter.Entry(window,width=10,font= ("Arial",14))
    l1.place(x=50,y=50)
    l2.place(x=50,y=100)
    l3.place(x=150,y=150)
    e1 = tkinter.Entry(window,width=10,bg="yellow",font=("Arial",14))
    e2 = tkinter.Entry(window,width=10,bg="green",font=("Arial",14))
    e3 = tkinter.Entry(window,width=10,bg="cyan",font=("Arial",14))
    e1.place(x=150,y=50)
    e2.place(x=150,y=100)
    e3.place(x=200,y=150)
    def add():
        n1 = int(e1.get())
        n2 = int(e2.get())
        n3 = n1+n2
        e3.delete(0,tkinter.END)
        e3.insert(0,str(n3))
    def sub():
        n1 = int(e1.get())
        n2 = int(e2.get())
        n3 = n1-n2
        e3.delete(0,tkinter.END)
        e3.insert(0,str(n3))
    def mul():
        n1 = int(e1.get())
        n2 = int(e2.get())
        n3 = n1*n2
        e3.delete(0,tkinter.END)
        e3.insert(0,str(n3))
    def div():
        n1 = int(e1.get())
        n2 = int(e2.get())
        n3 = n1/n2
        e3.delete(0,tkinter.END)
        e3.insert(0,str(n3))
    b1 = tkinter.Button(window,text="Add",width=10,command=add)
    b2 = tkinter.Button(window,text="Sub",width=10,command=sub)
    b3 = tkinter.Button(window,text="Mul",width=10,command=mul)
    b4 = tkinter.Button(window,text="Div",width=10,command=div)
    l1.grid(row=0,column=0)
    l2.grid(row=1,column=0)
    l3.grid(row=2,column=0)
    e1.grid(row=0,column=1)
    e2.grid(row=1,column=1)
    e3.grid(row=2,column=1)
    b1.grid(row=4,column=0)
    b2.grid(row=4,column=1)
    b3.grid(row=5,column=0)
    b4.grid(row=5,column=1)


    
  
        
                       

   
main()
