from tkinter import *
from tkinter import ttk, messagebox
import sqlite3 as sq
from PIL import Image, ImageTk#pillow library
class InventoryClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1450x800+0+0")
        self.root.title("bBusiness Management System - Inventory")
        self.root.config(bg="#FFCB5D")
        self.root.focus_force()
        self.bgImg=ImageTk.PhotoImage(file="vectors/ware.png")
        title=Label(self.root,image=self.bgImg,height=4000,width=3000,compound=LEFT ,font=("algeria",40,"bold"),bg="#FFCB5D",fg="#701057",anchor="w",padx=10).place(x=-20,y=0,relwidth=1,height=500)
        
        self.SearchBy = StringVar()
        self.SearchText = StringVar()

        self.productBrand = StringVar()
        self.productType = StringVar()
        self.productPrice = StringVar()
        self.productBatchCode = StringVar()
        self.productQuantity = StringVar()
        menu_lbl =Label(self.root, bg="#6422B8",  justify=CENTER)
        menu_lbl.place(x=290,y=0,height=500,width=800)

        lbl_productBrand = Label(self.root, text="Product Brand", font=("calibiri", 12, "bold"), bg="#6422B8", fg="white", justify=CENTER)
        lbl_productBrand.place(x=300, y=20, width=150, height=30)
        TextBox_productBrand = Entry(self.root, textvariable=self.productBrand, font=("calibiri", 12, "bold"), bg="#D1ADF4", fg="black", justify=CENTER)
        TextBox_productBrand.place(x=500, y=20, width=150, height=30)

        lbl_productType = Label(self.root, text="Product Type", font=("calibiri", 12, "bold"), bg="#6422B8", fg="white", justify=CENTER)
        lbl_productType.place(x=300, y=100, width=150, height=30)
        TextBox_productType = Entry(self.root, textvariable=self.productType, font=("calibiri", 12, "bold"), bg="#D1ADF4", fg="black", justify=CENTER)
        TextBox_productType.place(x=500, y=100, width=150, height=30)

        lbl_productPrice = Label(self.root, text="Product Price", font=("calibiri", 12, "bold"), bg="#6422B8", fg="white", justify=CENTER)
        lbl_productPrice.place(x=300, y=180, width=150, height=30)
        TextBox_productPrice = Entry(self.root, textvariable=self.productPrice, font=("calibiri", 12, "bold"), bg="#D1ADF4", fg="black", justify=CENTER)
        TextBox_productPrice.place(x=500, y=180, width=150, height=30)

        lbl_productBatchCode = Label(self.root, text="Product Batch Code", font=("calibiri", 12, "bold"), bg="#6422B8", fg="white", justify=CENTER)
        lbl_productBatchCode.place(x=650, y=20, width=180, height=30)
        TextBox_productBatchCode = Entry(self.root, textvariable=self.productBatchCode, font=("calibiri", 12, "bold"), bg="#D1ADF4", fg="black", justify=CENTER)
        TextBox_productBatchCode.place(x=850, y=20, width=150, height=30)

        lbl_productQuantity = Label(self.root, text="Product Quantity", font=("calibiri", 12, "bold"), bg="#6422B8", fg="white", justify=CENTER)
        lbl_productQuantity.place(x=650, y=100, width=150, height=30)
        TextBox_productQuantity = Entry(self.root, textvariable=self.productQuantity, font=("calibiri", 12, "bold"), bg="#D1ADF4", fg="black", justify=CENTER)
        TextBox_productQuantity.place(x=850, y=100, width=150, height=30)

        SaveButton = Button(self.root, text="Save", cursor="hand2", command=self.add_product, font=("calibiri", 15), bg="#701057", fg="white")
        SaveButton.place(x=300, y=300, width=200, height=50)
        UpdateButton = Button(self.root, text="Update", cursor="hand2", command=self.update_product, font=("calibiri", 15), bg="#701057", fg="white")
        UpdateButton.place(x=550, y=300, width=200, height=50)
        DeleteButton = Button(self.root, text="Delete", cursor="hand2", command=self.delete_product, font=("calibiri", 15), bg="#701057", fg="white")
        DeleteButton.place(x=800, y=300, width=200, height=50)

        self.SearchText = StringVar()
        cmd_search = ttk.Combobox(self.root, textvariable=self.SearchText, values=("SELECT","Product Brand", "Product Type", "Product Batch Code"), font="calibri", state="readonly", justify=CENTER)
        cmd_search.place(x=300, y=400, width=200)
        cmd_search.current(0)

        TextSearch = Entry(self.root, font=("Calibiri", 15, "bold"), bg="#D1ADF4")
        TextSearch.place(x=550, y=400, width=250, height=25)
        Button(self.root, text="Search", cursor="hand2", command=self.search_product, font=("calibiri", 15), bg="#FFCB5D").place(x=850, y=400, width=200, height=25)

        productFrame = Frame(self.root, bd=3, relief=RIDGE, bg="#A548FF")
        productFrame.place(x=0, y=500, relwidth=1, height=205)

        scrollbarV = Scrollbar(productFrame, orient=VERTICAL)
        scrollbarH = Scrollbar(productFrame, orient=HORIZONTAL)

        self.ProductTable = ttk.Treeview(productFrame, columns=("Brand", "Type", "Price", "Batch Code", "Quantity"), xscrollcommand=scrollbarH.set, yscrollcommand=scrollbarV.set)

        scrollbarH.pack(side=BOTTOM, fill=X)
        scrollbarV.pack(side=RIGHT, fill=Y)
        scrollbarH.config(command=self.ProductTable.xview)
        scrollbarV.config(command=self.ProductTable.yview)

        self.ProductTable.heading("Brand", text="Brand")
        self.ProductTable.heading("Type", text="Type")
        self.ProductTable.heading("Price", text="Price")
        self.ProductTable.heading("Batch Code", text="Batch Code")
        self.ProductTable.heading("Quantity", text="Quantity")

        self.ProductTable["show"] = "headings"
        self.ProductTable.pack(fill=BOTH, expand=1)

        self.ProductTable.column("Brand", width=100)
        self.ProductTable.column("Type", width=100)
        self.ProductTable.column("Price", width=100)
        self.ProductTable.column("Batch Code", width=100)
        self.ProductTable.column("Quantity", width=100)

    def add_product(self):
        try:
            con = sq.connect(database='bms_app.db')
            cur = con.cursor()
            if self.productBatchCode.get()=="":
                messagebox.showerror("Error","Enter the batchcode of the product")
            else:

                cur.execute("INSERT INTO products (Brand, Type, Price, Batch_Code, Quantity) VALUES (?, ?, ?, ?, ?)",
                            (self.productBrand.get(), self.productType.get(), self.productPrice.get(), self.productBatchCode.get(), self.productQuantity.get()))
                con.commit()

                messagebox.showinfo("Success", "Product added successfully")
                self.show_all_products()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def search_product(self):
        try:
            con = sq.connect(database='bms_app.db')
            cur = con.cursor()

            search_by = self.SearchBy.get()
            search_text =self.SearchText.get()

            if search_by == "SELECT" or not search_text:
                messagebox.showinfo("Info", "Please select a valid search criteria and provide a search value.")
            else:
                query = f"SELECT * FROM products WHERE {search_by.lower()} LIKE ?"
                cur.execute(query, ('%' + search_by + '%',))
                rows = cur.fetchall()
                for row in self.ProductTable.get_children():
                    self.ProductTable.delete(row)
                for row in rows:
                    self.ProductTable.insert("", "end", values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error during search: {str(ex)}", parent=self.root)

    def update_product(self):
        try:
            con = sq.connect(database='bms_app.db')
            cur = con.cursor()

            selected_item = self.ProductTable.selection()

            if not selected_item:
                messagebox.showinfo("Info", "Please select a product to update.")
                return

            values = self.ProductTable.item(selected_item)['values']

            if len(values) != 5:
                messagebox.showerror("Error", "Invalid data. Please select a valid product.")
                return

            product_id, current_brand, current_type, current_price, current_batch_code, current_quantity = values

            updated_brand = self.productBrand.get()
            updated_type = self.productType.get()
            updated_price = self.productPrice.get()
            updated_batch_code = self.productBatchCode.get()
            updated_quantity = self.productQuantity.get()

            cur.execute("UPDATE products SET Brand=?, Type=?, Price=?, Batch_Code=?, Quantity=? WHERE id=?",
                        (updated_brand, updated_type, updated_price, updated_batch_code, updated_quantity, product_id))
            con.commit()

            messagebox.showinfo("Success", "Product information updated successfully.")
            self.show_all_products()

        except Exception as ex:
            messagebox.showerror("Error", f"Error during update: {str(ex)}", parent=self.root)

    def delete_product(self):
        try:
            con = sq.connect(database='bms_app.db')
            cur = con.cursor()

            selected_item = self.ProductTable.selection()

            if not selected_item:
                messagebox.showinfo("Info", "Please select a product to delete.")
                return

            values = self.ProductTable.item(selected_item)['values']

            product_id = values[0]

            confirm = messagebox.askyesno("Confirmation", "Are you sure you want to delete this product?")

            if confirm:
                cur.execute("DELETE FROM products WHERE id=?", (product_id,))
                con.commit()

                messagebox.showinfo("Success", "Product deleted successfully.")
                self.show_all_products()

        except Exception as ex:
            messagebox.showerror("Error", f"Error during deletion: {str(ex)}", parent=self.root)

    def show_all_products(self):
        try:
            con = sq.connect(database='bms_app.db')
            cur = con.cursor()

            cur.execute("SELECT * FROM products")
            rows = cur.fetchall()

            for row in rows:
                self.ProductTable.insert("", "end", values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error while fetching products: {str(ex)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = InventoryClass(root)
    root.mainloop()
