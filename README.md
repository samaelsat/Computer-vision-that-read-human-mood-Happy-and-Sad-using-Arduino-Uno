Facial Expression Detection with Arduino LCD Display

A real-time facial expression detection system that uses computer vision to detect emotions and displays them on an LCD screen via Arduino.
🎯 Overview
This project combines Python-based facial landmark detection with Arduino hardware to create an interactive emotion recognition system. The system analyzes facial expressions through webcam input and displays corresponding emotions ("Happy" or "Sad") on a 16x2 I2C LCD display.
🔧 Hardware Requirements

Arduino board (Uno/Nano/Mega)
16x2 I2C LCD Display (address: 0x27)
Webcam
USB cable for Arduino connection
Jumper wires

LCD Connections

VCC → 5V
GND → GND
SDA → A4 (Uno/Nano) or SDA pin
SCL → A5 (Uno/Nano) or SCL pin

📦 Software Requirements
Python Dependencies
bashpip install opencv-python mediapipe pyserial
Arduino Libraries

Wire.h (built-in)
LiquidCrystal_I2C.h (Download here)

🚀 How It Works

Face Detection: MediaPipe's Face Mesh detects facial landmarks in real-time
Distance Calculation: Measures the distance between two key facial points (landmarks 306 and 61)
Expression Classification:

Distance > 55 pixels → Happy expression → Sends 'A' to Arduino
Distance < 55 pixels → Sad expression → Sends 'B' to Arduino


Display Output: Arduino receives the signal and displays the corresponding emotion on the LCD

📁 Project Structure
facial-expression-lcd/
├── emotion_detection.py    # Python script for face detection
├── arduino_lcd.ino         # Arduino code for LCD display
└── README.md              # This file
⚙️ Installation & Setup
1. Arduino Setup

Install the LiquidCrystal_I2C library in Arduino IDE
Upload arduino_lcd.ino to your Arduino board
Connect the I2C LCD to the Arduino as per the wiring diagram
Note the COM port your Arduino is connected to

2. Python Setup

Install required Python packages:

bash   pip install opencv-python mediapipe pyserial

Update the serial port in emotion_detection.py:

python   arduino = serial.Serial("COM5", 9600)  # Change COM5 to your port
3. Run the System

Make sure Arduino is connected and running
Run the Python script:

bash   python emotion_detection.py

Position your face in front of the webcam
Watch the LCD display update based on your expression!

🎮 Usage

Press 'q' to quit the application
The webcam window shows:

Red circles at detected facial landmarks
Blue line connecting the measurement points
Real-time distance values in console



🔍 Troubleshooting
Arduino Issues

LCD shows nothing: Check I2C address (try 0x3F if 0x27 doesn't work)
Random characters: Verify power supply and connections
Serial connection failed: Check COM port and close other serial monitors

Python Issues

No face detected: Ensure good lighting and face the camera directly
Serial connection error: Update the COM port in code
Import errors: Reinstall packages with pip install --upgrade

📊 Customization
Adjust Detection Sensitivity
Modify the distance threshold in Python code:
pythonif distance > 55:  # Change this value
    arduino.write(b"A")
elif distance < 55:  # And this value
    arduino.write(b"B")
Add More Expressions

Add new conditions in Python with different distance ranges
Send different characters (C, D, E, etc.)
Add corresponding cases in Arduino code

Change LCD Messages
Edit the Arduino code:
cppif (c == 'A') {
    lcd.print("Custom Message");
}
🤝 Contributing
Feel free to fork this project and submit pull requests for improvements!
📝 License
This project is open source and available for educational purposes.
🙏 Acknowledgments

MediaPipe by Google for facial landmark detection
OpenCV community for computer vision tools
LiquidCrystal_I2C library contributors
