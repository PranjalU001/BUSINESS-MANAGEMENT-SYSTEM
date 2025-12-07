# supplier.py
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3 as sq
from PIL import Image, ImageTk#pillow library

class SupplierClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1450x800+0+0")
        self.root.title("BUSINESS MANAGEMENT SYSTEM - Supplier")
        self.root.config(bg="#FFCB5D")
        self.root.focus_force()
        self.bgImg=ImageTk.PhotoImage(file="vectors/container.png")
        title=Label(self.root,image=self.bgImg,height=4000,width=3000,compound=LEFT ,font=("algeria",40,"bold"),bg="#FFCB5D",fg="#701057",anchor="w",padx=10).place(x=-20,y=0,relwidth=1,height=500)
        
        self.SearchBy = StringVar()
        self.SearchText = StringVar()

        self.supplierName = StringVar()
        self.supplierAddress = StringVar()
        self.supplierContact = StringVar()
        self.supplierEmail = StringVar()
        menu_lbl =Label(self.root, bg="#6422B8",  justify=CENTER)
        menu_lbl.place(x=290,y=0,height=500,width=800)

        cmd_search = ttk.Combobox( self.root,textvariable=self.SearchBy, values=("SELECT", "NAME", "EMAIL", "CONTACT"), font="calibri", state="readonly", justify=CENTER)
        cmd_search.place(x=300, y=20, width=200,height=25)
        cmd_search.current(0)

        TextSearch = Entry( self.root,textvariable=self.SearchText,font=("Calibiri", 15, "bold"), bg="#D1ADF4").place(x=550, y=20, width=350, height=23)
        Searchbtn = Button(self.root,text="Search", cursor="hand2", command= self.search_supplier,font=("calibiri", 15), bg="#FFCB5D").place(x=950, y=20, width=120, height=23)
        
        # --- Supplier Details Entry Widgets ---
        lbl_supplierName = Label(self.root, text="Supplier Name", font=("calibiri", 12, "bold"), bg="#6422B8", fg="white", justify=CENTER).place(x=350, y=100, width=150, height=30)
        TextBox_supplierName = Entry(self.root, textvariable=self.supplierName, font=("calibiri", 12, "bold"), bg="#D1ADF4", fg="black", justify=CENTER).place(x=600, y=100, width=150, height=30)

        lbl_supplierAddress = Label(self.root, text="Supplier Address", font=("calibiri", 12, "bold"), bg="#6422B8", fg="white", justify=CENTER).place(x=350, y=160, width=150, height=30)
        TextBox_supplierAddress = Entry(self.root, textvariable=self.supplierAddress, font=("calibiri", 12, "bold"), bg="#D1ADF4", fg="black", justify=CENTER).place(x=600, y=160, width=150, height=30)

        lbl_supplierContact = Label(self.root, text="Supplier Contact", font=("calibiri", 12, "bold"), bg="#6422B8", fg="white", justify=CENTER).place(x=350, y=220, width=150, height=30)
        TextBox_supplierContact = Entry(self.root, textvariable=self.supplierContact, font=("calibiri", 12, "bold"), bg="#D1ADF4", fg="black", justify=CENTER).place(x=600, y=220, width=150, height=30)
        lbl_supplierEmail = Label(self.root, text="Supplier Email", font=("calibiri", 12, "bold"), bg="#6422B8", fg="white", justify=CENTER).place(x=350, y=280, width=150, height=30)
        TextBox_supplierEmail = Entry(self.root, textvariable=self.supplierEmail, font=("calibiri", 12, "bold"), bg="#D1ADF4", fg="black", justify=CENTER).place(x=600, y=280, width=150, height=30)

        # ... (similar structure for other widgets)

        SaveButton = Button(self.root, text="Save", cursor="hand2", command=self.add_supplier, font=("calibiri", 15), bg="#701057", fg="white").place(x=300, y=350, width=200, height=50)
        updateButton=Button(self.root,text="Update",cursor="hand2", command=self.update_supplier,font=("calibiri",15),bg="#701057",fg="white").place(x=550,y=350,width=200,height=50)
        DeleteButton = Button(self.root, text="Delete", cursor="hand2", command=self.delete_supplier, font=("calibiri", 15), bg="#701057", fg="white").place(x=800, y=350, width=200, height=50)
        # This frame should be separated from the SearchFrame above
        supplierFrame = Frame(self.root, bd=3, relief=RIDGE, bg="#A548FF")
        supplierFrame.place(x=0, y=500, relwidth=1, height=205)

        scrollbarV = Scrollbar(supplierFrame, orient=VERTICAL)
        scrollbarH = Scrollbar(supplierFrame, orient=HORIZONTAL)

        self.SupplierTable = ttk.Treeview(supplierFrame, columns=("Name", "Email", "Address", "Contact"), xscrollcommand=scrollbarH.set, yscrollcommand=scrollbarV.set)

        scrollbarH.pack(side=BOTTOM, fill=X)
        scrollbarV.pack(side=RIGHT, fill=Y)
        scrollbarH.config(command=self.SupplierTable.xview)
        scrollbarV.config(command=self.SupplierTable.yview)

        self.SupplierTable.heading("Name", text="Name")
        self.SupplierTable.heading("Email", text="Email")
        self.SupplierTable.heading("Address", text="Address")
        self.SupplierTable.heading("Contact", text="Contact")

        self.SupplierTable["show"] = "headings"
        self.SupplierTable.pack(fill=BOTH, expand=1)

        self.SupplierTable.column("Name", width=90)
        self.SupplierTable.column("Email", width=90)
        self.SupplierTable.column("Address", width=90)
        self.SupplierTable.column("Contact", width=90)

    def add_supplier(self):
        try:
            con = sq.connect(database='bms_app.db')  # Connect to the new database
            cur = con.cursor()
            if self.supplierName.get()=="":
                messagebox.showerror("Error","Supplier name must be required",parent= self.root)
            else:
                cur.execute("INSERT INTO supplier (Name,Email, Address, Contact) VALUES (?, ?,?, ?)",
                            (self.supplierName.get(),self.supplierEmail.get(),self.supplierAddress.get(), self.supplierContact.get()))
                con.commit()

                messagebox.showinfo("Success", "Supplier added successfully")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    def search_supplier(self):
        try:
            con = sq.connect(database='bms_app.db')
            cur = con.cursor()
            
            search_by = self.SearchBy.get()
            search_text = self.SearchText.get()
            
            if search_by == "SELECT" or not search_text:
                messagebox.showinfo("Info", "Please select a valid search criteria and provide a search value.")
            else:
                query = f"SELECT * FROM supplier WHERE {search_by.lower()} LIKE ?"
                cur.execute(query, ('%' + search_text + '%',))
                rows = cur.fetchall()

                # Clear previous entries in the Treeview
                for row in self.SupplierTable.get_children():
                    self.SupplierTable.delete(row)

                # Insert new data into Treeview
                for row in rows:
                    self.SupplierTable.insert("", "end", values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error during search: {str(ex)}", parent=self.root)
    
    def update_supplier(self):
        try:
            con = sq.connect(database='bms_app.db')
            cur = con.cursor()

            # Get the currently selected item from the Treeview
            selected_item = self.SupplierTable.selection()

            if not selected_item:
                messagebox.showinfo("Info", "Please select a supplier to update.")
                return

            # Get the values from the selected item
            values = self.SupplierTable.item(selected_item)['values']

            # Assuming the columns are in the order: supplier_id, Name, Address, Contact, Email
            supplier_id, current_name, current_address, current_contact, current_email = values

            # Get the updated information from entry widgets
            updated_name = self.supplierName.get()
            updated_address = self.supplierAddress.get()
            updated_contact = self.supplierContact.get()
            updated_email = self.supplierEmail.get()

            # Update the database with the new information
            cur.execute("UPDATE supplier SET Name=?, Address=?, Contact=?, Email=? WHERE supplier_id=?", (
                updated_name, updated_address, updated_contact, updated_email, supplier_id
            ))
            con.commit()

            messagebox.showinfo("Success", "Supplier information updated successfully.")

            # Refresh the Treeview with updated data
            self.search_supplier()

        except Exception as ex:
            messagebox.showerror("Error", f"Error during update: {str(ex)}", parent=self.root)


    def delete_supplier(self):
        try:
            con = sq.connect(database='bms_app.db')
            cur = con.cursor()

            # Get the currently selected item from the Treeview
            selected_item = self.SupplierTable.selection()

            if not selected_item:
                messagebox.showinfo("Info", "Please select a supplier to delete.")
                return

            # Get the values from the selected item
            values = self.SupplierTable.item(selected_item)['values']

            # Assuming the columns are in the order: supplier_id, Name, Address, Contact, Email
            supplier_id = values[0]

            # Confirm deletion
            confirm = messagebox.askyesno("Confirmation", "Are you sure you want to delete this supplier?")

            if confirm:
                # Delete the supplier from the database
                cur.execute("DELETE FROM supplier WHERE supplier_id=?", (supplier_id,))
                con.commit()

                messagebox.showinfo("Success", "Supplier deleted successfully.")

                # Refresh the Treeview with updated data
                self.search_supplier()

        except Exception as ex:
            messagebox.showerror("Error", f"Error during deletion: {str(ex)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = SupplierClass(root)
    root.mainloop()
