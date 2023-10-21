#!/usr/bin/python3
"""
    Module: add_item
"""
import json
import sys
import os


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

# Create a list where we will store the arguments
if os.path.exists('add_item.json'):
    my_list = load_from_json_file('add_item.json')
else:
    my_list = []

# Loop through the arguments and append them to the list
for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])

# Save the list to the file
save_to_json_file(my_list, 'add_item.json')
