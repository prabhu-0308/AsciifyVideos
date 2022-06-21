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
         First, we extract all the frames from the input video by using cv2.videoCapture() to capture the video and 
    VideoCaptureObject.read() to separate each frame and store it in InputImages folder. we also notedown fps of video 
    by using videoCaptureObject.get() function and total number of frames.
         Now we go through each frame of the video, and in each frame we go through pixel by pixel and map each of 
    pixel with a suitable ascii character. We also colour the suitable ascii character with the average color of the 
    pixel and then finally write this character onto output image. we store all these output images in one folder.
         Finally, we write each frame onto the video using video.write() function and then release the "final_video.mp4" 
    by using video.release().

## Learning takeaways from the project
        I have learnt about a lot of very useful python libraries like PIL (Image, ImageOps, ImageDraw, ImageFont), 
    opencv, numpy etc while working on the project. I have learnt how to manipulate and process images and videos using 
    PIL and OpenCV libraries. I have also learnt to work with numpy arrays.
        By Doing this project, I have also learnt that the best way to learn any technical thing is utility based learning
    i.e get good grasp on things that are required for the project first and then expand your knowledge gradually by doing 
    more projects in the future as opposed to trying to learn everything about it in the beginning itself.
    
## References 

- [learnopencv.com](https://learnopencv.com/)
- [https://www.instructables.com/Turn-Videos-Into-ASCII-Art-Videos/](https://www.instructables.com/Turn-Videos-Into-ASCII-Art-Videos/)
- [https://www.geeksforgeeks.org/](https://www.geeksforgeeks.org/) for learning about specific library functions
- [Wiki article on ASCII Art and Images.](https://en.wikipedia.org/wiki/ASCII_art#Types_and_styles)
- [How digital images are stored in a computer.](https://alekya3.medium.com/how-images-are-stored-in-a-computer-f364d11b4e93)


## Results
    Both original video and asciified video are submitted in files section.
    
    OriginalVideo: cars.mp4
    AsciifiedVideo: final_video.mp4

