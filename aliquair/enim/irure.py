import os

# List of file and directory names
items = ['file1.txt', 'file2.txt', 'file3.txt', 'directory1', 'directory2']

# Separate files and directories
files = [item for item in items if os.path.isfile(item)]
directories = [item for item in items if os.path.isdir(item)]

# Example operation on files: print their names
for file in files:
    print(f"File: {file}")

# Example operation on directories: print their names
for directory in directories:
    print(f"Directory: {directory}")
