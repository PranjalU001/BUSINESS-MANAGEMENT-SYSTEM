from tkinter import *
from tkinter import ttk, messagebox
import sqlite3 as sq
from PIL import Image, ImageTk#pillow library
class EmployeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1450x800+0+0")
        self.root.title("BUSINESS MANAGEMENT SYSTEM - Employee")
        self.root.config(bg="#FFCB5D")
        self.root.focus_force()
        self.bgImg=ImageTk.PhotoImage(file="vectors/forest.png")
        title=Label(self.root,image=self.bgImg,height=4000,width=3000,compound=LEFT ,font=("algeria",40,"bold"),bg="#FFCB5D",fg="#701057",anchor="w",padx=10).place(x=-20,y=0,relwidth=1,height=500)
        

        self.SearchBy = StringVar()
        self.SearchText = StringVar()

        self.employeeName = StringVar()
        self.employeeAddress = StringVar()
        self.employeeContact = StringVar()
        self.employeeEmail = StringVar()
        self.employeeGender = StringVar()
        self.employeeJoinDate = StringVar()
        self.employeePassword = StringVar()
        self.employeeUserType= StringVar()
        menu_lbl =Label(self.root, bg="#6422B8",  justify=CENTER)
        menu_lbl.place(x=290,y=0,height=500,width=800)
        cmd_search = ttk.Combobox( self.root,textvariable=self.SearchBy, values=("SELECT", "NAME", "EMAIL", "CONTACT"), font="calibri", state="readonly", justify=CENTER)
        cmd_search.place(x=300, y=20, width=200,height=25)
        cmd_search.current(0)
       
        TextSearch = Entry( self.root,textvariable=self.SearchText, font=("Calibiri", 15, "bold"), bg="#D1ADF4")
        TextSearch.place(x=550, y=20, width=300, height=25)
        searchbtn=Button(self.root,text="Search", cursor="hand2", command=self.search_employee, font=("calibiri", 15), bg="#FFCB5D")
        searchbtn.place(x=880, y=20, width=200, height=30)
        #employee lable

        lbl_employeeName = Label(self.root, text="Employee Name", font=("calibiri", 12, "bold"), bg="#6422B8", fg="white", justify=CENTER)
        lbl_employeeName.place(x=300, y=100, width=150, height=30)
        TextBox_employeeName = Entry(self.root, textvariable=self.employeeName, font=("calibiri", 12, "bold"), bg="#D1ADF4", fg="black", justify=CENTER)
        TextBox_employeeName.place(x=480, y=100, width=150, height=30)

        lbl_employeeAddress = Label(self.root, text="Employee Address", font=("calibiri", 12, "bold"), bg="#6422B8", fg="white", justify=CENTER)
        lbl_employeeAddress.place(x=300, y=160, width=150, height=30)
        TextBox_employeeAddress = Entry(self.root, textvariable=self.employeeAddress, font=("calibiri", 12, "bold"), bg="#D1ADF4", fg="black", justify=CENTER)
        TextBox_employeeAddress.place(x=480, y=160, width=150, height=30)

        lbl_employeeContact = Label(self.root, text="Employee Contact", font=("calibiri", 12, "bold"), bg="#6422B8", fg="white", justify=CENTER)
        lbl_employeeContact.place(x=300, y=220, width=150, height=30)
        TextBox_employeeContact = Entry(self.root, textvariable=self.employeeContact, font=("calibiri", 12, "bold"), bg="#D1ADF4", fg="black", justify=CENTER)
        TextBox_employeeContact.place(x=480, y=220, width=150, height=30)

        lbl_employeeEmail = Label(self.root, text="Employee Email", font=("calibiri", 12, "bold"), bg="#6422B8", fg="white", justify=CENTER)
        lbl_employeeEmail.place(x=300, y=280, width=150, height=30)
        TextBox_employeeEmail = Entry(self.root, textvariable=self.employeeEmail, font=("calibiri", 12, "bold"), bg="#D1ADF4", fg="black", justify=CENTER)
        TextBox_employeeEmail.place(x=480, y=280, width=150, height=30)

        lbl_employeeGender = Label(self.root, text="Employee Gender", font=("calibiri", 12, "bold"), bg="#6422B8", fg="white", justify=CENTER)
        lbl_employeeGender.place(x=700, y=100, width=150, height=30)
        TextBox_employeeGender = Entry(self.root, textvariable=self.employeeGender, font=("calibiri", 12, "bold"), bg="#D1ADF4", fg="black", justify=CENTER)
        TextBox_employeeGender.place(x=880, y=100, width=150, height=30)

        lbl_employeeJoinDate = Label(self.root, text="Date of Joining", font=("calibiri", 12, "bold"), bg="#6422B8", fg="white", justify=CENTER)
        lbl_employeeJoinDate.place(x=700, y=160, width=150, height=30)
        TextBox_employeeJoinDate = Entry(self.root, textvariable=self.employeeJoinDate, font=("calibiri", 12, "bold"), bg="#D1ADF4", fg="black", justify=CENTER)
        TextBox_employeeJoinDate.place(x=880, y=160, width=150, height=30)

        lbl_employeePassword = Label(self.root, text="Employee Id", font=("calibiri", 12, "bold"), bg="#6422B8", fg="white", justify=CENTER)
        lbl_employeePassword.place(x=700, y=220, width=150, height=30)
        TextBox_employeePassword = Entry(self.root, textvariable=self.employeePassword, font=("calibiri", 10, "bold"), bg="#D1ADF4", fg="black", justify=CENTER)
        TextBox_employeePassword.place(x=880, y=220, width=150, height=30)

        lbl_employeeType = Label(self.root, text="Employee Type", font=("calibiri", 12, "bold"), bg="#6422B8", fg="white", justify=CENTER)
        lbl_employeeType.place(x=700, y=280, width=150, height=30)
        TextBox_employeeType = Entry(self.root, textvariable=self.employeeUserType, font=("calibiri", 10, "bold"), bg="#D1ADF4", fg="black", justify=CENTER)
        TextBox_employeeType.place(x=880, y=280, width=150, height=30)
      

        SaveButton = Button(self.root, text="Save", cursor="hand2", command=self.add_employee, font=("calibiri", 15), bg="#701057", fg="white")
        SaveButton.place(x=350, y=350, width=200, height=50)
        updateButton=Button(self.root,text="Update",cursor="hand2", command=self.update_employee,font=("calibiri",15),bg="#701057",fg="white")
        updateButton.place(x=600,y=350,width=200,height=50)
        DeleteButton=Button(self.root,text="Delete",cursor="hand2", command=self.delete_employee,font=("calibiri",15),bg="#701057",fg="white")
        DeleteButton.place(x=850,y=350,width=200,height=50)

        employeeFrame = Frame(self.root, bd=3, relief=RIDGE, bg="#A548FF")
        employeeFrame.place(x=0, y=500, relwidth=1, height=205)

        scrollbarV = Scrollbar(employeeFrame, orient=VERTICAL)
        scrollbarH = Scrollbar(employeeFrame, orient=HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(employeeFrame, columns=("Name", "Email", "Address", "Contact", "Gender", "JoinDate", "Password", "Type"), xscrollcommand=scrollbarH.set, yscrollcommand=scrollbarV.set)

        scrollbarH.pack(side=BOTTOM, fill=X)
        scrollbarV.pack(side=RIGHT, fill=Y)
        scrollbarH.config(command=self.EmployeeTable.xview)
        scrollbarV.config(command=self.EmployeeTable.yview)

        self.EmployeeTable.heading("Name", text="Name")
        self.EmployeeTable.heading("Email", text="Email")
        self.EmployeeTable.heading("Address", text="Address")
        self.EmployeeTable.heading("Contact", text="Contact")
        self.EmployeeTable.heading("Gender", text="Gender")
        self.EmployeeTable.heading("JoinDate", text="JoinDate")
        self.EmployeeTable.heading("Password", text="Password")
        self.EmployeeTable.heading("Type", text="Type")

        self.EmployeeTable["show"] = "headings"
        self.EmployeeTable.pack(fill=BOTH, expand=1)

        self.EmployeeTable.column("Name", width=90)
        self.EmployeeTable.column("Email", width=90)
        self.EmployeeTable.column("Address", width=90)
        self.EmployeeTable.column("Contact", width=90)
        self.EmployeeTable.column("Gender", width=90)
        self.EmployeeTable.column("JoinDate", width=90)
        self.EmployeeTable.column("Password", width=90)
        self.EmployeeTable.column("Type", width=90)

    def add_employee(self):
        
            # Connect to the database
        con = sq.connect(database='bms_app.db')
        cur = con.cursor()
        try:
            if self.employeeName.get()=="":
                messagebox.showerror("Error","employee name must be required",parent= self.root)
            # Insert employee details into the database
            else:
                cur.execute("INSERT INTO employee (Name, Email, Address, Contact ,Gender, JoinDate, Password, UserType) VALUES (?,?,?,?,?,?,?,?)",
                        (self.employeeName.get(), self.employeeEmail.get(), self.employeeAddress.get(), self.employeeContact.get(),self.employeeGender.get(), self.employeeJoinDate.get(),self.employeePassword.get(), self.employeeUserType.get()))
                con.commit()
 
                messagebox.showinfo("Success", "Employee added successfully")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    

    def search_employee(self):
        try:
            con = sq.connect(database='bms_app.db')
            cur = con.cursor()

            search_by = self.SearchBy.get()
            search_text = self.SearchText.get()

            if search_by == "SELECT" or not search_text:
                messagebox.showinfo("Info", "Please select a valid search criteria and provide a search value.")
            else:
                query = f"SELECT * FROM employee WHERE {search_by.lower()} LIKE ?"
                cur.execute(query, ('%' + search_text + '%',))
                rows = cur.fetchall()
                print(rows)

                for row in self.EmployeeTable.get_children():
                    self.EmployeeTable.delete(row)

                for row in rows:
                    self.EmployeeTable.insert("", "end", values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error during search: {str(ex)}", parent=self.root)

    def update_employee(self):
        try:
            con = sq.connect(database='bms_app.db')
            cur = con.cursor()
            print("hello")

            selected_item = self.EmployeeTable.selection()

            if not selected_item:
                messagebox.showinfo("Info", "Please select an employee to update.")
                return

            values = self.EmployeeTable.item(selected_item)['values']
            print(values)

            if len(values) != 9:
                messagebox.showerror("Error", "Invalid data. Please select a valid employee.")
                return

            employee_id, current_name, current_address, current_contact, current_email, current_gender, current_join_date, current_password, current_type = values
            
            updated_name = self.employeeName.get()
            updated_email = self.employeeEmail.get()
            updated_address = self.employeeAddress.get()
            updated_contact = self.employeeContact.get()
            updated_gender = self.employeeGender.get()
            updated_join_date = self.employeeJoinDate.get()
            updated_password = self.employeePassword.get()
            updated_type = self.employeeUserType.get()
            print(employee_id)
            print(type(employee_id))

            cur.execute("UPDATE employee SET Name=?, Address=?, Contact=?, Email=?, Gender=?, JoinDate=?, Password=?, UserType=? WHERE employee_id=?", (
                updated_name, updated_email,updated_address, updated_contact, updated_gender, updated_join_date, updated_password, updated_type,employee_id
            ))
            con.commit()

            messagebox.showinfo("Success", "Employee information updated successfully.")

            self.search_employee()

        except Exception as ex:
            messagebox.showerror("Error", f"Error during update: {str(ex)}", parent=self.root)

    def delete_employee(self):
        try:
            con = sq.connect(database='bms_app.db')
            cur = con.cursor()

            selected_item = self.EmployeeTable.selection()

            if not selected_item:
                messagebox.showinfo("Info", "Please select an employee to delete.")
                return

            values = self.EmployeeTable.item(selected_item)['values']

            employee_id = values[0]

            confirm = messagebox.askyesno("Confirmation", "Are you sure you want to delete this employee?")

            if confirm:
                cur.execute("DELETE FROM employee WHERE employee_id=?", (employee_id,))
                con.commit()

                messagebox.showinfo("Success", "Employee deleted successfully.")

                self.search_employee()

        except Exception as ex:
            messagebox.showerror("Error", f"Error during deletion: {str(ex)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = EmployeeClass(root)
    root.mainloop()
