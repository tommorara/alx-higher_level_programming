#!/usr/bin/python3
"""script that adds all arguments to a Python
list, and then save them to a file
"""
import sys
if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        # Load existing data from file if available
        data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        data = []
    # Add new command-line arguments to the existing list
    data.extend(sys.argv[1:])
    # Save the updated list to add_item.json
    save_to_json_file(data, "add_item.json")
