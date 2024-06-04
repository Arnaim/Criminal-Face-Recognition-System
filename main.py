import face_recognition
import cv2
import numpy as np
import winsound
import customtkinter as ctk
from tkinter import messagebox

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

# Function to handle panic button
def panic_button():
    messagebox.showwarning("Panic Button", "Authorities have been alerted!")


# Function to handle panic button with a beeping sound
def panic_button():
    # Play a beeping sound
    winsound.Beep(1500, 1000)  # Beep at 1000 Hz for 500 milliseconds
    messagebox.showwarning("Panic Button", "Authorities have been alerted!")    

# Create the main window
root = ctk.CTk()
root.title("Face Recognition")
root.geometry("800x600")  # Set the window size

# Create the GUI elements
title_label = ctk.CTkLabel(root, text="Face Recognition System", font=("Arial", 24))
title_label.pack(pady=20)

capture_button = ctk.CTkButton(root, text="Capture Live Image and Compare", command=compare_faces, font=("Arial", 18))
capture_button.pack(pady=20)

result_label = ctk.CTkLabel(root, text="", font=("Arial", 18))
result_label.pack(pady=20)

# Add a slider to adjust the sensitivity for matching faces
sensitivity_label = ctk.CTkLabel(root, text="Matching Sensitivity:", font=("Arial", 14))
sensitivity_label.pack(pady=10)

sensitivity_slider = ctk.CTkSlider(root, from_=0.1, to=1.0, orientation='horizontal', command=update_sensitivity)
sensitivity_slider.set(0.6)  # Initial sensitivity value
sensitivity_slider.pack(pady=10)

# Create a label to display the current sensitivity value
sensitivity_value_label = ctk.CTkLabel(root, text=f"Sensitivity: {sensitivity_slider.get():.2f}", font=("Arial", 14))
sensitivity_value_label.pack(pady=10)

# Add the instructions button
instructions_button = ctk.CTkButton(root, text="Instructions", command=show_instructions, font=("Arial", 18))
instructions_button.pack(pady=10)

# Add the panic button
panic_button = ctk.CTkButton(root, text="Panic Button", command=panic_button, font=("Arial", 18), fg_color="red", text_color="white")
panic_button.pack(pady=10)

# Run the main loop
root.mainloop()
