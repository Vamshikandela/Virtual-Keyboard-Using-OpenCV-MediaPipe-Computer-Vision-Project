# Virtual-Keyboard-Using-OpenCV-MediaPipe-Computer-Vision-Project
## 🖐️ Virtual Keyboard Using Hand Gestures (Single Touch)
## 📌 Project Description

This project implements a virtual keyboard controlled using hand gestures with the help of a webcam. The system tracks the user’s index finger tip and allows typing by hovering over a key for a fixed delay, eliminating the need for a physical keyboard.

The application is built using OpenCV, MediaPipe (via CVZone), and pynput, and provides real-time visual feedback along with audio click sounds using the built-in winsound module.

## 🎯 Key Features

Real-time hand tracking using webcam

On-screen QWERTY-style virtual keyboard

Single-touch typing logic with delay control

Backspace (<<) and Space (SPACE) key support

Live text display area

Visual hover and press effects

Audio feedback on each key press (Windows)

## 🎮 Controls & Gestures
## 🖥️ Gesture Controls
### Action	Gesture
   Hover on key	Move index finger tip over a key
   Type character	Keep finger over key for 2 seconds
   Backspace	Hover over << key
   Space	Hover over SPACE key
   Exit program	Press q on physical keyboard

📌 Typing is based on time delay (pressDelay = 2 seconds) to prevent accidental presses.

## 🚀 How to Run the Project


   1️⃣  Create Virtual Environment
    py -3.10 -m venv venv
    venv\Scripts\activate   # Windows

 2️⃣ Install Required Dependencies
pip install opencv-python cvzone mediapipe pynput numpy

 3️⃣Run the Application
python Virk.py


📌 Ensure your webcam is enabled and properly positioned.

## 📦 Required Modules & Supported Versions
### Module	Supported Version
   Python	3.9 – 3.11
   opencv-python==4.8.1.78
   cvzone==1.5.6
   mediapipe==0.10.9
   numpy==1.24.4
   pynput==1.7.6

⚠️ winsound works only on Windows OS.

## 🧠 How It Works (Code Logic)

Webcam captures real-time video frames

Hand landmarks are detected using CVZone HandDetector

Index finger tip (landmark 8) is tracked

Finger position is checked against key boundaries

If finger stays on a key for 2 seconds, the key is triggered

Key press is simulated using pynput.keyboard.Controller

Typed text is displayed on screen

Sound feedback is played using winsound.Beep()

## ⌨️ Keyboard Layout Used
Q W E R T Y U I O P
A S D F G H J K L <<
Z X C V B N M SPACE


<< → Backspace

SPACE → Space bar
## 📁 Project Structure
📦 virtual-keyboard-hand-gesture
┣ 📜 Virk.py
┣ 📜 README.md
┗ 🎥 working_demo.mp4

## ⚠️ Limitations

Typing speed depends on delay timing

Works best in good lighting conditions

Designed for single-hand usage only

Windows-only sound feedback

## 🔮 Future Improvements

Adjustable typing delay

Multi-hand support

Gesture-based click instead of time delay

Mobile camera support

Improved UI design

## 👤 Author

Vamshi Kandela
Aspiring Data Analyst & Computer Vision Enthusiast

## ⭐ Acknowledgements

OpenCV Community

MediaPipe by Google

CVZone Library
