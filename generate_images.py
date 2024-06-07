import cv2
import os

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Unable to read camera feed')

output_dir = 'output_images'
os.makedirs(output_dir, exist_ok=True)

img_counter = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow('Webcam', frame)

    k = cv2.waitKey(1)

    if k%256 == 27:
        print('Escape hit, closing... ')
        break

    elif k%256 == ord('s'): # 's' key to save the frame
        img_name = os.path.join(output_dir, 'opencv_frame_{}.png' .format(img_counter))
        cv2.imwrite(img_name, frame)
        print(f"{img_name} written!") 
        img_counter += 1

cap.release()
cv2.destroyAllWindows()