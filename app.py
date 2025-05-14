import tkinter as tk
from tkinter import messagebox

def calculate_emi():
    try:
        principal = float(entry_principal.get())
        annual_rate = float(entry_rate.get())
        years = int(entry_years.get())

        monthly_rate = annual_rate / (12 * 100)
        months = years * 12

        emi = principal * monthly_rate * ((1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
        total_payment = emi * months
        total_interest = total_payment - principal

        label_emi_result.config(text=f"Monthly EMI: ₹ {emi:.2f}")
        label_interest_result.config(text=f"Total Interest: ₹ {total_interest:.2f}")
        label_total_result.config(text=f"Total Payment: ₹ {total_payment:.2f}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("EMI Calculator")
root.geometry("400x300")
root.resizable(False, False)

# Labels and entry fields
tk.Label(root, text="Loan Amount (₹):").grid(row=0, column=0, padx=10, pady=10, sticky='e')
entry_principal = tk.Entry(root)
entry_principal.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Annual Interest Rate (%):").grid(row=1, column=0, padx=10, pady=10, sticky='e')
entry_rate = tk.Entry(root)
entry_rate.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Loan Tenure (years):").grid(row=2, column=0, padx=10, pady=10, sticky='e')
entry_years = tk.Entry(root)
entry_years.grid(row=2, column=1, padx=10, pady=10)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate EMI", command=calculate_emi)
calculate_button.grid(row=3, column=0, columnspan=2, pady=20)

# Output Labels
label_emi_result = tk.Label(root, text="Monthly EMI: ₹ 0.00")
label_emi_result.grid(row=4, column=0, columnspan=2)

label_interest_result = tk.Label(root, text="Total Interest: ₹ 0.00")
label_interest_result.grid(row=5, column=0, columnspan=2)

label_total_result = tk.Label(root, text="Total Payment: ₹ 0.00")
label_total_result.grid(row=6, column=0, columnspan=2)

# Run the app
root.mainloop()
