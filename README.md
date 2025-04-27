# Stock Dashboard GUI

A lightweight Python application for searching, viewing, and analyzing stock data through an intuitive desktop interface.  
The app validates ticker symbols through an API, stores data locally in a SQLite database, and provides real-time filtering and charting capabilities — all built using `Tkinter` and `ttkbootstrap`.

## Features

- 🔎 **Ticker Search & Validation** — Search for stock data using a ticker symbol with API validation.
- 🗄️ **SQLite Integration** — Automatically stores and retrieves stock data locally.
- 📊 **Data Filtering & Visualization** — View selected stock attributes and plot them directly from the Treeview table.
- 🧹 **Reset & Refresh Buttons** — Easily clear or reload data without restarting the app.
- 🎨 **Modern UI** — Built with `ttkbootstrap` for a clean, responsive interface.

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
  - `stock_dashboard_gui.py` — Main application GUI (entry point)
  - `README.md` — Project documentation


## How It Works

1. Enter a stock ticker symbol into the search bar.
2. The app validates the ticker via an API call.
3. If valid, stock data is fetched, stored in SQLite, and displayed in the GUI.
4. Select specific attributes (e.g., Open, High, Low, Close) to filter the data.
5. Plot filtered results directly from the displayed table.
6. Use the Reset button to clear or reload the view as needed.

