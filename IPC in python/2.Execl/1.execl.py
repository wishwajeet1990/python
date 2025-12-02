import os

# Run dir in CMD (cmd closes after execution because of /c)
os.execl(r"C:\Windows\System32\cmd.exe", "cmd.exe", "/c", "dir")