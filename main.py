import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from PyPDF2 import PdfReader, PdfWriter
import os
import random

def split_pdf(input_pdf, split_pages):
    reader = PdfReader(input_pdf)
    total_pages = len(reader.pages)

    base_filename = os.path.splitext(os.path.basename(input_pdf))[0]
    output_dir = os.path.dirname(input_pdf)
    random_number = str(random.randint(10000, 99999))

    for i in range(0, total_pages, split_pages):
        writer = PdfWriter()
        for j in range(i, min(i + split_pages, total_pages)):
            writer.add_page(reader.pages[j])
        
        output_filename = f"{base_filename}-SPLIT-{random_number}-{(i // split_pages + 1):02d}.pdf"
        output_path = os.path.join(output_dir, output_filename)
        with open(output_path, "wb") as output_pdf:
            writer.write(output_pdf)
        print(f"Created: {output_path}")

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    return file_path

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    input_pdf = select_file()
    if input_pdf:
        split_pages = simpledialog.askinteger("Input", "After how many pages should the PDF be split?", minvalue=1)
        if split_pages:
            split_pdf(input_pdf, split_pages)
            messagebox.showinfo("Success", "The PDF has been successfully split!")
        else:
            messagebox.showwarning("Error", "Invalid page input")
    else:
        messagebox.showwarning("Error", "No file selected")

if __name__ == "__main__":
    main()
