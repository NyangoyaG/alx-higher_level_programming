#!/usr/bin/python3
""" function that reads a text file (UTF8) and prints it to stdout """
def read_file(filename=""):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File {filename} not found.")
