#!/usr/bin/env python3
import os

# Read the file
with open("shellprac.txt", "r") as file:
    file_content = file.read()
    print("File contents:", file_content)

# Get directory listing
files_and_dirs = os.listdir()
print("Files and directories:", files_and_dirs)
