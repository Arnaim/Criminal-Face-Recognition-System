import tkinter as tk
from tkinter import ttk

class CriminalFaceRecognitionApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Criminal Face Recognition")
        self.geometry("600x400")
        self.configure(bg="#3a3d9f")

        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = tk.Label(self, text="Criminal Face Recognition", font=("Helvetica", 24, "bold"), fg="white", bg="#3a3d9f")
        title_label.pack(pady=20)

        # Capture & Compare button
        capture_frame = tk.Frame(self, bg="#3a3d9f")
        capture_frame.pack(pady=10)
        capture_button = tk.Button(capture_frame, text="Capture & compare", font=("Helvetica", 14), bg="#5a5ddf", fg="white", relief="flat", width=20)
        capture_button.pack()

        # Matching Sensitivity
        sensitivity_frame = tk.Frame(self, bg="#3a3d9f")
        sensitivity_frame.pack(pady=20)
        sensitivity_label = tk.Label(sensitivity_frame, text="MATCHING SENSITIVITY", font=("Helvetica", 12), fg="white", bg="#3a3d9f")
        sensitivity_label.pack()
        
        self.sensitivity_scale = tk.Scale(sensitivity_frame, from_=0.0, to=1.0, orient="horizontal", resolution=0.1, length=300, bg="#3a3d9f", fg="white", troughcolor="#5a5ddf")
        self.sensitivity_scale.set(0.60)
        self.sensitivity_scale.pack()

        # Sensitivity Value
        sensitivity_value_label = tk.Label(sensitivity_frame, text="Sensitivity : 0.60", font=("Helvetica", 12), fg="white", bg="#3a3d9f")
        sensitivity_value_label.pack()

        # Update sensitivity value
        self.sensitivity_scale.bind("<Motion>", lambda event: self.update_sensitivity_value(sensitivity_value_label))

    def update_sensitivity_value(self, label):
        sensitivity_value = self.sensitivity_scale.get()
        label.config(text=f"Sensitivity : {sensitivity_value:.2f}")

if __name__ == "__main__":
    app = CriminalFaceRecognitionApp()
    app.mainloop()
