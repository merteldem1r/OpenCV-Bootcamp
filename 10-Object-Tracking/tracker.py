from IPython.display import YouTubeVideo, display, HTML
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
import os
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

print("Current opencv version: ", cv2.__version__)


DATA_RAW_PATH = os.path.abspath(os.path.join(
    os.getcwd(), "data/raw"))
DATA_OUTPUT_PATH = os.path.abspath(os.path.join(os.getcwd(), "data/output"))
MODELS_PATH = os.path.abspath(os.path.join(os.getcwd(), "models"))

video_input_file_path = f"{DATA_RAW_PATH}/race_car.mp4"

# Tracker & Tracker type
MIL = "MIL"
GOTURN = "GOTURN"
NANO = "NANO"
VIT = "VIT"

tracker_type = None  # or set from user input
tracker = None

# utility functions


def draw_rectangle(frame, bbox):
    x, y, w, h = [int(v) for v in bbox]
    top_left = (x, y)
    bottom_right = (x + w, y + h)
    cv2.rectangle(frame, top_left, bottom_right, (0, 0, 255), 2, cv2.LINE_AA)


def draw_text(frame, text, location, color=(50, 170, 59)):
    cv2.putText(frame, text, location,
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, color, 2)


# open video & capture first frame for roi selection (object rectangle box)
video = cv2.VideoCapture(video_input_file_path)

if not video.isOpened():
    print("Error while opening video file.")
    sys.exit()
else:
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps_input = int(video.get(cv2.CAP_PROP_FPS))

video_output_file_name = f"{DATA_OUTPUT_PATH}/race_car-{tracker_type}.mp4"
video_out = cv2.VideoWriter(
    video_output_file_name, cv2.VideoWriter_fourcc(*'mp4v'), fps_input, (width, height))


video_out = cv2.VideoWriter(
    video_output_file_name,
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps_input,
    (width, height)
)

has_frame, frame = video.read()
original_frame = frame.copy()

if not has_frame:
    print("Error: on startup frame read.")
    sys.exit()

selector_frame = original_frame.copy()
# Select Tracker mode
while tracker_type == None:
    cv2.imshow("Tracker Selector", selector_frame)
    key = cv2.waitKey(1)

    draw_text(selector_frame, "Select Tracker Mode Q: ",
              (80, 140), color=(255, 0, 0))
    draw_text(selector_frame, "M: MIL",
              (100, 200), color=(255, 0, 0))
    draw_text(selector_frame, "G: GOTURN",
              (100, 260), color=(255, 0, 0))
    draw_text(selector_frame, "N: NANO",
              (100, 380), color=(255, 0, 0))
    draw_text(selector_frame, "V: VIT",
              (100, 440), color=(255, 0, 0))

    if key == ord("Q") or key == ord("q") or key == 27:
        sys.exit()
    elif key == ord("M") or key == ord("m"):
        tracker_type = MIL
    elif key == ord("G") or key == ord("g"):
        tracker_type = GOTURN
    elif key == ord("N") or key == ord("n"):
        tracker_type = NANO
    elif key == ord("V") or key == ord("v"):
        tracker_type = VIT

if tracker_type == MIL:
    tracker = cv2.TrackerMIL.create()
elif tracker_type == GOTURN:
    tracker_params = cv2.TrackerGOTURN().Params()
    tracker_params.modelBin = f"{MODELS_PATH}/goturn/goturn.caffemodel"
    tracker_params.modelTxt = f"{MODELS_PATH}/goturn/goturn.prototxt"
    tracker = cv2.TrackerGOTURN.create(tracker_params)
elif tracker_type == NANO:
    tracker_params = cv2.TrackerNano().Params()
    tracker_params.neckhead = f"{MODELS_PATH}/nano/nanotrack_head_sim.onnx"
    tracker_params.backbone = f"{MODELS_PATH}/nano/nanotrack_backbone_sim.onnx"
    tracker = cv2.TrackerNano.create(tracker_params)
elif tracker_type == VIT:
    model_path = f"{MODELS_PATH}/vit/object_tracking_vittrack_2023sep_int8bq.onnx"
    vit_net = cv2.dnn.readNet(model_path)
    tracker = cv2.TrackerVit.create(vit_net)

    if vit_net.empty():
        print("Error loading ViT model!")
        sys.exit()
else:
    print(f"Tracker type '{tracker_type}' is not recognized.")
    sys.exit(1)

# Select ROI
roi_frame = original_frame.copy()
draw_text(roi_frame, "Select ROI: Object box wanted to track",
          (80, 140), color=(255, 0, 0))
draw_text(roi_frame, "and press Enter",
          (80, 200), color=(255, 0, 0))
roi = cv2.selectROI("tracker", roi_frame)

if roi == (0, 0, 0, 0):
    print("ROI not selected properly.")
    sys.exit()

cv2.destroyWindow("tracker")
ok = tracker.init(roi_frame, roi)

while True:
    has_frame, frame = video.read()

    if not has_frame:
        print("Error during frame capture")
        break

    start_time = cv2.getTickCount()

    has_roi, roi = tracker.update(frame)

    if has_roi:
        draw_rectangle(frame, roi)
    else:
        draw_text(frame, "Tracking failure", (80, 140), color=(0, 0, 255))

    cv2.rectangle(frame, roi, (255, 0, 0), 2, cv2.LINE_AA)

    end_time = cv2.getTickCount()
    time_passed = (end_time - start_time) / cv2.getTickFrequency()
    fps = 1 / time_passed if time_passed > 0 else 0

    # Display Info
    draw_text(frame, f"{tracker_type}Tracker", (80, 60))
    draw_text(frame, f"FPS : {int(fps)}", (80, 100))

    cv2.imshow("Tracking", frame)

    video_out.write(frame)

    key = cv2.waitKey(1)
    if key == 27:  # ESC key
        break

video.release()
video_out.release()
cv2.destroyAllWindows()
print("Tracking done")
