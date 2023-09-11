import face_recognition
import cv2
import imutils
import pickle
 
# Load trained data
with open("trained_faces.dat", "rb") as file:
    known_face_encodings, known_face_names = pickle.load(file)
 
# Initialize the camera
video_capture = cv2.VideoCapture(-1, cv2.CAP_V4L)
 
# Ensure the camera is properly initialized
if not video_capture.isOpened():
    print("Could not open camera")
    exit()
 
skip_frames = 12
frame_count = 0
 
while True:
    ret, frame = video_capture.read()
    frame_count += 1
 
    if frame_count % skip_frames == 0:
        frame = imutils.resize(frame, width=400)
 
        # Find all face locations and face encodings in the current frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
 
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Not Known"
 
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
 
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)
 
        cv2.imshow('Video', frame)
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
video_capture.release()
cv2.destroyAllWindows()