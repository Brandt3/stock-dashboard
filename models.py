import csv
import matplotlib.pyplot as plt
from tkinter import messagebox, filedialog
from datetime import datetime


def export_csv_from_db(rows, columns):
    # Check to see if there is data to be put into a CSV file otherwise returns error
    if not rows:
        return messagebox.showerror("Unsuccessful Export", f"No data to create CSV file.")

    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    # Write to CSV
    if file_path:
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(columns)  # Write column names
            for row in rows:
                writer.writerow(row)    # Write data rows

    messagebox.showinfo("Export Successful", f"CSV file '{file_path}' has been created.")

def createModel(data, title, sign):
    # This doesn't allow the button to visualize anything and gives a error message if data is empty
    if not data:
        return messagebox.showerror("Unsuccessful Data Visualization", f"No data to visualize.")
    
    if len(title) == 7:
        ticker = data[0][0]
        dates = [(datetime.strptime(item[1], "%Y-%m-%d")) for item in data]
        opens = [float(item[2]) for item in data]
        highs = [float(item[3]) for item in data]
        lows = [float(item[4]) for item in data]
        closes = [float(item[5]) for item in data]
        # volumes = [item[6] for item in data]
        
        plt.figure(figsize=(14, 6))
        
        plt.plot(dates, opens, label="Open")
        plt.plot(dates, highs, label="High")
        plt.plot(dates, lows, label="Low")
        plt.plot(dates, closes, label="Close")
        # plt.plot(dates, volumes, label="Volume")

        every_5_dates = dates[::5]
        labels = [d.strftime('%Y-%m-%d') for d in every_5_dates]
        plt.xticks(ticks=every_5_dates, labels=labels, rotation=45)

        plt.title(f"{ticker} Stock Trends (Dates Every 5 Stock Days For The Past 100 Days)")
        plt.xlabel("Date")
        plt.ylabel("Value")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    
    if len(title) == 2:
        '''Found this line through research but it is very important becasue it uses the datetime 
        library and converts the string dates into readable dates for the matplotlib'''
        data = [(datetime.strptime(item[0], "%Y-%m-%d"), item[1]) for item in data]

        date = [item[0] for item in data]
        value = [float(item[1]) for item in data]
        # date = date[::5]
        # value = value[::5]
        days = list(range(len(value)))[::-1]


        plt.figure(figsize=(14, 6)) 
        # For cleaner x-axis it only shows every fifth date
        every_5_dates = date[::5]
        labels = [d.strftime('%Y-%m-%d') for d in every_5_dates]
        plt.xticks(ticks=every_5_dates, labels=labels, rotation=45)


        plt.plot(date, value, marker='o', linestyle='-', color='b', linewidth=2)
        plt.xlabel("Dates")
        plt.ylabel(title[1])
        plt.title(f"{sign} {title[1]} Over Time (Dates Every 5 Stock Days For The Past 100 Days) ")
        plt.grid(True)

        plt.tight_layout() 
        plt.show()

# import matplotlib.pyplot as plt

# # List of high prices
# high_prices = [
#     233.36, 232.78, 249.34, 242.64, 240.805, 241.775, 243.2999, 241.53, 241.77, 237.58,
#     232.57, 236.3, 233.05, 232.29, 240.16, 250.61, 252.79, 250.62, 250.89, 247.57,
#     250.3, 254.32, 250.9, 248.82, 245.205, 246.8, 253.66, 252.57, 254.63, 248.9499,
#     249.27, 253.1273, 256.7, 266.45, 261.96, 252.1, 252.74, 255.48, 255.99, 252.8099,
#     257.63, 258.325, 263.48, 263.845, 264.83, 265.09, 264.36, 263.965, 261.94, 259.28,
#     256.4, 256.75, 251.95, 256.93, 263.38, 265.72, 265.25, 262.06, 257.235, 261.8,
#     229.47, 225.77, 224.3, 226.8104, 226.04, 224.4, 227.45, 225.955, 222.68, 221.6761,
#     218.125, 219.59, 222.43, 224.9, 226.711, 224.35, 223.66, 222.49, 221.0493, 221.5942,
#     224.42, 225.4, 224.4446, 223.74, 227.6847, 226.2, 229.035, 230.2, 231.03, 233.775,
#     233.89, 233.0, 234.39, 239.35, 238.38, 236.52, 233.74, 229.11, 228.38, 230.36
# ]

# # Generate X axis (just simple numbers for each day)
# days = list(range(len(high_prices)))

# # Plotting
# plt.figure(figsize=(14, 6))
# plt.plot(days, high_prices, marker='o', linestyle='-', color='blue')

# plt.title('Line Graph of High Prices')
# plt.xlabel('Days')
# plt.ylabel('High Price')
# plt.grid(True)
# plt.tight_layout()
# plt.show()
