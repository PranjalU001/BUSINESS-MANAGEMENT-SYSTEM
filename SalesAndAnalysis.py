import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SalesAnalysis:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x700+220+130")
        self.root.title("BUSINESS MANAGEMENT SYSTEM - Sales Analysis")
        self.root.config(bg="#FFCB5D")
        self.root.focus_force()

        self.sales_frame = ttk.Frame(self.root)
        self.sales_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        self.sales_label = ttk.Label(self.sales_frame, text="Sales Details", font=("Arial", 16, "bold"))
        self.sales_label.pack(pady=10)

        self.sales_tree = ttk.Treeview(self.sales_frame, columns=("Date", "Revenue"), show="headings")
        self.sales_tree.heading("Date", text="Sale Date")
        self.sales_tree.heading("Revenue", text="Total Revenue")
        self.sales_tree.pack(fill=tk.BOTH, expand=True)

        self.fetch_sales_data()
        self.display_sales_data()

        ttk.Label(self.root, text="Date:", font=("calibiri", 12), background="#FFCB5D").place(x=80, y=590, width=120, height=23)
        self.date_entry = ttk.Entry(self.root)
        self.date_entry.place(x=220, y=590, width=120, height=23)

        ttk.Label(self.root, text="Revenue:", font=("calibiri", 12), background="#FFCB5D").place(x=80, y=620, width=120, height=23)
        self.revenue_entry = ttk.Entry(self.root)
        self.revenue_entry.place(x=220, y=620, width=120, height=23)

        self.save_button = Button(self.root, text="Save", cursor="hand2", command=self.save_sale, font=("calibiri", 12), bg="#701057", fg="white")
        self.save_button.place(x=800, y=580, width=120, height=30)

        self.delete_button = Button(self.root, text="Delete", cursor="hand2", command=self.delete_sale, font=("calibiri", 12), bg="#701057", fg="white")
        self.delete_button.place(x=950, y=580, width=120, height=30)

        self.generate_button = Button(self.root, text="Generate Analysis", cursor="hand2", command=self.generate_analysis, font=("calibiri", 12), bg="#701057", fg="white")
        self.generate_button.place(x=820, y=640, width=250, height=30)

    def fetch_sales_data(self):
        try:
            conn = sqlite3.connect('bms_app.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM sale")
            self.sales_data = cursor.fetchall()
            conn.close()
        except sqlite3.Error as e:
            print("Error fetching sales data:", e)
            self.sales_data = []

    def display_sales_data(self):
        for row in self.sales_data:
            self.sales_tree.insert("", "end", values=row)

    def save_sale(self):
        try:
            date = self.date_entry.get()
            revenue = float(self.revenue_entry.get())

            conn = sqlite3.connect('bms_app.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO sale (date, revenue) VALUES (?, ?)", (date, revenue))
            conn.commit()
            conn.close()

            self.fetch_sales_data()
            self.sales_tree.delete(*self.sales_tree.get_children())
            self.display_sales_data()

            messagebox.showinfo("Success", "Sale record saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Error saving sale record: {e}")

    def delete_sale(self):
        selected_item = self.sales_tree.selection()
        if not selected_item:
            messagebox.showinfo("Info", "Please select a sale record to delete.")
            return

        confirmed = messagebox.askyesno("Confirm", "Are you sure you want to delete this sale record?")
        if not confirmed:
            return
        if confirmed:
            try:
                conn = sqlite3.connect('bms_app.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM sale WHERE rowid=?", (selected_item,))
                conn.commit()
                conn.close()

                self.fetch_sales_data()
                self.sales_tree.delete(*self.sales_tree.get_children())
                self.display_sales_data()

                messagebox.showinfo("Success", "Sale record deleted successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Error deleting sale record: {e}")

    def generate_analysis(self):
        dates = [row[1] for row in self.sales_data]
        revenues = [row[2] for row in self.sales_data]

        plt.figure(figsize=(8, 4))
        plt.plot(dates, revenues, marker='o', color='b')
        plt.title('Sales Analysis')
        plt.xlabel('Sale Date')
        plt.ylabel('Total Revenue')
        plt.xticks(rotation=45)
        plt.tight_layout()

        self.figure_canvas = FigureCanvasTkAgg(plt.gcf(), master=self.root)
        self.figure_canvas.draw()
        self.figure_canvas.get_tk_widget().place(x=80, y=50, width=800, height=500)

if __name__ == "__main__":
    root = tk.Tk()
    app = SalesAnalysis(root)
    root.mainloop()
