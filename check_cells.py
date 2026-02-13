import json

try:
    with open('zomato_analysis.ipynb', 'r') as f:
        data = json.load(f)
    cells = data.get('cells', [])
    executed = [cell for cell in cells if cell.get('execution_count') is not None]
    print(f'Total cells: {len(cells)}, Executed cells: {len(executed)}')
    if executed:
        print("Yes, some cells have been executed.")
    else:
        print("No, no cells have been executed yet.")
except Exception as e:
    print(f'Error reading notebook: {e}')
