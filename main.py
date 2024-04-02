
import tkinter as tk
from tkinter import messagebox
from validation import validate_data
from pdf_generation import generate_pdf

def submit_form():
    # Get data from GUI fields
    name = name_entry.get().strip()
    aicte_id = aicte_id_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()
    college = college_entry.get().strip()

    # Validate data
    validation_result, error_message = validate_data(name, aicte_id, email, phone, college)
    if validation_result:
        # Generate PDF
        generate_pdf(name, aicte_id, email, phone, college)
        messagebox.showinfo("Success", "PDF generated successfully!")
        clear_form()
    else:
        messagebox.showerror("Error", error_message)

def clear_form():
    name_entry.delete(0, tk.END)
    aicte_id_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    college_entry.delete(0, tk.END)

# Create tkinter window
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("400x250")  # Set initial window size

# Create input fields
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

aicte_id_label = tk.Label(root, text="AICTE ID:")
aicte_id_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
aicte_id_entry = tk.Entry(root)
aicte_id_entry.grid(row=1, column=1, padx=10, pady=5)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=5)

phone_label = tk.Label(root, text="Phone:")
phone_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
phone_entry = tk.Entry(root)
phone_entry.grid(row=3, column=1, padx=10, pady=5)

college_label = tk.Label(root, text="College:")
college_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
college_entry = tk.Entry(root)
college_entry.grid(row=4, column=1, padx=10, pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=5, column=0, columnspan=2, pady=10)

# Clear form button
clear_button = tk.Button(root, text="Clear Form", command=clear_form)
clear_button.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
