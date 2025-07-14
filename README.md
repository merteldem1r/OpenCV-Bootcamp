## OpenCV Core

Core concepts & implementations of OpenCV library to manipulate images and videos, and detect objects and faces, among other topics.

- **Course**: [OpenCV University](https://opencv.org/university/)
- **Implemented by**: [Mert Eldemir](https://github.com/merteldem1r)

**NOTE**: To manipulate code and see the results first download the respective images and documents. On each moduel folder run the `download_assets.py` script

### Module 1: Getting Started With Images

- Reading & Display images using **opencv** and **matplotlib**
- Representing images as **numpy arrays** & **RGB** & **HSV** format images
- **cv2**: `imread()` `imwrite()` `cvtColor()` `split()` `merge()`

  - File: [image-handling.ipynb](1-Image-Handling/notebooks/image_handling.ipynb)

### Module 2: Basic Image Manipulation

- **Accessing** & **Modifying** image pixels
- **Crop** & **Resize** & **Flipping** images
- **cv2**: `resize()` `flip()`

  - File: [image_manipulation.ipynb](2-Image-Manipulation/notebooks/image_manipulation.ipynb)

### Module 3: Image Annotation

- **Annotating** images
- Drawing **line**, **circle**, **rectangle** & Putting **text** on images
- **cv2**: `line()` `circle()` `rectangle()` `putText()`

  - File: [image_annotation.ipynb](3-Image-Annotation/notebooks/image_annotation.ipynb)

### Module 4: Image Enhancement

- **Brightness** & **Contrast** & **Image Thresholding**
- Difference between **Global** and **Adaptive thresholding**
- Thresholding Types: **THRESH_BINARY**, **THRESH_BINARY_INV**, **THRESH_TRUNC** etc.
- Bitwise operations: **AND**, **OR**, **XOR**, **NOT**
- Applying **Mask** on the background
- Creating and type casting **numpy arrays**
- **cv2**: `add()` `subtract()` `multiply()` `threshold()` `adaptiveThreshold()` `bitwise_and()` `bitwise_or()` `bitwise_xor()` `bitwise_not()`

  - File: [image_enhancement.ipynb](4-Image-Enhancement/notebooks/image_enhancement.ipynb)

### Module 5: Accessing and Writing to Camera

- **Accessing** to camera and **Writing video** as **mp4**
- **cv2**: `VideoCapture()` `VideoWriter()`

  - File: [camera.py](5-Access-Write-Camera/camera.py)

### Module 6: Image Filtering and Edge Detection

- Opening camera via **VideoCapture** and using keyboard to apply different **filters** and **detection functions**
- **Edge** & **Corner** & **Filter (Kernel)** term explanations
- **Gaussian Blur** & **Edge Detection** & **Corner Detection** (Shi-Tomasi)
- **cv2**: `blur()` `GaussianBlur()` `Canny()` `goodFeaturesToTrack()`

  - File: [detection.py](6-Image-Filtering-and-Edge-Detection/detection.py)

### Module 7: Image Features and Alignment

- Goal is **warping** scanned image to make it look as original reference image (basically align them)
- Using **Feature-based matching** (ORB) and **Homography** (a 3×3 transformation matrix that maps points from one perspective to another)
- **KeyPoint** & **Descriptor** & **Matching**
- **Use cases**: Document alignment & scanning, Panorama stitching, Augmented Reality (placing virtual objects correctly) etc.
- **cv2**: `ORB_create()` `orb.detectAndCompute()` `drawKeypointss()` `DescriptorMatcher_create()` `drawMatches()` `findHomography()` `warpPerspective()`

  - File: [image_features_alignment.ipynb](7-Image-Features-and-Alignment/notebooks/image_features_alignment.ipynb)

### Module 8: Panorama

- Image allignment and creating **panorama** image
- **cv2**: `Stitcher_create()` `stitcher.stitch`

  - File: [panorama.ipynb](8-Panorama/notebooks/panorama.ipynb)

### Module 9: HDR

- Idea of **HDR** Images
- **MTB - Median Threshold Bitmap** (compute the median pixel intensity)
- **cv2**: `createAlignMTB()` `alignMTB.process()` `createCalibrateDebevec()` `calibrate_debevec.process()` `createMergeDebevec()` `createTonemapDrago()` `createTonemapReinhard()` `createTonemapMantiuk()`

  - File: [hdr.ipynb](9-HDR/notebooks/hdr.ipynb)

### Module 10: Object Tracking

- **Object Detection** vs **Object Tracking**
- **Object Tracking** steps & differences on **Deep learning-based models** 
- Tracking libraries like **GOTURN**, **MIL**, **Nano**, **Vit**, **mean shift** etc.
- **Appearance Model** & **Motion Model** terms
- **cv2**: `TrackerMIL()` `TrackerGOTURN()` `TrackerNano()` `dnn.readNet()` `TrackerVit()` `getTickCount()` `getTickFrequency()`

  - File: [tracker.py](10-Object-Tracking/tracker.py)
  - Notebook File: [hdr.ipynb](10-Object-Tracking/notebooks/object_tracking.ipynb)
