import sys
import os
import cv2

MODELS_PATH = os.path.abspath(os.path.join(
    os.getcwd(), "models"))

source = cv2.VideoCapture(0)

if not source.isOpened():
    print("Error while source opening")
    sys.exit()

win_name = "camera_preview"
cv2.namedWindow(win_name)

net = cv2.dnn.readNetFromCaffe(
    f"{MODELS_PATH}/deploy.prototxt", f"{MODELS_PATH}/res10_300x300_ssd_iter_140000_fp16.caffemodel")

# Model parameters
in_width = 300
in_height = 300
# standard mean subtraction for normalization (Caffe style)
mean = [104, 117, 123]
conf_threshold = 0.7  # for sensetivity of detections

while cv2.waitKey(1) != 27:
    has_frame, frame = source.read()
    if not has_frame:
        break
    frame = cv2.flip(frame, 1)
    frame_height = frame.shape[0]
    frame_width = frame.shape[1]

    # Create a 4D blob from a frame.
    # Preprocessing on frame to put it proper format
    # swapRB=False -> Caffe expects BGR, so no channel reordering
    # crop=False -> No center cropping
    blob = cv2.dnn.blobFromImage(
        frame, 1.0, (in_width, in_height), mean, swapRB=False, crop=False)
    # Run a model
    # preparing for inference (Sends the preprocessed blob into the network)
    net.setInput(blob)
    # performing inferene on input image (executes the forward pass, all predictions the model makes)
    detections = net.forward()
    """ 
    detections = 4D NumPy array
    detections.shape = [1, 1, N, 7]:
     	- 1 is the batch size (we only run one image at a time),
        - 1 is the number of classes (face detector = just faces),
        - N is the number of detections (can be 100, 200, etc.),
        - 7 means each detection includes 7 values:
            Each detection is:
                detections[0, 0, i] = [
                    0,           # image_id (always 0 in our case)
                    1,           # class_id (1 for "face")
                    confidence,  # confidence score (0 to 1)
                    x1, y1, x2, y2  # normalized box coords (between 0 and 1)   
                ]
    """

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            x_top_left = int(detections[0, 0, i, 3] * frame_width)
            y_top_left = int(detections[0, 0, i, 4] * frame_height)
            x_bottom_right = int(detections[0, 0, i, 5] * frame_width)
            y_bottom_right = int(detections[0, 0, i, 6] * frame_height)

            cv2.rectangle(frame, (x_top_left, y_top_left),
                          (x_bottom_right, y_bottom_right), (0, 255, 0), 2)

            # put Confidence text and white label box
            label = "Confidence: %.4f" % confidence
            # getTextSize(): Calculates the width and height of a text string
            label_size, base_line = cv2.getTextSize(
                label, cv2.FONT_HERSHEY_SIMPLEX, 1, 1)
            cv2.rectangle(
                frame,
                (x_top_left, y_top_left - label_size[1]),
                (x_top_left + label_size[0], y_top_left + base_line),
                (255, 255, 255),
                cv2.FILLED,
            )
            cv2.putText(frame, label, (x_top_left, y_top_left),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))

    # returns the number of clock ticks taken by net.forward()
    t, _ = net.getPerfProfile()
    inference_time_label = "Inference time: %.2f ms" % (
        t * 1000.0 / cv2.getTickFrequency())

    # put label and black label box
    x_top_left_inf = 25
    y_top_left_inf = 100

    label_size, base_line = cv2.getTextSize(
        inference_time_label, cv2.FONT_HERSHEY_SIMPLEX, 2, 1)
    cv2.rectangle(frame, (x_top_left_inf - 20, y_top_left_inf - label_size[1] - 20),
                  (x_top_left_inf + label_size[0] + 20, y_top_left_inf + base_line + 20), (0, 0, 0), cv2.FILLED)
    cv2.putText(frame, inference_time_label, (x_top_left_inf, y_top_left_inf),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 1)
    cv2.imshow(win_name, frame)

source.release()
cv2.destroyWindow(win_name)
