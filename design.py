'''THIS MODULE IS GUI OF BUSINESS MANGEMNT SYSTEM
WE ARE USING TKINTER  '''


from tkinter import * #TKINTER IS IMPORTED
from PIL import Image, ImageTk#pillow library
from employee import EmployeeClass
from supplier import SupplierClass
from inventory import InventoryClass
from SalesAndAnalysis import SalesAnalysis
from about import About
class BMS:
    def __init__(self, root) :
       
        self.root=root
        self.root.geometry("1450x800+0+0")
        # self.root.title("BUSINESS MANAGEMENT SYSTEM")
        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
        self.root.config(bg="#FFCB5D")


        #TITLE
        self.icon_title=ImageTk.PhotoImage(file="vectors/bms (2).png")
        title=Label(self.root,image=self.icon_title,height=4000,width=30000,compound=LEFT ,font=("algeria",40,"bold"),bg="#FFCB5D",fg="#701057",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=120)
        
        #---------Menu buttons-----------
        EmployeeButton=Button(self.root,text="Employee",command=self.employee,font=("times new roman",15,"bold"),bg="#A548FF",cursor="hand2").place(x=200,y=0,height=60,width=200)
        InventoryButton=Button(self.root,text="Inventory",command=self.inventory,font=("times new roman",15,"bold"),bg="#A548FF",cursor="hand2").place(x=400,y=0,height=60,width=200)
        SupplierButton=Button(self.root,text="Supplier",command=self.supplier,font=("times new roman",15,"bold"),bg="#A548FF",cursor="hand2").place(x=600,y=0,height=60,width=200)
        AnalysisButton=Button(self.root,text="Sales & Analysis",command =self.analysis,font=("times new roman",15,"bold"),bg="#A548FF",cursor="hand2").place(x=800,y=0,height=60,width=200)
        About=Button(self.root,text="About us",command =self.about,font=("times new roman",15,"bold"),bg="#A548FF",cursor="hand2").place(x=1000,y=0,height=60,width=200)
        
        #-------FOOTER------
        self.lbl_copyright=Label(self.root,text="\u00A9 2024 All Copyrights are encrypted by Business Mangement System ",height=6000,width=40000 ,font=("calibri",20),bg="#6422B8",fg="white")
        self.lbl_copyright.place(x=0,y=640,relwidth=1,height=70)
        self.bgImg=ImageTk.PhotoImage(file="vectors/temp.png")
        title=Label(self.root,image=self.bgImg,height=4000,width=3000,compound=LEFT ,font=("algeria",40,"bold"),bg="#FFCB5D",fg="#701057",anchor="w",padx=0).place(x=0,y=100,relwidth=1,height=550)
        
       
#-------------------------------------------------------------------------------------------
    def about(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=About(self.new_win)
    
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=EmployeeClass(self.new_win)
    
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=SupplierClass(self.new_win)
    def inventory(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=InventoryClass(self.new_win)
    def analysis(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=SalesAnalysis(self.new_win)
          



if __name__=="__main__":
    root=Tk()
    obj=BMS(root)
    root.mainloop()



