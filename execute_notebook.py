import os
import nbformat
from nbclient import NotebookClient

notebook_path = r"D:\Nasa FINAL\main.ipynb"
print(f"Reading notebook: {notebook_path}")

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

client = NotebookClient(nb, timeout=600, kernel_name='python3')
print("Starting execution of main.ipynb...")

try:
    client.execute()
    print("All cells executed successfully!")
    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    print("Saved executed notebook with all outputs and figures embedded!")
except Exception as e:
    print(f"Execution encountered an error: {e}")
    # Still write whatever executed
    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    raise e
