# Text to Colab Notebook Converter

This Python application converts plain text input into a structured Google Colab notebook, making it easier to create and share interactive documents.

## Features

- **Markdown Support**: Use markdown syntax to create formatted text cells.
- **Code Cells**: Write Python code that can be executed in Google Colab.
- **Automatic File Naming**: Generated notebooks have unique filenames based on the current timestamp.
- **User-defined Notebook Names**: Users can specify custom names for their notebooks.
- **GUI Interface**: A simple graphical user interface for easy text input and notebook creation.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or higher
- wxPython (for the GUI version)

You can install wxPython using pip:

```bash
pip install wxPython
```


## Installation

1. Clone the repository or download the files to your local machine:

   ```bash
   git clone https://github.com/yourusername/text-to-colab-notebook.git
   cd text-to-colab-notebook
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### GUI Version

1. Run the `text_to_notebook.py` file:

   ```bash
   python text_to_colab_notebook/text_to_notebook.py
   ```

2. Enter your text in the main text area.
3. (Optional) Enter a custom name for your notebook in the "Enter notebook name" field.
4. Click the "Save Notebook" button to generate and save your Colab notebook.

### Command-Line Version

1. Run the `main.py` file:

   ```bash
   python text_to_colab_notebook/main.py
   ```

2. Enter your text, using '#' at the beginning of a line to denote markdown cells.
3. Type 'END' on a new line when you're finished entering text.
4. Enter a name for your notebook when prompted (or press Enter to use the default name).

## File Structure

- `text_to_notebook.py`: Contains the GUI application code.
- `main.py`: Contains the command-line interface code.
- `text_parser.py`: Handles parsing of input text into notebook cells.
- `notebook_creator.py`: Creates and saves the Jupyter notebook file.

## How It Works

1. The application takes user input as plain text.
2. It parses the text, separating it into code and markdown cells.
3. Lines starting with '#' are treated as markdown cells.
4. Other lines are treated as code cells.
5. The parsed cells are used to create a Jupyter notebook structure.
6. The notebook is saved with a unique filename based on the user's input and current timestamp.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to the Jupyter and Google Colab teams for their amazing tools.
- wxPython for providing the GUI framework.
```

Feel free to copy and use this markdown text for your README.md file!