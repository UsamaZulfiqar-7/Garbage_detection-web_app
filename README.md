Face Attendance System (Computer Vision Project)
📌 Project Overview

The Face Attendance System is a Computer Vision project that automatically marks student attendance using real-time face recognition.
The system detects faces through a live camera, recognizes registered students from a local dataset, and saves attendance with date and time in an Excel file.

🎯 Project Objectives

Detect faces using Computer Vision

Recognize registered students in real time

Automatically mark attendance without manual entry

Store attendance in an organized Excel file

Reduce human effort in attendance management

⚙️ Features

Live camera-based face detection

Automatic face recognition of registered students

Real-time attendance marking

Saves Name, Date, and Time in Excel

Simple and automated system

📂 Dataset Structure

A folder named datasets already exists in the project. Inside it, create separate folders for each student and add their images.

datasets/
│
├── Aliyan/
│   ├── img1.jpg
│   ├── img2.jpg
│
├── Noor/
│   ├── img1.jpg
│   ├── img2.jpg
│
└── Usama/
    ├── img1.jpg
    └── img2.jpg

Important: Each folder name must exactly match the student’s name because this name will be used in the attendance file.

🧠 Technologies Used

Python

OpenCV

face_recognition library

NumPy

Pandas

Excel (attendance.xlsx)

VS Code (Development Environment)

▶️ How to Run the Project
Step 1: Clone the Repository
git clone <your-repository-link>
cd face-attendance-system
Step 2: Install Dependencies
pip install opencv-python numpy pandas face-recognition
Step 3: Add Dataset

Place student images inside:

datasets/
Step 4: Run the Project
python attendance.py

The camera will open automatically and start marking attendance.

📊 Attendance Output

Attendance is saved in:

attendance.xlsx

Example format:

Name	Date	Time
Aliyan	2025-02-10	09:15 AM
Noor	2025-02-10	09:17 AM
Usama	2025-02-10	09:20 AM
👨‍💻 Author

Rana Usama
Computer Vision Project

📄 Note

The dataset is not included in the repository for privacy reasons.
You must add your own images inside the datasets folder before running the system.

📜 License

This project is for educational purposes only.
