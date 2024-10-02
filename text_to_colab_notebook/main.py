from text_parser import parse_text_to_cells
from notebook_creator import create_notebook, save_notebook  # Ensure both functions are imported

def main():
    print("Enter your text (type 'END' on a new line to finish):")
    
    input_lines = []
    
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        input_lines.append(line)
    
    input_text = "\n".join(input_lines)

    # Parse the input text
    cells = parse_text_to_cells(input_text)
    # Create the notebook
    notebook = create_notebook(cells)
    # Save the notebook to a file
    save_notebook(notebook)

if __name__ == '__main__':
    main()
