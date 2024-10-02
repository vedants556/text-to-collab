def parse_text_to_cells(input_text):
    cells = []
    lines = input_text.strip().split('\n')
    
    current_code = []
    
    for line in lines:
        if line.startswith('#'):
            if current_code:
                # Save previous code cell if it exists, without empty strings
                cells.append({'cell_type': 'code', 'source': current_code})
                current_code = []
            # Save markdown cell
            markdown_content = line[1:].strip()  # Remove '#' and whitespace
            cells.append({'cell_type': 'markdown', 'source': markdown_content})
        else:
            # Only add non-empty lines to current_code
            if line.strip():  # Check if the line is not just whitespace
                current_code.append(line)
    
    # Add any remaining code cell
    if current_code:
        cells.append({'cell_type': 'code', 'source': current_code})
    
    return cells
