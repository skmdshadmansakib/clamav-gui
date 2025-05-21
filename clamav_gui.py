import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
import datetime
import os

# Path to clamdscan
CLAMDSCAN_PATH = r"C:\clamav-dev\clamav-1.4.2\build\install\clamdscan.exe"

# Output log file
LOG_FILE = "clamav_scan_log.txt"

def log_results(text):
    with open(LOG_FILE, "a") as f:
        f.write(f"\n--- Scan on {datetime.datetime.now()} ---\n")
        f.write(text + "\n")

def scan_path(path, show_only_infected=False):
    progress_bar.start()
    try:
        result = subprocess.run(
            [CLAMDSCAN_PATH, '--fdpass', '--recursive', path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output = result.stdout or result.stderr
        log_results(output)

        # Filter infected results
        if show_only_infected:
            filtered = "\n".join(
                line for line in output.splitlines()
                if "FOUND" in line
            )
            output = filtered or "✅ No infected files found."

        messagebox.showinfo("Scan Completed", output)
    except Exception as e:
        messagebox.showerror("Scan Error", f"Scan failed:\n{str(e)}")
    finally:
        progress_bar.stop()

def threaded_scan(path, show_only_infected):
    threading.Thread(target=scan_path, args=(path, show_only_infected), daemon=True).start()

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        threaded_scan(file_path, infected_only_var.get())

def select_folder_or_drive():
    folder_path = filedialog.askdirectory(title="Select Folder / Drive (e.g., D:\\, E:\\)")
    if folder_path:
        threaded_scan(folder_path, infected_only_var.get())

def open_log():
    if os.path.exists(LOG_FILE):
        os.startfile(LOG_FILE)
    else:
        messagebox.showinfo("No Logs", "No scan logs found yet.")

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("🛡️ ClamAV Enhanced Scanner")
root.geometry("450x320")
root.configure(bg="#f8f8f8")

tk.Label(root, text="ClamAV GUI Scanner", font=("Arial", 16, "bold"), bg="#f8f8f8").pack(pady=10)

# Buttons
tk.Button(root, text="📄 Scan a File", width=30, command=select_file).pack(pady=5)
tk.Button(root, text="📁 Scan Folder / USB / Drive", width=30, command=select_folder_or_drive).pack(pady=5)

# Check option to show only infected
infected_only_var = tk.BooleanVar()
tk.Checkbutton(root, text="Only show infected files", variable=infected_only_var, bg="#f8f8f8").pack(pady=5)

# Progress bar
progress_bar = ttk.Progressbar(root, mode="indeterminate", length=300)
progress_bar.pack(pady=10)

# Log viewer
tk.Button(root, text="🗒️ View Scan Log", command=open_log).pack(pady=5)


tk.Label(root, text="Powered By SS", fg="green", bg="#f8f8f8").pack(pady=5)

root.mainloop()
