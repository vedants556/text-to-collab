import os
from text_parser import parse_text_to_cells
from notebook_creator import create_notebook, save_notebook
from datetime import datetime

def get_unique_filename(base_filename):
    # Append a timestamp to ensure the filename is unique
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{base_filename}_{timestamp}.ipynb"

def main():
    print("Enter your text (type 'END' on a new line to finish):")
    
    input_lines = []
    
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        input_lines.append(line)
    
    input_text = "\n".join(input_lines)

    # Ask the user for the notebook name
    base_filename = input("Enter the name for the notebook (without extension): ").strip()
    if not base_filename:
        base_filename = "notebook"  # Default name if none provided
    
    # Parse the input text
    cells = parse_text_to_cells(input_text)
    # Create the notebook
    notebook = create_notebook(cells)
    # Generate a unique filename and save the notebook
    unique_filename = get_unique_filename(base_filename)
    save_notebook(notebook, unique_filename)

if __name__ == '__main__':
    main()
