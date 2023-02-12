from tkinter import*
w=Tk()
def send():
    send="You => "+e.get()
    txt.insert(END, "\n"+send)
    if(e.get()=="hello"):
        txt.insert(END,"\n"+"Bot=>Hi")
    elif(e.get()=="hi"):
         txt.insert(END,"\n"+"Bot=>Hello")
    elif(e.get()=="how are you"):
         txt.insert(END,"\n"+"Bot=> fine and you")
    elif(e.get()=="fine"):
         txt.insert(END,"\n"+"Bot=> Nice to hear")  
    elif(e.get()=="which subject you make project"):
         txt.insert(END,"\n"+"Bot=> Robitics and automation")  
    elif(e.get()=="what is the Course code"):
         txt.insert(END,"\n"+"Bot=> ECE218")  
     
    elif(e.get()=="Name of the teacher"):
         txt.insert(END,"\n"+"Bot=>Nitin Kumar sir ")  
    elif(e.get()=="University Name"):
         txt.insert(END,"\n"+"Bot=> Lovely Professional University")  
    elif(e.get()=="where it is located"):
         txt.insert(END,"\n"+"Bot=> Punjab")  
     elif(e.get()=="Name of the student"):
         txt.insert(END,"\n"+"Bot=>  Sahil kumar")  
     elif(e.get()=="Registration Number"):
         txt.insert(END,"\n"+"Bot=>  12008227")   
     elif(e.get()=="Name of the course he is doing"):
         txt.insert(END,"\n"+"Bot=>  Electronics and Electrical Engineering")          

    
     else:
         txt.insert(END,"\n"+"Bot=>sorry I didnt get")             
    e.delete(0,END)
txt=Text(w)
txt.grid(row=0,column=0,columnspan=2)
e=Entry(w,width=100)  
send=Button(w,text="Send",command=send).grid(row=1,column=1) 
e.grid(row=1,column=0)
w.title("CHATBOT")

w.mainloop()






