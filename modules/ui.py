import customtkinter as ctk
import webbrowser
from PIL import Image
from modules.file_utils import select_csv, select_directory
from modules.qr_generator import generate_qr_codes
import os
import sys

# Function to get the logo path
def get_logo_path():
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, "assets", "logo.png")
    else:
        return os.path.join(os.path.dirname(__file__), "assets", "logo.png")

def open_link():
    webbrowser.open("https://jyuviolegrace.t.me")

def create_ui():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("QRSV Gen")
    app.geometry("800x600")
    app.minsize(600, 500)

    # Add a custom logo
    logo_image = Image.open(get_logo_path())
    logo = ctk.CTkImage(light_image=logo_image, size=(150, 150))
    logo_label = ctk.CTkLabel(app, image=logo, text="")
    logo_label.pack(pady=(20, 5))

    # Application title
    title_label = ctk.CTkLabel(app, text="QRSV Gen", font=("Helvetica", 24, "bold"))
    title_label.pack(pady=5)

    # Branding
    branding_label = ctk.CTkLabel(app, text="Made by 25thNight", font=("Helvetica", 14), text_color="blue", cursor="hand2")
    branding_label.pack(pady=5)
    branding_label.bind("<Button-1>", lambda e: open_link())

    # Main Frame for Inputs
    main_frame = ctk.CTkFrame(app)
    main_frame.pack(pady=10, fill="both", expand=True, padx=20)

    main_frame.grid_columnconfigure(1, weight=1)
    main_frame.grid_rowconfigure(3, weight=1)

    # CSV file selection
    csv_var = ctk.StringVar()
    ctk.CTkLabel(main_frame, text="CSV File:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    ctk.CTkEntry(main_frame, textvariable=csv_var, state="readonly").grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    ctk.CTkButton(main_frame, text="Browse", command=lambda: select_csv(csv_var, column_dropdown_menu, column_dropdown)).grid(row=0, column=2, padx=10, pady=10, sticky="ew")

    # Output directory selection
    directory_var = ctk.StringVar()
    ctk.CTkLabel(main_frame, text="Output Directory:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    ctk.CTkEntry(main_frame, textvariable=directory_var, state="readonly").grid(row=1, column=1, padx=10, pady=10, sticky="ew")
    ctk.CTkButton(main_frame, text="Browse", command=lambda: select_directory(directory_var)).grid(row=1, column=2, padx=10, pady=10, sticky="ew")

    # Column selection dropdown
    ctk.CTkLabel(main_frame, text="Select Column for QR Names:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
    column_dropdown = ctk.StringVar()
    column_dropdown_menu = ctk.CTkComboBox(main_frame, variable=column_dropdown, values=[])
    column_dropdown_menu.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    # Progress tracker
    progress_label = ctk.CTkLabel(app, text="Generated: 0/0", font=("Helvetica", 14), text_color="green")
    progress_label.pack(pady=10)

    # Generate button
    ctk.CTkButton(app, text="Generate QR Codes", command=lambda: generate_qr_codes(csv_var.get(), directory_var.get(), column_dropdown.get(), progress_label)).pack(pady=10)

    app.mainloop()
