from services.confluence_getters import fetch_and_store_confluence_data

output_directory = 'confluence_data'
fetch_and_store_confluence_data(output_directory)

# Example of loading and printing the content of a saved text file
with open('confluence_data/Space One/Sample Page.txt', 'r', encoding='utf-8') as f:
    print(f.read())
