import face_recognition
import cv2
import numpy as np
import tkinter as tk
from tkinter import messagebox, ttk
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load the pre-listed image with a raw string literal
image_path = r'img.jpeg'
image = face_recognition.load_image_file(image_path)
image_encoding = face_recognition.face_encodings(image)[0]

# Define the threshold variable
threshold = 0.6

# Function to capture live image from webcam and compare with pre-listed image
def compare_faces():
    # Initialize webcam capture
    cap = cv2.VideoCapture(0)
    
    while True:
        # Capture a frame from the webcam
        ret, frame = cap.read()
        
        # Find face locations and encodings in the current frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        
        # Compare face encodings with the pre-listed image encoding
        for face_encoding in face_encodings:
            results = face_recognition.compare_faces([image_encoding], face_encoding, tolerance=threshold)
            
            if results[0]:
                result_label.config(text="Faces match!")
            else:
                result_label.config(text="Faces do not match.")
        
        # Display the resulting image
        cv2.imshow('Face Recognition', frame)
        
        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the webcam capture
    cap.release()
    cv2.destroyAllWindows()

# Function to update the sensitivity value
def update_sensitivity(val):
    global threshold
    threshold = float(val)
    sensitivity_value_label.config(text=f"Sensitivity: {threshold:.2f}")

# Function to show instructions
def show_instructions():
    instructions = (
        "1. If you see a criminal, do not approach them.\n"
        "2. Immediately press the panic button.\n"
        "3. Alert the authorities with the location and description.\n"
        "4. Stay safe and keep a safe distance."
    )
    messagebox.showinfo("Instructions", instructions)

# Function to handle panic button with an audio file
def panic_button():
    # Play an audio file
    pygame.mixer.music.load('call911.mp3')  # Replace 'panic_alarm.mp3' with your audio file path
    pygame.mixer.music.set_volume(1.0)  # Set volume to maximum
    pygame.mixer.music.play()
    messagebox.showwarning("Panic Button", "Authorities have been alerted!") 

# Create the main window
class CriminalFaceRecognitionApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Criminal Face Recognition")
        self.geometry("800x600")
        self.configure(bg="#3a3d9f")

        self.create_widgets()

    def create_widgets(self):
        global result_label, sensitivity_value_label
        
        # Title
        title_label = tk.Label(self, text="Face Recognition System", font=("Helvetica", 24, "bold"), fg="white", bg="#3a3d9f")
        title_label.pack(pady=20)

        # Capture & Compare button
        capture_button = tk.Button(self, text="Capture Live Image and Compare", font=("Helvetica", 18), bg="#5a5ddf", fg="white", relief="flat", command=compare_faces)
        capture_button.pack(pady=20)

        # Result Label
        result_label = tk.Label(self, text="", font=("Helvetica", 18), fg="white", bg="#3a3d9f")
        result_label.pack(pady=20)

        # Sensitivity Label
        sensitivity_label = tk.Label(self, text="Matching Sensitivity:", font=("Helvetica", 14), fg="white", bg="#3a3d9f")
        sensitivity_label.pack(pady=10)

        # Sensitivity Slider
        self.sensitivity_scale = tk.Scale(self, from_=0.1, to=1.0, orient="horizontal", resolution=0.01, length=300, bg="#3a3d9f", fg="white", troughcolor="#5a5ddf", command=update_sensitivity)
        self.sensitivity_scale.set(0.6)  # Initial sensitivity value
        self.sensitivity_scale.pack(pady=10)

        # Sensitivity Value Label
        sensitivity_value_label = tk.Label(self, text=f"Sensitivity: {self.sensitivity_scale.get():.2f}", font=("Helvetica", 14), fg="white", bg="#3a3d9f")
        sensitivity_value_label.pack(pady=10)

        # Instructions Button
        instructions_button = tk.Button(self, text="Instructions", font=("Helvetica", 18), bg="#5a5ddf", fg="white", relief="flat", command=show_instructions)
        instructions_button.pack(pady=10)

        # Rounded Panic Button
        panic_button_widget = tk.Button(self, text="Panic Button", font=("Helvetica", 18), bg="red", fg="white", relief="flat", command=panic_button)
        panic_button_widget.pack(pady=10, ipadx=10, ipady=5)
        panic_button_widget.config(borderwidth=2, relief="groove")
        panic_button_widget.config(highlightbackground="red", highlightthickness=2, padx=20, pady=10)

if __name__ == "__main__":
    app = CriminalFaceRecognitionApp()
    app.mainloop()
