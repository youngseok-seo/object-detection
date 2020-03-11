# Object Detection and Location using OpenCV

### Template matching

Create a template from a sample image, which will be used to locate the object later.

Scale the images over a range to allow for accurate detection.

`multiScaleTemplate.py` produces a copy of the original image with a red bounding box around the detected object (`redbox.png`).

### Thresholding

Using `redbox.png`, create a color threshold for the red bounding box. 

`threshold.py` generates a binary image with the box now in white and the background in black (`whitebox.png`).

