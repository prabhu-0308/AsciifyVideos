import numpy as np
import os
import cv2
import imgkit
from PIL import Image, ImageDraw, ImageOps, ImageFont


def video_to_images(path):
   os.mkdir('InputImages')
   os.mkdir('OutputImages')
   video = cv2.VideoCapture(path)
   fps = video.get(cv2.CAP_PROP_FPS)
   success, image = video.read()
   counter = 1
   while success:
       cv2.imwrite("InputImages/Image{0}.jpg".format(str(counter)), image)
       success, image = video.read()
       counter+=1
   return fps, (counter-1)


def set_mode(mode):
    # font = ImageFont.truetype("fonts/DejaVuSansMono-Bold.ttf", size=20)
    # scale = 1.7

    # these characters are mapped to each pixel of the image based on the luminosity
    ascii_string = {
        "standard": "&@%#*+=-:. ",
        "complex": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    }
    ascii_list = ascii_string[mode]
    return ascii_list


def set_bg_color(bg_color):
    # set Background color as Black or White
    if bg_color == "white":
        bg_code = (255, 255, 255)
    elif bg_color == "black":
        bg_code = (0, 0, 0)
    return bg_code


def get_input_dimensions(input_img):
    return input_img.shape


def get_pixel_dimensions(input_h, input_w, scale):
    # we fix the number of columns, so we get pixel width and
    # from scale and pixel width, we get pixel height
    col_count = 300
    pixel_w = input_w / col_count
    pixel_h = scale * pixel_w
    row_count = int( input_h / pixel_h)
    return col_count, row_count, pixel_h, pixel_w


def get_output_dimensions(row_count, col_count, scale, char_w, char_h):
    output_h = int(scale * char_h * row_count)
    output_w = char_w * col_count
    return output_h, output_w


def main(video_path):
    ascii_list = set_mode("standard")
    bg = "white"
    bg_code = set_bg_color(bg)

    # scale is defined as the ratio of ascii font height and width
    scale = 1.7

    font = ImageFont.truetype("fonts/DejaVuSansMono-Bold.ttf", size=20)
    char_w, char_h = font.getsize("A")

    # calculating total frames of video and also fps to reconstruct output video with same parameters
    fps, number_images = video_to_images(video_path)

    # finding height, width and color compositions of input image
    dummy_img = cv2.imread("InputImages/Image1.jpg")
    input_h, input_w, input_col= get_input_dimensions(dummy_img)

    # finding pixel dimensions and pixel count along rows and columns
    col_count, row_count, pixel_h, pixel_w = get_pixel_dimensions(input_h, input_w, scale)

    # finding output image dimensions from pixel dimensions
    output_h, output_w = get_output_dimensions(row_count, col_count, scale, char_w, char_h)

    for k in range(1,number_images+1):
        # reading input image
        input_img = cv2.imread("InputImages/Image{0}.jpg".format(str(k)))

        # converting the img to 'RGB' type
        input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2RGB)

        # making a new output image with dimensions and back ground color calculated above
        output_img = Image.new("RGB", (output_w, output_h), bg_code)

        # ImageDraw.Draw() method allows us to write ascii chars on the image
        draw = ImageDraw.Draw(output_img)

        # Mapping the Characters
        for i in range(row_count):
            for j in range(col_count):
                pixel_img = input_img[int(i*pixel_h):min(int((i+1)*pixel_h), input_h), int(j*pixel_w):min(int((j+1)*pixel_w), input_w), : ]
                avg_pixel_color = np.sum(np.sum(pixel_img, axis=0), axis=0) / (pixel_h*pixel_w)
                avg_pixel_color = tuple(avg_pixel_color.astype(np.int32).tolist())
                c= ascii_list[min(int(np.mean(pixel_img) * len(ascii_list)/255), len(ascii_list)-1)]
                draw.text( (j * char_w, i * char_h) , c, fill= avg_pixel_color, font=font )

        # Inverting Image and removing excess borders
        if bg == "white":
            cropped_img = ImageOps.invert(output_img).getbbox()
        elif bg == "black":
            cropped_img = output_img.getbbox()

        # Saving the new Image
        output_img = output_img.crop(cropped_img)
        output_img.save("OutputImages/Image{0}.jpg".format(str(k)))

    res = Image.open('OutputImages/Image1.jpg').size
    video = cv2.VideoWriter('final_video.mp4',cv2.VideoWriter_fourcc(*'mp4v'),int(fps),res)

    for j in range(1,number_images+1):
      video.write(cv2.imread('OutputImages/Image{0}.jpg'.format(str(j))))
    video.release()


main("cars.mp4")
