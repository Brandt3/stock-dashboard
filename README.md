# Stock Dashboard GUI

A lightweight Python application for searching, viewing, and analyzing stock data through an intuitive desktop interface.  
The app validates ticker symbols through an API, stores data locally in a SQLite database, and provides real-time filtering and charting capabilities — all built using `Tkinter` and `ttkbootstrap`.

## Features

- 🔎 **Ticker Search & Validation** — Search for stock data using a ticker symbol with API validation.
- 🗄️ **SQLite Integration** — Automatically stores and retrieves stock data locally.
- 📊 **Data Filtering & Visualization** — View selected stock attributes and plot them directly from the Treeview table.
- ➕ **Add to Watchlist** — Save selected stocks to a local watchlist for quick future access.
- ↕️ **Sortable Columns** — Sort stock data ascending or descending by clicking column headers.
- 🧹 **Reset & Refresh Buttons** — Easily clear or reload data without restarting the app.
- 💾 **Download Data** — Export stock data into a CSV file.
- 🎨 **Modern UI** — Built with `ttkbootstrap` for a clean, responsive interface.

<img width="1443" alt="Screenshot 2025-04-27 at 2 57 04 PM" src="https://github.com/user-attachments/assets/39ec3ead-429d-4305-974a-8bd162901a87" />

<img width="1399" alt="Screenshot 2025-04-27 at 3 02 47 PM" src="https://github.com/user-attachments/assets/a3b275dd-d4cf-43a6-9570-9709eeff033e" />

<img width="1399" alt="Screenshot 2025-04-27 at 3 03 02 PM" src="https://github.com/user-attachments/assets/5858afbd-75b8-4d39-b0c8-9a3ec374078f" />

## Tech Stack

- **Python 3**
- **Tkinter** (GUI framework)
- **ttkbootstrap** (modern theming for Tkinter)
- **SQLite3** (local database storage)
- **Requests** (for API calls)
- **Matplotlib** (for charting selected stock attributes)

## Project Structure

- `project_folder/`
  - `api_caller.py` — Handles API requests and ticker validation
  - `class_structure.py` — Defines classes for organizing stock data
  - `data_cleanup.py` — Handles the data and cleans it using JSON parsing
  - `db_handler.py` — Manages SQLite database operations
  - `models.py` — Takes the data and converts it into data visualizations
  - `stock_dashboard_gui.py` — Main application GUI (entry point)
  - `README.md` — Project documentation
  - `test/`
    - `test_API.py` — Tests the API call to ensure it handles invalid inputs
    - `test_db_handler.py` — Tests database file creation and basic DB operations
  - `dist/`
    - `stock_dashboard_gui.app` — Final standalone executable file. Can be copied and run without Python installed.

## How It Works

1. Enter a stock ticker symbol into the search bar.
2. The app validates the ticker via an API call.
3. If valid, stock data is fetched, stored in SQLite, and displayed in the GUI.
4. Select specific attributes (e.g., Open, High, Low, Close) to filter the displayed data.
5. Add stocks to a **Watchlist** to easily track selected companies.
6. Click column headers to **sort** the data ascending or descending.
7. Plot filtered results directly from the displayed table.
8. Download the displayed stock data into a **CSV file**.
9. Use the **Reset** button to clear or reload the view as needed.

