# Virtual-Keyboard-Using-OpenCV-MediaPipe-Computer-Vision-Project
## 🖐️ Virtual Keyboard Using Hand Gestures (Single Touch)
## 📌 Project Description

This project implements a virtual keyboard controlled using hand gestures with the help of a webcam. The system tracks the user’s index finger tip and allows typing by hovering over a key for a fixed delay, eliminating the need for a physical keyboard.

The application is built using OpenCV, MediaPipe (via CVZone), and pynput, and provides real-time visual feedback along with audio click sounds using the built-in winsound module.

## 💼 Business Problem

Traditional physical keyboards are not always practical or accessible in modern computing environments. Users working in touchless, hygienic, or assistive environments—such as healthcare facilities, public kiosks, AR/VR systems, or individuals with physical impairments—face challenges using conventional input devices.

Additionally, increasing demand for gesture-based and contactless interfaces highlights the need for low-cost, camera-based alternatives. Existing solutions often require specialized hardware, making them expensive and difficult to deploy at scale.

## 🎯 Business Objective

The objective of this project is to design a cost-effective, touchless virtual keyboard using computer vision that enables users to type using simple hand gestures. The solution aims to:

Reduce dependency on physical keyboards

Improve accessibility for differently-abled users

Enable hygienic, contact-free interaction

Provide a scalable input method for smart systems

## 🏢 Use Cases

Healthcare & Laboratories – Touchless input in sterile environments

Public Kiosks & Smart Displays – Reducing physical contact

Assistive Technology – Supporting users with motor impairments

AR/VR & Metaverse Applications – Gesture-based input systems

Smart Classrooms & Presentations – Interactive human–computer interaction

## 🎯 Key Features

Real-time hand tracking using webcam

On-screen QWERTY-style virtual keyboard

Single-touch typing logic with delay control

Backspace (<<) and Space (SPACE) key support

Live text display area

Visual hover and press effects

Audio feedback on each key press (Windows)

## 🎮 Controls & Gestures
### 🖥️ Gesture Controls
Action	Gesture
- Hover on key	Move index finger tip over a key
- Type character	Keep finger over key for **2** seconds
- Backspace	Hover over << key
- Space	Hover over SPACE key
- Exit program	**Press q** on physical keyboard

📌 Typing is based on time delay (pressDelay = 2 seconds) to prevent accidental presses.

## 🚀 How to Run the Project
1️⃣ Create Virtual Environment
**py -3.10 -m venv venv**
**venv\Scripts\activate**

2️⃣ Install Required Dependencies
pip install opencv-python cvzone mediapipe pynput numpy

3️⃣ Run the Application
python Main.py


📌 Ensure your webcam is enabled and properly positioned.

## 📦 Required Modules & Supported Versions
Module	Supported Version
- Python	3.9 – 3.11
- opencv-python	4.8.1.78
- cvzone	1.5.6
- mediapipe	0.10.9
- numpy	1.24.4
- pynput	1.7.6

⚠️ winsound works only on Windows OS.

## 🧠 How It Works (Code Logic)

- Webcam captures real-time video frames

- Hand landmarks are detected using CVZone HandDetector

- Index finger tip (landmark 8) is tracked

- Finger position is checked against key boundaries

- If finger stays on a **key for 2 seconds**, the key is **triggered**

- Key press is simulated using pynput.keyboard.Controller

- Typed text is displayed on screen

- Sound feedback is played using winsound.Beep()


<img width="563" height="474" alt="image" src="https://github.com/user-attachments/assets/d7066db7-470a-4fe0-a3a4-aa7fcdff4e9c" />


## 📁 Project Structure
- **Main.py**  
  Main Python script containing the virtual keyboard logic using OpenCV, MediaPipe (CVZone), and hand gestures.

- **README.md**  
  Project documentation including description, setup instructions, features, and usage details.

- **working_demo.mp4**  
  Demo video showcasing the real-time working of the virtual keyboard.


## ⚠️ Limitations

- Typing speed depends on delay timing

- Works best in good lighting conditions

- Designed for single-hand usage only

- Windows-only sound feedback

## 🔮 Future Improvements

- Adjustable typing delay

- Multi-hand support

- Gesture-based click instead of time delay

- Mobile camera support

- Improved UI design

## 👤 Author

**Vamshi Kandela**
**Aspiring Data Scientist & Computer Vision Enthusiast**

## ⭐ Acknowledgements

OpenCV Community

MediaPipe by Google

CVZone Library
