import os
import cv2
import sys

# Capture and write video from camere using OpenCV

VIDEO_OUTPUT_PATH = os.path.abspath(os.path.join(os.getcwd(), "output"))

source_indx = 0  # default sourceera device index
if len(sys.argv) > 1:
    source_indx = int(sys.argv[1])

source = cv2.VideoCapture(source_indx)

if not source.isOpened():
    print(f"Error: Cannot open camera index {source_indx}")
    sys.exit(1)

frame_width = int(source.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(source.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(f"{VIDEO_OUTPUT_PATH}/output.mp4", fourcc, 20.0,
                      (frame_width, frame_height))

while True:
    has_frame, frame = source.read()

    if not has_frame:
        print("No frame found while capturing video")
        break

    frame = cv2.flip(frame, 1)  # mirror effect on the sourceera
    out.write(frame)
    cv2.imshow("Camera Preview", frame)

    if cv2.waitKey(1) == ord('q'):
        break


source.release()
out.release()
cv2.destroyAllWindows()
