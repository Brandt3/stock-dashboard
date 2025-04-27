import tkinter as tk
from ttkbootstrap import ttk
from tkinter import messagebox
import sqlite3

from api_caller import fetchApiData
from data_cleanup import cleanApiData
from db_handler import insertStock, createDB
from models import export_csv_from_db, createModel


# Function to fetch stock data from the database using SQL queries
def fetch_data_from_db(ticker):
    conn = sqlite3.connect('FinalProject.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Stocks WHERE Ticker_Symbol = ?", (ticker,))
    rows = cursor.fetchall()
    conn.close()
    return rows

# Function to display fetched data in Treeview 
def display_data():
    ticker = ticker_entry.get().strip().upper()

    # Step 1: Check if it's already in DB
    results = fetch_data_from_db(ticker)
    if not results:
        # Step 2: If not in DB, fetch from API
        is_valid, json_data = fetchApiData(ticker)
        if is_valid:
            # Step 3: Convert to Stock objects and insert
            stocks, companies = cleanApiData(ticker, json_data)
            insertStock(stocks, companies)
            results = fetch_data_from_db(ticker)
        else:
            messagebox.showerror("Error", f"'{ticker}' is not valid or API limit reached.")
            return
    
    # Resets the chosen attributes to show so everyhting is reset and recreates the columns
    filter_var.set("All")
    tree["columns"] = ("Ticker", "Date", "Open", "High", "Low", "Close", "Volume")
    for col in tree["columns"]:
        tree.heading(col, text=col, command=lambda _col=col: sort_treeview(_col, False))

    # Step 4: Clear Treeview and populate with data
    for row in tree.get_children():
        tree.delete(row)
    for row in results:
        tree.insert("", "end", values=row)

def sort_treeview(value, valid):
    l = [(tree.set(k, value), k) for k in tree.get_children('')]

    # This trys to see if it is a number or string value that is sorted
    try:
        l.sort(key=lambda t: float(t[0].replace(",", "")), reverse=valid)
    except ValueError:
        l.sort(key=lambda t: t[0], reverse=valid)

    for index, (val, k) in enumerate(l):
        tree.move(k, '', index)

    # Clear all arrows
    for col in tree["columns"]:
        tree.heading(col, text=col + " ↑", command=lambda _col=col: sort_treeview(_col, False))

    # Update current column with the proper arrow
    arrow = " ↓" if valid else " ↑"
    tree.heading(value, text=value + arrow, command=lambda: sort_treeview(value, not valid))

def get_filtered_data(event=None):
    selected_col = filter_var.get()

    ticker = ticker_entry.get().strip().upper()
    results = fetch_data_from_db(ticker)
    # Checks to see if all is selected then there is no need to filter data
    if selected_col == "All":
        tree["columns"] = ("Ticker", "Date", "Open", "High", "Low", "Close", "Volume")
        for col in tree["columns"]:
            tree.heading(col, text=col, command=lambda _col=col: sort_treeview(_col, False))
        display_data()
        return

    col_map = {
        "Open": 2,
        "High": 3,
        "Low": 4,
        "Close": 5,
        "Volume": 6
    }
    # This gets the index of the attribute the user only wants to show
    col_index = col_map[selected_col]
    dates = []
    values = []

    for row in results:
        dates.append(row[1])  # Date is always index 1
        values.append(float(row[col_index]))

    data = list(zip(dates, values))

    # Setting the column titles to the date and the selected attribute
    tree["columns"] = ("Date", selected_col)
    # This makes the headers sortable
    tree.heading("Date", text="Date", command=lambda: sort_treeview("Date", False))
    tree.heading(selected_col, text=selected_col, command=lambda: sort_treeview(selected_col, False))

    for row in tree.get_children():
        tree.delete(row)
    for row in data:
        tree.insert("", "end", values=row)

def get_current_tree_data():
    # Get all visible data and return it 
    columns = tree["columns"]
    rows = []
    for item_id in tree.get_children():
        row = tree.item(item_id)['values']
        rows.append(row)
    return rows, columns

def add_to_watchlist():
    ticker = ticker_entry.get().strip().upper()
    if not ticker:
        messagebox.showerror("Error", "Please enter a ticker symbol.")
        return
    
    # Validate the ticker by calling the API
    is_valid, _ = fetchApiData(ticker)
    if not is_valid:
        messagebox.showerror("Error", f"'{ticker}' is not a valid ticker or API limit reached.")
        return

    # If valid, add to watchlist
    if ticker not in saved_dropdown['values']:
        new_list = list(saved_dropdown['values']) + [ticker]
        saved_dropdown['values'] = new_list
        saved_var.set(ticker)
        status_label.config(text=f"{ticker} added to watchlist!")
    else:
        messagebox.showinfo("Info", f"{ticker} is already in the watchlist.")

def load_saved_ticker(event=None):
    ticker = saved_var.get()
    if ticker:
        ticker_entry.delete(0, tk.END)
        ticker_entry.insert(0, ticker)
        filter_var.set("All")
        display_data()

def reset_display():
    ticker = ticker_entry.get().strip().upper()
    if ticker:  # If there's a ticker, try to reload it
        display_data()
    else:
        # Clear the TreeView if no ticker
        for row in tree.get_children():
            tree.delete(row)

# Call to make sure db is created
createDB()

# ---- Initialize root window ----
root = tk.Tk()
root.title("Stock Data Viewer")

# Center the window on the screen
window_width = 1500
window_height = 650
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# ---- Top Row: Ticker Entry ----
ticker_label = ttk.Label(root, text="Ticker Symbol:")
ticker_label.grid(row=0, column=0, padx=5, pady=10, sticky='w')

ticker_entry = ttk.Entry(root, width=25)
ticker_entry.grid(row=0, column=1, padx=5, pady=10)

search_button = ttk.Button(root, text="Search", command=display_data, style="primary.TButton")
search_button.grid(row=0, column=2, padx=5, pady=10)

# ---- Second Row: Filter and Saved Tickers ----
filter_label = ttk.Label(root, text="Filter By:")
filter_label.grid(row=1, column=0, padx=5, pady=10, sticky='w')

filter_var = tk.StringVar()
filter_options = ["All", "Open", "Close", "High", "Low", "Volume"]
filter_dropdown = ttk.Combobox(root, textvariable=filter_var, values=filter_options, state="readonly")
filter_dropdown.bind("<<ComboboxSelected>>", get_filtered_data)
filter_dropdown.grid(row=1, column=1, padx=5, pady=10)
filter_dropdown.current(0)

saved_label = ttk.Label(root, text="Saved Tickers:")
saved_label.grid(row=1, column=2, padx=5, pady=10, sticky='w')

saved_var = tk.StringVar()
saved_dropdown = ttk.Combobox(root, textvariable=saved_var, values=["GOOG", "IBM", "AAPL"], state="readonly")
saved_dropdown.bind("<<ComboboxSelected>>", load_saved_ticker)
saved_dropdown.grid(row=1, column=3, padx=5, pady=10)

add_watchlist_button = ttk.Button(root, text="Add to Watchlist", style="success.TButton", command=lambda:add_to_watchlist())
add_watchlist_button.grid(row=0, column=3, padx=5, pady=10)

reset_button = ttk.Button(root, text="Reset Display", style="secondary.TButton", command=reset_display)
reset_button.grid(row=1, column=4, padx=10, pady=15)


# ---- Treeview Table for Displaying Stock Data ----
tree = ttk.Treeview(root, columns=("Ticker", "Date", "Open", "High", "Low", "Close", "Volume"), show="headings")

for col in ["Ticker", "Date", "Open", "High", "Low", "Close", "Volume"]:
    tree.heading(col, text=col, command=lambda: sort_treeview(col, False))

tree.grid(row=2, column=0, columnspan=5, padx=10, pady=10)

# ---- Bottom Buttons ----
data_vis_button = ttk.Button(root, text="Data Visualization", style="info.TButton", command=lambda: createModel(*get_current_tree_data(), ticker_entry.get().strip().upper()))
data_vis_button.grid(row=3, column=0, padx=10, pady=15)

# ---- This was an interesting line but becasue the function returns two item they are techincally one tuple so i use the * to unpack the items into two differnet aurguments ----
download_csv_button = ttk.Button(root, text="Download CSV", style="danger.TButton", command=lambda: export_csv_from_db(*get_current_tree_data()))
download_csv_button.grid(row=3, column=4, padx=10, pady=15)

# ---- Status Label ----
status_label = ttk.Label(root, text="", foreground="green")
status_label.grid(row=4, column=0, columnspan=5, padx=10, pady=10)

# ---- Main loop ----
root.mainloop()
