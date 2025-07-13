import numpy as np
import cv2

"""
    THEORY:
    
        Edge:
            In math terms, edges are where the gradient (change) of intensity is large.
        
        Corner:
            A point where intensity changes in both X and Y directions.
            Imagine sliding a window over:
                - Flat area -> values stay same -> not a corner
                - Edge -> changes in 1 direction -> not a corner
                - Corner -> changes in both directions
                
        Filter (Kernel)
            A kernel is a small matrix (like 3x3 or 5x5) that you slide over an image to apply some operation (e.g., blur, sharpen, detect edges).
            We apply it using convolution: multiply each kernel value with the corresponding pixel under it, sum the results, and put that value in the output image.

        1, cv2.GaussianBlur() 
            - Smooths an image by reducing noise and small details.
	        - Blends each pixel with its neighbors using a weighted average.
	        - Keeps the image edges soft and natural-looking.
         

        2. cv2.Canny() — Edge Detection

            Finds edges — locations in the image where pixel intensity changes sharply.

            Steps:
                1.	Convert to grayscale
                2.	Apply Gaussian blur to reduce noise
                3.	Compute gradients with Sobel filters (kernels):
                    - Gx = ∂I/∂x, Gy = ∂I/∂y
                    - Gradient magnitude: G = √(Gx² + Gy²)
                4.	Non-Maximum Suppression: keeps only strongest edges
                5.	Double Threshold: classifies pixels as strong/weak/no edge
                6.	Edge Tracking by Hysteresis: keeps weak edges connected to strong ones
                
            Key formula:
                G = √(Gx² + Gy²)
                θ = arctan(Gy / Gx) 
                
        3. cv2.goodFeaturesToTrack() — Corner Detection (Shi-Tomasi)
        
            Finds corners — points where intensity changes in both X and Y directions (good for tracking).

            Steps:
                1.	Compute image gradients: Ix, Iy
                2.	Build structure matrix M over each local window:
                    M = [ ∑Ix²   ∑IxIy ]
                        [ ∑IxIy  ∑Iy²  ]
                3.	Compute eigenvalues of M: λ₁, λ₂
                4.	Corner score: score = min(λ₁, λ₂)
                5.	Keep strongest corners based on score
                
            Key Formula:
                score = min(λ₁, λ₂)
    
"""

PREVIEW = 0  # Preview Mode
BLUR = 1  # Blurring Filter
GAUSSIAN_BLUR = 2  # Gaussian Blur (Filter function)
CANNY = 3  # Canny Edge Detector
FEATURES = 4  # Corner Feature Detector


feature_params = dict(maxCorners=500, qualityLevel=0.2,
                      minDistance=15, blockSize=9)

image_filter = PREVIEW
win_name = "Camera Filters"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

result_frame = None

source = cv2.VideoCapture(0)
source.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
source.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
print("Starting video capturing...")

while True:
    has_frame, frame = source.read()

    if not has_frame:
        print("No frame found")
        break

    frame = cv2.flip(frame, 1)

    if image_filter == PREVIEW:
        result_frame = frame
    elif image_filter == BLUR:
        result_frame = cv2.blur(frame, (20, 20))
    elif image_filter == GAUSSIAN_BLUR:
        result_frame = cv2.GaussianBlur(frame, (27, 27), 5)
    elif image_filter == CANNY:
        result_frame = cv2.Canny(frame, 50, 150)
    elif image_filter == FEATURES:
        result_frame = frame
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(frame_gray, **feature_params)
        if corners is not None:
            """
                Example:    
                    corners = np.array([
                        [[123.4, 80.7]],
                        [[150.9, 90.2]],
                        [[180.3, 110.5]]
                    ])
                    Its shape is: (3, 1, 2)
                        - 3:  number of corners (→ N)
                        - 1:  unnecessary nesting
                        - 2:  [x, y]

                    corners.reshape(-1, 2) => Shape becomes (3, 2)
                    -> [
                        [123.4, 80.7],
                        [150.9, 90.2],
                        [180.3, 110.5]
                    ]
            """
            for x, y in np.uint32(corners).reshape(-1, 2):
                cv2.circle(result_frame, (x, y), 10, (0, 255, 0), 1)

    cv2.imshow(win_name, result_frame)

    # image filter switch keys
    key = cv2.waitKey(1)
    if key == ord("Q") or key == ord("q") or key == 27:
        break
    elif key == ord("C") or key == ord("c"):
        image_filter = CANNY
    elif key == ord("B") or key == ord("b"):
        image_filter = BLUR
    elif key == ord("G") or key == ord("g"):
        image_filter = GAUSSIAN_BLUR
    elif key == ord("F") or key == ord("f"):
        image_filter = FEATURES
    elif key == ord("P") or key == ord("p"):
        image_filter = PREVIEW


source.release()
print("source released")
