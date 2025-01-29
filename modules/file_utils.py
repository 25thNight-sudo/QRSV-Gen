import csv
from tkinter import filedialog, messagebox

def select_csv(csv_var, column_dropdown_menu, column_dropdown):
    csv_path = filedialog.askopenfilename(title="Select CSV File", filetypes=[("CSV Files", "*.csv")])
    csv_var.set(csv_path)
    if csv_path:
        populate_columns(csv_path, column_dropdown_menu, column_dropdown)

def populate_columns(csv_file, column_dropdown_menu, column_dropdown):
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            columns = reader.fieldnames
            column_dropdown.set("")
            column_dropdown_menu.configure(values=columns if columns else [])
            if not columns:
                raise ValueError("No columns found in the CSV file.")
    except Exception as e:
        column_dropdown_menu.configure(values=[])
        messagebox.showerror("Error", f"Could not read CSV file: {str(e)}")

def select_directory(directory_var):
    directory_path = filedialog.askdirectory(title="Select Output Directory")
    directory_var.set(directory_path)
