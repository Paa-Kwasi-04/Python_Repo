import tkinter as tk
from tkinter import ttk, messagebox
from api_key import API_KEY
import requests

# --- API Calls ---


def safe_get(url, params):
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        messagebox.showerror("API Error", f"Error contacting API:\n{e}")
        return None


def get_symbols():
    url = "https://api.forexrateapi.com/v1/symbols"
    params = {"api_key": API_KEY}
    data = safe_get(url, params)
    return data.get("symbols", {}) if data else {}


def convert_currency(from_curr, to_curr, amount):
    url = "https://api.forexrateapi.com/v1/convert"
    params = {
        "api_key": API_KEY,
        "from": from_curr,
        "to": to_curr,
        "amount": amount
    }
    data = safe_get(url, params)
    return data.get("result") if data else None

# --- GUI ---


class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.symbols = get_symbols()
        if not self.symbols:
            messagebox.showerror("Error", "Failed to load currency symbols.")
            self.root.quit()
            return

        self.create_widgets()

    def create_widgets(self):
        padding = {"padx": 10, "pady": 10}

        # Amount
        ttk.Label(self.root, text="Amount:").grid(
            row=0, column=0, sticky="w", **padding)
        self.amount_entry = ttk.Entry(self.root)
        self.amount_entry.grid(row=0, column=1, **padding)

        # From Currency
        ttk.Label(self.root, text="From:").grid(
            row=1, column=0, sticky="w", **padding)
        self.from_currency = ttk.Combobox(
            self.root, values=list(self.symbols.keys()), state="readonly")
        self.from_currency.grid(row=1, column=1, **padding)
        self.from_currency.set("USD")

        # To Currency
        ttk.Label(self.root, text="To:").grid(
            row=2, column=0, sticky="w", **padding)
        self.to_currency = ttk.Combobox(self.root, values=list(
            self.symbols.keys()), state="readonly")
        self.to_currency.grid(row=2, column=1, **padding)
        self.to_currency.set("EUR")

        # Convert Button
        self.convert_button = ttk.Button(
            self.root, text="Convert", command=self.perform_conversion)
        self.convert_button.grid(row=3, column=0, columnspan=2, **padding)

        # Result Label
        self.result_label = ttk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.grid(row=4, column=0, columnspan=2, **padding)

    def perform_conversion(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning(
                "Invalid Input", "Please enter a positive number.")
            return

        from_curr = self.from_currency.get()
        to_curr = self.to_currency.get()

        result = convert_currency(from_curr, to_curr, amount)
        if result is not None:
            self.result_label.config(
                text=f"{amount:.2f} {from_curr} = {result:.2f} {to_curr}")
        else:
            self.result_label.config(text="Conversion failed.")


# --- Run App ---
if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
