Python Serialization & File Handling Utilities

📌 Description

This project contains a collection of Python modules and scripts that demonstrate:

File reading, writing, and appending

JSON serialization and deserialization

Working with command-line arguments

Converting objects and classes to dictionaries

CSV to JSON conversion

XML serialization and deserialization

Object serialization using Pickle

Generating Pascal’s Triangle


📂 Files Overview

📄 File Handling

read_file: Reads and prints a text file.

write_file: Writes text to a file and returns character count.

append_write: Appends text to the end of a file.

📄 JSON Utilities

to_json_string: Converts a Python object to a JSON string.

from_json_string: Converts a JSON string to a Python object.

save_to_json_file: Saves a Python object to a JSON file.

load_from_json_file: Loads a Python object from a JSON file.

📄 Command-Line Arguments

add_item.py
Adds all command-line arguments to a Python list and saves them to add_item.json.

Creates the file if it does not exist

Preserves existing data

📄 Classes & Objects

class_to_json: Returns the dictionary representation of an object.

Student class:

Attributes: first_name, last_name, age

to_json() with optional attribute filtering

reload_from_json() to update attributes from a dictionary

📄 Pascal’s Triangle

pascal_triangle: Generates Pascal’s Triangle up to n rows.

🔁 Advanced Serialization

📄 Pickle Serialization

CustomObject class

Serialize and deserialize custom objects using pickle

Handles file errors safely

Includes a display method for object data

📄 CSV to JSON

convert_csv_to_json

Reads data from a CSV file

Converts it into data.json

Returns False if the CSV file is not found

📄 XML Serialization

serialize_to_xml

Converts a Python dictionary into an XML file

deserialize_from_xml

Reads an XML file and converts it back into a dictionary
