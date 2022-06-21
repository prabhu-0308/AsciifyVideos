**Asciify Videos : ASCII Video Art Generator**
===


## PROJECT'S DESCRIPTION: 
           This Project "Asciify Videos" will take a video file as an input, and then it will asciify each frame of the
    video i.e replace each pixel of the frame with a suitable coloured ascii character and finally returns the Asciified 
    version of original video as the output.


## How to run the project:
    We will be needing the following libraries
        1. PIL (Image, ImageOps, ImageDraw, ImageFont)
        2. Opencv (cv2)
        3. numpy 
        4. os

    Steps to run the program:
        1. For giving the video of your choice as an input, give the absolute path of the video as an argument inside the 
    main(absolute_video_path). 
        2. Now, just run the asciify_videos.py and the output file "final_video.mp4" will automatically be created in 
    the projects directory.

## Internal Working of the project:
        1. First, we extract all the frames from the input video ( By calling video_to_images() 
    function).  

## Learning takeaways from the project
        I have learnt about a lot of very useful python libraries like PIL (Image, ImageOps, ImageDraw, ImageFont), 
    opencv, numpy etc while working on the project. I have learnt how to manipulate and process image and 
## Resources Used 
**Timeline**
---
- **Week 1 : 28 May - 3 June** 
    - Introduction to the problem at hand
    - Basics of image processing
    - Working with images and turning them into grayscale


- **Week 2 : 4 June - 10 June** 
    - Implementing the algorithm. 
    - Get comfortable with the libraries/frameworks required for working with images
    - Sampling, scaling and transforming images to map pixels to their desired characters

- **Week 3 : 11 June - 17 June** 
    - Handling Image Aspect Ratio
    - Adding additional features to your program:
        - Turn your ASCII art into a pencil sketch
        - Modify the generated image, .. change it's style etc.
        - Asciify videos!

### Resources and Suggested Readings


- [Wiki article on ASCII Art and Images.](https://en.wikipedia.org/wiki/ASCII_art#Types_and_styles)
- [How digital images are stored in a computer.](https://alekya3.medium.com/how-images-are-stored-in-a-computer-f364d11b4e93)
- [Another one regarding digital images](
https://www.analyticsvidhya.com/blog/2021/03/grayscale-and-rgb-format-for-storing-images/)
- \[Chapter 3] - "Raster Images", Fundamentals of Computer Graphics, Fourth Edition by Steve Marschner & Peter Shirley.

**Goal**
---
Convert images(jpg/png) to ASCII encoded strings, that look like the image.

Here's an example : 

![](https://i.imgur.com/fJsEVJi.png)