# Real-Time Python Student Management System with MongoDB

A powerful, real-time student management system built with Python and MongoDB. This application features a graphical user interface (GUI) using Tkinter, and allows you to manage student records efficiently. You can also build an executable app for easy distribution.

## 🎥 Watch the Tutorial

[![Watch on YouTube](https://img.shields.io/badge/YouTube-Video%20Tutorial-red?logo=youtube)](https://youtu.be/PCo9FDCbsEM)

---

## 🚀 Features

- Real-time CRUD operations (Create, Read, Update, Delete)
- MongoDB integration for data storage
- User-friendly Tkinter GUI
- Easily create an executable (.exe) application for Windows
- Simple setup and clear instructions

---

## 🛠️ Requirements

- Python 3.x
- [MongoDB](https://www.mongodb.com/try/download/shell)
- [MongoDB Compass (GUI, optional)](https://downloads.mongodb.com/compass/mongodb-compass-1.42.0-win32-x64.exe)

**Python Dependencies:**
```bash
pip install tk
pip install pymongo
pip install PyInstaller
```

---

## 🏗️ Setup Instructions

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/HarshShinde0/Student-Management-System
    cd Student-Management-System
    ```

2. **Install Python Dependencies:**
    ```bash
    pip install tk pymongo pyinstaller
    ```

3. **Download and Install MongoDB:**
    - [Download MongoDB Shell](https://downloads.mongodb.com/compass/mongosh-2.1.4-win32-x64.zip)
    - [Download MongoDB Compass (optional)](https://downloads.mongodb.com/compass/mongodb-compass-1.42.0-win32-x64.exe)
    - Or use [MongoDB Atlas Cloud](https://cloud.mongodb.com/)

4. **Configure MongoDB:**
    - Start your MongoDB server locally or connect to Atlas.
    - Update the connection string in the Python code if needed.

5. **Run the Application:**
    ```bash
    python app.py
    ```

---

## 📦 Create an Executable Application

You can convert the Python app into a Windows executable:

- **With Terminal Window:**
    ```bash
    python -m PyInstaller app.py --onefile
    ```
- **Without Terminal Window:**
    - Change the file extension to `.pyw` (e.g., `app.pyw`).
    - Run:
      ```bash
      python -m PyInstaller app.pyw --onefile
      ```
    - This version will not show a terminal window.

The generated executable will be located in the `dist` folder.

---

## 📁 Repository

**GitHub Project Link:**  
[https://github.com/HarshShinde0/Student-Management-System](https://github.com/HarshShinde0/Student-Management-System)

An already built executable application is also provided in the repo for testing.

---

---
- **YouTube:** [Tutorial Video](https://youtu.be/PCo9FDCbsEM)

---

## 🙏 Credits

Created by Harsh 
