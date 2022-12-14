<h1> Image Resize Bicubic Interpolation </h1>
Image resizing is a crucial concept that wishes to augment or reduce the number of pixels in a picture. Applications of image resizing can occur under a wider form of scenarios: transliteration of the image, correcting for lens distortion, changing perspective, and rotating a picture. The results of resizing greatly vary looking on the kind of interpolation algorithm used.
<h2>What is Interpolation?</h2>
Interpolation works by using known data to estimate values at unknown points. For example: if you wanted to understand the pixel intensity of a picture at a selected location within the grid (say coordinate (x, y), but only (x-1,y-1) and (x+1,y+1) are known, you’ll estimate the value at (x, y) using linear interpolation. The greater the quantity of already known values, the higher would be the accuracy of the estimated pixel value.
<h2>Interpolation Algorithms</h2>
Different interpolation algorithms include the nearest neighbor, bilinear, bicubic, and others. Betting on their complexity, these use anywhere from 0 to 256 (or more) adjacent pixels when interpolating. The accuracy of those algorithms is increased significantly by increasing the number of neighboring pixels considered while evaluation of the new pixel value. Interpolation algorithms are predominantly used for resizing and distorting a high-resolution image to an occasional resolution image. There are various interpolation algorithms one of them is Bicubic Interpolation.
<h2>Bicubic Interpolation</h2>
In addition to going 2×2 neighborhood of known pixel values, Bicubic goes one step beyond bilinear by considering the closest 4×4 neighborhood of known pixels — for a complete of 16 pixels. The pixels that are closer to the one that’s to be estimated are given higher weights as compared to those that are further away. Therefore, the farthest pixels have the smallest amount of weight. The results of Bicubic interpolation are far better as compared to NN or bilinear algorithms. This can be because a greater number of known pixel values are considered while estimating the desired value.



Document Reference
https://www.geeksforgeeks.org/python-opencv-bicubic-interpolation-for-resizing-image/
