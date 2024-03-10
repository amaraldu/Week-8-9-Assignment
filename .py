# Importing necessary modules for GUI functionality
import tkinter as tk
from tkinter import messagebox, filedialog
import csv
import json

# Function to clean up extra quote characters from the data
def clean_data(value):
    return value.replace('"', '').strip()

# Function to convert CSV file to JSON format
def convert_csv_to_json():
    # Asking user to select a CSV file
    filename = filedialog.askopenfilename(title="Open CSV File", filetypes=[("CSV Files", "*.csv")])
    if not filename:  # If user cancels file selection
        messagebox.showerror("Error", "You didn't select a file.")
        return
    
    # Reading data from the CSV file and cleaning each row
    sales_data = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                cleaned_row = {key: clean_data(value) for key, value in row.items()}
                sales_data.append(cleaned_row)
        
        # Asking user to specify a filename to save the JSON file
        save_filename = filedialog.asksaveasfilename(title="Save JSON File", filetypes=[("JSON Files", "*.json")], defaultextension=".json")
        if not save_filename:  # If user cancels file saving
            messagebox.showerror("Error", "You didn't specify a file to save.")
            return
        
        # Writing the cleaned data into a JSON file
        with open(save_filename, 'w', encoding='utf-8') as json_file:
            json.dump(sales_data, json_file, indent=4)

        # Showing success message upon successful conversion and save
        messagebox.showinfo("Success", "Data successfully converted and saved.")
    except Exception as e:
        # Showing error message if any exception occurs during conversion
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to open the conversion window for user interaction
def open_conversion_window():
    # Creating a new window for conversion
    conversion_window = tk.Toplevel(root)
    conversion_window.title("Convert CSV to JSON")
    conversion_window.geometry("300x100")
    conversion_window.configure(bg="#005A4E")  # Setting background color

    # Button to initiate the conversion process
    convert_button = tk.Button(conversion_window, text="Convert", command=convert_csv_to_json, bg="#007B6E", fg="white")
    convert_button.pack(pady=20)

# Function to quit the program with confirmation
def quit_program():
    if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
        root.destroy()

# Main window initialization
root = tk.Tk()
root.title("Sales Data Converter")
root.geometry("400x200")
root.configure(bg="#005A4E")  # Setting background color

# Button to open the conversion window
convert_window_button = tk.Button(root, text="Open Converter", command=open_conversion_window, bg="#007B6E", fg="white")
convert_window_button.pack(pady=20)

# Button to quit the program
quit_button = tk.Button(root, text="QUIT", command=quit_program, bg="#007B6E", fg="white")
quit_button.pack(pady=20)

# Running the GUI event loop
root.mainloop()
