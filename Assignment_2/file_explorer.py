import os
import stat

path = input("Enter directory path (e.g. . ): ")

if os.path.isdir(path):
    print(f"\nListing files in: {path}")
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        
        # Check if it is a file
        if os.path.isfile(full_path):
            size = os.path.getsize(full_path)
            # Get file permissions mask
            mode = os.stat(full_path).st_mode
            permissions = stat.filemode(mode)
            
            print(f"File: {item} | Size: {size} bytes | Permissions: {permissions}")
else:
    print("Invalid directory path.")
