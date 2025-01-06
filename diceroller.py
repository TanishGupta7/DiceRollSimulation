import tkinter as tk
from PIL import Image, ImageTk
import random
import winsound  # For playing sound on Windows
import time

# Initialize the main window
window = tk.Tk()
window.geometry("800x500")
window.title("Dice Roll")
window.config(bg="#2E2E2E")

# Create a frame for the dice roll area
dice_frame = tk.Frame(window, bg="#2E2E2E")
dice_frame.place(relwidth=0.7, relheight=1)

# Create a frame for the control area (history, dice size, etc.)
control_frame = tk.Frame(window, bg="#3C3C3C", width=250)
control_frame.place(relx=0.7, relheight=1, relwidth=0.3)

# List of dice images
dice = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png"]

# Initial Dice Size
dice_size = 100

# History of rolls (Last 5 rolls)
roll_history = []

# Roll Counter
roll_count = 0

# Function to load and resize images
def load_and_resize(image_path):
    image = Image.open(image_path)
    return ImageTk.PhotoImage(image.resize((dice_size, dice_size)))

# Create labels to display images
image1 = load_and_resize(random.choice(dice))
image2 = load_and_resize(random.choice(dice))

label1 = tk.Label(dice_frame, image=image1, bg="#2E2E2E")
label2 = tk.Label(dice_frame, image=image2, bg="#2E2E2E")

label1.image = image1
label2.image = image2

# Position the labels in the dice frame
label1.place(x=100, y=100)
label2.place(x=300, y=100)

# Roll Counter Label in control frame
counter_label = tk.Label(control_frame, text=f"Roll Count: {roll_count}", bg="#3C3C3C", fg="white", font=("Arial", 14))
counter_label.pack(pady=10)

# History Label in control frame
history_label = tk.Label(control_frame, text="History: ", bg="#3C3C3C", fg="white", font=("Arial", 12))
history_label.pack(pady=10)

# Function to update dice images on button click
def dice_roll():
    global roll_count, dice_size, roll_history
    
    roll_count += 1
    counter_label.config(text=f"Roll Count: {roll_count}")
    
    # Add current roll to history (max 5)
    roll_history.insert(0, f"Roll {roll_count}: {random.randint(1, 6)}-{random.randint(1, 6)}")
    roll_history = roll_history[:5]  # Limit to last 5 rolls
    
    # Update History
    history_display = "\n".join(roll_history)
    history_label.config(text=f"History:\n{history_display}")
    
    # Play sound effect when the dice roll happens
    winsound.Beep(500, 200)  # Beep sound (you can add custom sound files here if needed)
    
    # Change background color based on dice result
    dice1_roll = random.randint(1, 6)
    dice2_roll = random.randint(1, 6)
    if dice1_roll == 6 and dice2_roll == 6:
        window.config(bg="green")  # Winning combination
    else:
        window.config(bg="#2E2E2E")
    
    # Animated Dice Roll - Change dice images briefly before showing result
    for _ in range(5):  # Quick transitions
        temp_image1 = load_and_resize(random.choice(dice))
        temp_image2 = load_and_resize(random.choice(dice))
        label1.configure(image=temp_image1)
        label2.configure(image=temp_image2)
        window.update()
        time.sleep(0.1)  # Pause between transitions
    
    # Show the final result
    final_image1 = load_and_resize(dice[dice1_roll - 1])
    final_image2 = load_and_resize(dice[dice2_roll - 1])
    
    label1.configure(image=final_image1)
    label2.configure(image=final_image2)

    # Keep the reference to the images
    label1.image = final_image1
    label2.image = final_image2

# Slider for Customizable Dice Size
def update_dice_size(val):
    global dice_size
    dice_size = int(val)
    new_image1 = load_and_resize(random.choice(dice))
    new_image2 = load_and_resize(random.choice(dice))
    label1.configure(image=new_image1)
    label2.configure(image=new_image2)
    label1.image = new_image1
    label2.image = new_image2

# Add the slider to control dice size in control frame
size_slider = tk.Scale(control_frame, from_=50, to=200, orient="horizontal", label="Dice Size", bg="#3C3C3C", fg="white", font=("Arial", 12))
size_slider.set(100)  # Default size
size_slider.pack(pady=10)
size_slider.bind("<Motion>", lambda event: update_dice_size(size_slider.get()))

# Style the Roll Button in control frame
button = tk.Button(control_frame, text="ROLL", bg="#FF6347", fg="white", font=("Arial", 16, "bold"), command=dice_roll, relief="solid", bd=2)
button.pack(pady=20)

# Run the window
window.mainloop()
