# 🛡️ ClamAV GUI - Windows Antivirus Frontend

A lightweight graphical user interface (GUI) for [ClamAV](https://www.clamav.net/) built with Python and Tkinter. Easily scan files, folders, USB drives, or entire local disks for viruses on Windows using ClamAV’s engine — no command line needed.

---

## 🔧 Features

- ✅ File & Folder virus scanning  
- ✅ USB drive (pendrive) scanning  
- ✅ Selectable disk scanning  
- ✅ Save scan results to `.txt`  
- ✅ Option to show only infected files  
- ✅ Visual progress bar  
- ✅ Clean, beginner-friendly interface  
- 🔜 More features coming soon: quarantine, scheduling, auto-clean, notifications

---

## 🚀 Getting Started

### Requirements

- ✅ [ClamAV for Windows](https://www.clamav.net/downloads)
- ✅ Python 3.7+  
- ✅ Modules: `tkinter`, `subprocess`, `threading`, `datetime`, `os`

### Setup Instructions

1. **Clone this repo**
   ```bash!

   git clone https://github.com/skmdshadmansakib/clamav-gui.git
   cd clamav-gui
📸 Screenshots

[Screenshot 2025-05-21 132148](https://github.com/user-attachments/assets/75d6286b-7374-49f5-a47f-033d7a0e8db7)


![Screenshot 2025-05-21 132125](https://github.com/user-attachments/assets/0059cb45-e46b-4d55-b6e8-6fdeb471a4a2)


![Screenshot 2025-05-21 132058](https://github.com/user-attachments/assets/d4a2f1f3-96ce-4377-a1f8-c32c84d75f4d)



Run the GUI!!!!
python clamav_gui.py

📁 Project Structure
clamav-gui/
├── clamav_gui.py       # Main GUI script
├── README.md           # Project description
└── results/            # Saved scan logs
