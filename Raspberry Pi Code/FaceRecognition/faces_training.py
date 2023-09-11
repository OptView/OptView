import face_recognition
import os
import pickle
 
# Load known faces and their names
known_face_encodings = []
known_face_names = []
 
# Path to the dataset directory
dataset_path = "dataset"
 
# Iterate through each person's folder in the dataset directory
for person_name in os.listdir(dataset_path):
    person_folder = os.path.join(dataset_path, person_name)
    
    # Ensure we're looking at a directory
    if os.path.isdir(person_folder):
        for filename in os.listdir(person_folder):
            if filename.endswith(".jpg"):  # Ensure we're only processing .jpg files
                image_path = os.path.join(person_folder, filename)
                image = face_recognition.load_image_file(image_path)
                encodings = face_recognition.face_encodings(image)
                
                # Check if a face is detected
                if encodings:
                    known_face_encodings.append(encodings[0])
                    known_face_names.append(person_name)
                    print(f"Face detected in {image_path}. Saving this image.")
                else:
                    print(f"No face detected in {image_path}. Skipping this image.")
            else:
                print(f"Image {image_path} should be on jpg format")

# Save the trained data for later use
with open("trained_faces.dat", "wb") as file:
    pickle.dump((known_face_encodings, known_face_names), file)
 
print("Training complete. Data saved to trained_faces.dat.")


cv2.destroyAllWindows()

 