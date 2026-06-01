# Assignment 2 - File System Interaction

## Libraries & Functions Used
* `os.listdir()`: Used to iterate through the given directory path and retrieve all items inside it.
* `os.path.getsize()`: Used to obtain the exact file size in bytes by tapping into file metadata.
* `os.stat().st_mode` & `stat.filemode()`: Used to extract the raw OS file permission flags and convert them into a human-readable format (e.g., `-rw-r--r--`).

