import json

def create_notebook(cells):
    notebook = {
        "cells": [],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.7.3"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

    for cell in cells:
        if cell['cell_type'] == 'code':
            notebook['cells'].append({
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": cell['source']
            })
        else:
            notebook['cells'].append({
                "cell_type": "markdown",
                "metadata": {},
                "source": [cell['source'] + '\n']  # Ensure it ends with a newline
            })

    return notebook

def save_notebook(notebook, filename='notebook.ipynb'):
    with open(filename, 'w') as f:
        json.dump(notebook, f, indent=2)
    print(f'Notebook saved as {filename}')
