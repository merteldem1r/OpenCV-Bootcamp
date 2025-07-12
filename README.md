## OpenCV Bootcamp

OpenCV course to manipulate images and videos, and detect objects and faces, among other exciting topics.

- **Course**: [OpenCV University](https://opencv.org/university/)
- **Implemented by**: [Mert Eldemir](https://github.com/merteldem1r)

**NOTE**: To manipulate code and see the results first download the respective images and documents. On each moduel folder run the `download_assets.py` script

### Module 1: Getting Started With Images

- Reading & Display images using **opencv** and **matplotlib**
- Representing images as **numpy arrays** & **RGB** & **HSV** format images
- **cv2**: `imread()` `imwrite()` `cvtColor()` `split()` `merge()`
- **matplotlib**: `imshow()` `figure()` `subplot()`

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
