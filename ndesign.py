from tkinter import * #TKINTER IS IMPORTED
from PIL import Image, ImageTk#pillow library
from design import BMS
class ndesign:
    def __init__(self, root) :
       
        self.root=root
        self.root.geometry("1450x800+0+0")
        self.root.title("BUSINESS MANAGEMENT SYSTEM")
        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
        self.root.config(bg="#FFCB5D")
        self.bgtitle=ImageTk.PhotoImage(file="vectors/temp.png")
        bgtitle=Label(self.root,image=self.bgtitle,height=700,width=4000,compound=LEFT ,font=("algeria",40,"bold"),bg="#FFCB5D",fg="#701057",anchor="w",padx=1).place(x=0,y=-80,relwidth=10,height=900)
        StartButton=Button(self.root,text="HOME",command=self.design,font=("times new roman",15,"bold"),bg="#A548FF",cursor="hand2").place(x=600,y=600,height=60,width=200)

    def design(self):
        self.new_win=Toplevel(self.root)
        
        self.new_obj=BMS(self.new_win)
if __name__=="__main__":
    root=Tk()
    obj=ndesign(root)
    root.mainloop()
