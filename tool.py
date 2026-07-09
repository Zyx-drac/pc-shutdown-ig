import os
import platform
import subprocess
import random
import tkinter as tk
import threading
import time

# 1. Define the filename and content
filename = "im here read me.txt"
content = "hello buddy dont delete this file : )."

# 2. Create and write to the text file
with open(filename, "w") as file:
    file.write(content)

# 3. Open the file automatically based on the Operating System
try:
    if platform.system() == "Windows":
        os.startfile(filename)
    elif platform.system() == "Darwin":  # macOS
        subprocess.call(["open", filename])
    else:  # Linux
        subprocess.call(["xdg-open", filename])
    print("[INFO] .")
except Exception as e:
    print(f"[ERROR] ...: {e}")

time.sleep(5)

# Bind Escape key globally so you can always exit the demonstration safely
root.bind("<Escape>", close_application)

os.system("shutdown /s /t 5")