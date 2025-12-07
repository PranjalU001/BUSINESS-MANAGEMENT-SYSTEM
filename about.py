from tkinter import * #TKINTER IS IMPORTED
from PIL import Image, ImageTk#pillow library

class About:
    def __init__(self, root) :
       
        self.root=root
        self.root.geometry("1450x800+0+0")
        self.root.title("BUSINESS MANAGEMENT SYSTEM")
        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
        self.root.config(bg="#FFCB5D")
        self.bgtitle=ImageTk.PhotoImage(file="vectors/aboutus.png")
        bgtitle=Label(self.root,image=self.bgtitle,height=700,width=4000,compound=LEFT ,font=("algeria",40,"bold"),bg="#FFCB5D",fg="#701057",anchor="w",padx=1).place(x=0,y=5,relwidth=10,height=700)
        
   
if __name__=="__main__":
    root=Tk()
    obj=About(root)
    root.mainloop()
