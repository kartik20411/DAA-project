import os
import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox

def select_files():
    """Open a file dialog to select multiple files"""
    files = filedialog.askopenfilenames(title="Select Files to Zip")
    file_list.set("\n".join(files))  # Display selected files in the GUI
    return files

def zip_selected_files():
    """Compress the selected files into a ZIP archive"""
    files = file_list.get().split("\n")
    
    if not files or files == [""]:
        messagebox.showerror("Error", "No files selected!")
        return

    zip_filename = filedialog.asksaveasfilename(defaultextension=".zip",
                                                filetypes=[("ZIP Files", "*.zip")],
                                                title="Save ZIP File")
    
    if not zip_filename:
        return  # User canceled save dialog

    try:
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for file in files:
                if os.path.exists(file):
                    zipf.write(file, os.path.basename(file))  # Add file to ZIP
        messagebox.showinfo("Success", f"Files successfully zipped into {zip_filename}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create GUI Window
root = tk.Tk()
root.title("File Zipper")
root.geometry("500x400")

# UI Elements
file_list = tk.StringVar()

tk.Label(root, text="Selected Files:", font=("Arial", 12)).pack(pady=10)
file_display = tk.Label(root, textvariable=file_list, bg="white", relief="solid", width=60, height=10, anchor="nw", justify="left")
file_display.pack(pady=5)

tk.Button(root, text="Select Files", command=select_files, font=("Arial", 12), bg="lightblue").pack(pady=10)
tk.Button(root, text="Zip Files", command=zip_selected_files, font=("Arial", 12), bg="lightgreen").pack(pady=10)

# Run the GUI
root.mainloop()