import os
import platform
import getpass

print("=== ASSIGNMENT 1: SYSTEM INFORMATION ===")
# 1. OS name and kernel version
print(f"OS Name: {platform.system()}")
print(f"Kernel Version: {platform.release()}")

# 2. Current logged-in user
print(f"Logged-in User: {getpass.getuser()}")

# 3. Current working directory
print(f"Working Directory: {os.getcwd()}")
print("========================================")
