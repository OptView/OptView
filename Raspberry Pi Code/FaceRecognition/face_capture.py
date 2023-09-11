import cv2
import os
 
# Get the person's name and create a directory for them inside the "dataset" folder
person_name = input("Enter the person's name: ")
folder_path = os.path.join("dataset", person_name)
 
# Create the "dataset" directory if it doesn't exist
if not os.path.exists("dataset"):
    os.makedirs("dataset")
 
# Create the person's directory inside "dataset" if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
 
# Initialize the camera
camera = cv2.VideoCapture(-1, cv2.CAP_V4L)
 
# Ensure the camera is properly initialized
if not camera.isOpened():
    print("Could not open camera")
    exit()
 
image_counter = 0
 
while True:
    ret, frame = camera.read()
    if not ret:
        print("Failed to grab frame")
        break
    
    # Display the live video feed
    cv2.imshow(f'Press SPACE to capture an image for {person_name}', frame)
 
    key = cv2.waitKey(1)
 
    # Check if SPACE key is pressed
    if key == 32:  # 32 is the ASCII value for SPACE
        filename = os.path.join(folder_path, f"{person_name}_{image_counter}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Image saved as {filename}")
        image_counter += 1
    elif key == 27:  # 27 is the ASCII value for ESC
        break
 
camera.release()