import os
import cv2
import sys

# Capture and write video from camere using OpenCV

VIDEO_OUTPUT_PATH = os.path.abspath(os.path.join(os.getcwd(), "output"))

cam_indx = 0  # default camera device index
if len(sys.argv) > 1:
    cam_indx = int(sys.argv[1])

cam = cv2.VideoCapture(cam_indx)

if not cam.isOpened():
    print(f"Error: Cannot open camera index {cam_indx}")
    sys.exit(1)

frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(f"{VIDEO_OUTPUT_PATH}/output.mp4", fourcc, 20.0,
                      (frame_width, frame_height))

while True:
    has_frame, frame = cam.read()

    if not has_frame:
        print("No frame found while capturing video")
        break

    frame = cv2.flip(frame, 1)
    out.write(frame)
    cv2.imshow("Camera Preview", frame)

    if cv2.waitKey(1) == ord('q'):
        break


cam.release()
out.release()
cv2.destroyAllWindows()
