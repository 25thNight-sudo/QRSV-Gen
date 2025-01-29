QRSV Gen - QR Code Generator

QRSV Gen is a Python-based QR code generator with a GUI built using CustomTkinter. It reads a CSV file, generates QR codes for each entry, and saves them to a selected directory.

Features

Upload a CSV file and generate QR codes for each row

Select a column as the name for each QR code image

Track progress while generating QR codes

Modern UI using CustomTkinter

Clickable branding link for developer information

Installation

Step 1: Clone the Repository

git clone https://github.com/yourusername/QRSV-Gen.git
cd QRSV-Gen

Step 2: Set Up a Virtual Environment (Optional but Recommended)

Windows:

python -m venv venv
venv\Scripts\activate

Mac/Linux:

python3 -m venv venv
source venv/bin/activate

Step 3: Install Dependencies

pip install -r requirements.txt

Usage

Running the Application

python main.py

Steps to Generate QR Codes:

Click the Browse button to select a CSV file.

Choose the output directory where QR codes will be saved.

Select the column name that should be used for naming the QR code files.

Click Generate QR Codes to start the process.

CSV Format

Your CSV file should have at least one column with unique values for QR code names. Example:

Name,Email,Phone
John Doe,john@example.com,1234567890
Jane Doe,jane@example.com,0987654321

Contributing

Pull requests are welcome! If you’d like to improve the project, follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature-branch).

Commit your changes (git commit -m "Add new feature").

Push to the branch (git push origin feature-branch).

Open a Pull Request.

License

This project is open-source and available under the MIT License.