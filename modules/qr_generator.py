import os
import csv
import qrcode
from tkinter import messagebox

def generate_qr_codes(csv_file, output_directory, name_column, progress_label):
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)

            if name_column not in reader.fieldnames:
                raise ValueError(f"Column '{name_column}' not found in the CSV file.")

            rows = list(reader)
            total_rows = len(rows)
            generated_count = 0

            for row in rows:
                qr_name = row[name_column]
                qr_data = '\n'.join([f"{key}: {value}" for key, value in row.items()])

                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(qr_data)
                qr.make(fit=True)

                img = qr.make_image(fill_color="black", back_color="white")
                qr_path = os.path.join(output_directory, f"{qr_name}.png")
                img.save(qr_path)

                generated_count += 1
                progress_label.configure(text=f"Generated: {generated_count}/{total_rows}")
                progress_label.update_idletasks()

            messagebox.showinfo("Success", f"QR codes generated successfully in {output_directory}")
    except Exception as e:
        messagebox.showerror("Error", str(e))
