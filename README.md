# Journal Application

The **Journal Application** is a Python-based tool designed to help users efficiently write and read journal entries stored in a CSV file. This application features a simple interface for managing journal entries by date, ensuring data persistence between sessions.

---

## Features

- **Write Journal Entries**: Save journal entries by specifying the date and content.
- **Read Journal Entries**: Retrieve journal entries by entering the date.
- **Date Validation**: Ensure dates are in the correct format (D/M/Y).
- **User Interface**: Simple text-based menu with enhanced visuals using the `tabulate` and `pyfiglet` libraries.

---

## Prerequisites

To run the Journal Application, ensure you have the following installed:
- Python 3.x
- `pyfiglet` library for styled text (`pip install pyfiglet`)
- `tabulate` library for table formatting (`pip install tabulate`)

---

## File Structure

- **`journal.py`**: Contains the `Journal` class with methods for reading, writing, and validating journal entries.
- **`main.py`**: The main program that handles user interaction and displays the menu.
- **`journal.csv`**: CSV file storing the journal entries (date, content).

---

## How It Works

### 1. **Write Journal Entry**
   - Select the write option by entering `w`.
   - Enter the date in the format `D/M/Y`.
   - Enter the journal content.
   - The entry will be saved to `journal.csv`.

### 2. **Read Journal Entry**
   - Select the read option by entering `r`.
   - Enter the date of the journal entry you wish to read in the format `D/M/Y`.
   - The application will display the journal entry if it exists.

### 3. **Exit**
   - Select the exit option by entering `e` to close the application.

---

## Code Breakdown

### `journal.py`

The `Journal` class includes key methods for managing journal entries.

- **`__init__(self, date, file, journal)`**: Initializes a new journal entry with the specified date, file, and content.
- **`reading_journal(date, file)`**: Reads and returns the journal entry for the given date from the CSV file.
- **`writing_journal(date, file, journal)`**: Writes a new journal entry to the CSV file.
- **`date_verification(date)`**: Validates the date format.

### `main.py`

The main script handles user interaction and displays the menu.

- **`main()`**: The entry point of the application. Displays the title, menu, and processes user input.
- **`title()`**: Renders and displays the application title using `pyfiglet`.
- **`menu()`**: Displays the available options using the `tabulate` library.

---

## How to Run

1. Clone or download the repository to your local machine.
2. Ensure the required CSV file (`journal.csv`) is present.
3. Run the program using Python:

   ```bash
   python main.py
   ```
## Future Improvements
- Add functionality for managing multiple entries at once.
- Implement a graphical user interface (GUI) for better user interaction.