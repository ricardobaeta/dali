#
#
# {d}ali
#
# Understanding and applying Gestalt Laws of Perceptual Organization
#
#

# First things first.

from PIL import Image, ImageDraw, ImageFont
from PIL import ImageOps
import glob
import os
from pathlib import Path
import sys
import PIL
import cv2
import imutils
import numpy as np
import sys
import shutil

# ~~~~~~~~~~
# MODULE ONE
# ~~~~~~~~~~
#
# On this Module, we want to analyse all images, and get from them their shape and filename. Secondly, we want to properly store this data to enable the manipulation we need.
# While researching for a solution to recognise images shapes, I found an amazing project called OpenCV shape detection - https://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/
# I had a ball adapting it for my purposes, with the best of my intentions. A big shoutout to PyImageSearch and their amazing work.

# For a start, we need to set these ones in advance, semantically self-explanatory. We'll need them later on.
total_triangles_count = 0
total_squares_count = 0
total_circles_count = 0
triangle_shapes = []
square_shapes = []
circle_shapes = []

# Here is created a list, containing the filename for each identical identified shapes.
def image_meta_list(shape_list, image, count):
    list_shape_name = shape_list
    shape_list.append(image)
    # I want to extract the list, once it adds the last shape value. For now, I'm limiting it to what I know is the ammount of identical shapes, which is pretty much naive.
    if count == 3:
        global shape_values
        shape_values = list()
        shape_values.extend(shape_list)
        list_shape_name = shape_values
    
    return list_shape_name      

# Here's the main analysis function, that recognises the shape on each image, count the similatiry and diversity, and group them by unique shape.
# creating a list with each one's filename.
def recognize_shape_count_and_list(image):
    
    # Defining some variables as global so that their value is bound with the ones we defined before.
    global total_triangles_count
    global total_squares_count
    global total_circles_count
    global triangle_shapes
    global square_shapes
    global circle_shapes

    # Bellow it's the adapted code from OpenCV shape detection.
    
    # PyImageSearch
    # load the image and resize it to a smaller factor so that the shapes can be approximated better.
    img = cv2.imread(image)
    img_name = str(image)
    resized = imutils.resize(img, width=300)
    ratio = img.shape[0] / float(resized.shape[0])

    # As of now, I only get good results when running the analysys on low-brightness background images with vibrant coloured shapes.
    # Is my intention to digg deeper into this, to broaden the diversity of possible analysable images.
    # I'm quite sure PyImageSearch works like a charm, and I'm the one to blame :) I'll get there soon(ish).

    # PyImageSearch
    # convert the resized image to grayscale, blur it slightly, and threshold it.
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

    # PyImageSearch
    # Find contours in the thresholded image
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0]

    # Now we want to start to run the analysis over all the images inside the images directory.   

    # PyImageSearch
    # Loop over the contours.
    for c in cnts:

        # PyImageSearch
        # Initialize the shape name and approximate the contour.
        shape = "unidentified"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
                
        # PyImageSearch 
        # If the shape is a triangle, it will have 3 vertices.
        if len(approx) == 3:
            shape = "triangle"
            total_triangles_count += 1
            # Here I'm creating a list with all the triangle images filename.
            triangle_shapes = image_meta_list(triangle_shapes, img_name, total_triangles_count)
        # If the shape has 4 vertices, it is a square.
        elif len(approx) == 4:  
            shape = "square"
            total_squares_count += 1
            # Here I'm creating a list with all the square images filename.
            square_shapes = image_meta_list(square_shapes, img_name, total_squares_count)
        # Otherwise, we assume the shape is a circle.
        else:
            shape = "circle"
            total_circles_count += 1
            # Here I'm creating a list with all the circle images filename.
            circle_shapes = image_meta_list(circle_shapes, img_name, total_circles_count)

        # PyImageSearch    
        # Return the name of the shape
        return shape    

# These are the final, and intended operations of Module One.
# Here I create a list with all the images in the directory, to be able to loop on them. 
all_images = list(sorted(glob.glob('images/*.png')))
# Here, and at this moment, it's useful to count all the images. This information will be used while writing the Content later on.
number_files = len(all_images)

# Here's the loop that will trigger images shape recognition, counting and listing function across all images.
for image in all_images:
    recognize_shape_count_and_list(image)

# ~~~~~~~~~~     
# MODULE TWO
# ~~~~~~~~~~
#
# On this module, the main objective is to group similar shapes and create an image composition of each shape, doing a vertical alignment on them.

# Here, all identical shapes images filenames list - from Module One - are attributed to a new variable. 
list_circles = circle_shapes
list_triangles = triangle_shapes
list_squares = square_shapes

# Here, we're getting the three shapes lists ready, for proper upcoming manipulation.
imgs_circles = [ PIL.Image.open(i) for i in list_circles ]
imgs_triangles = [ PIL.Image.open(i) for i in list_triangles ]
imgs_squares = [ PIL.Image.open(i) for i in list_squares ]

# Here I pick each shape image which is the smallest, and resize the others to match them.
min_shape_circles = sorted( [(np.sum(i.size), i.size ) for i in imgs_circles])[0][1]
min_shape_triangles = sorted( [(np.sum(i.size), i.size ) for i in imgs_triangles])[0][1]
min_shape_squares = sorted( [(np.sum(i.size), i.size ) for i in imgs_squares])[0][1]

# Here I'm doing the vertical stacking composition of each idential shape in its simple way, using vstack.
imgs_comb_circles = np.vstack( tuple(np.asarray( i.resize(min_shape_circles) ) for i in imgs_circles ) )
imgs_comb_circles = PIL.Image.fromarray( imgs_comb_circles )
imgs_comb_triangles = np.vstack( tuple(np.asarray( i.resize(min_shape_triangles) ) for i in imgs_triangles ) )
imgs_comb_triangles = PIL.Image.fromarray( imgs_comb_triangles)
imgs_comb_squares = np.vstack( tuple(np.asarray( i.resize(min_shape_squares) ) for i in imgs_squares ) )
imgs_comb_squares = PIL.Image.fromarray( imgs_comb_squares)

# Here I'm creating a temporary folder to store output assets. 
output_assets_directory = 'output-assets/'
os.mkdir(output_assets_directory)

# Here I'm saving the identical shapes vertical composition images.
imgs_comb_circles.save( 'output-assets/circles.png', 'PNG' )
imgs_comb_triangles.save( 'output-assets/triangles.png', 'PNG' )
imgs_comb_squares.save( 'output-assets/squares.png', 'PNG' )

# ~~~~~~~~~~~~     
# MODULE THREE
# ~~~~~~~~~~~~     
#
#
# here I combine the circles compostion image, the triangles compostion image, and the squares composition image.
list_im_composition = ['output-assets/circles.png', 'output-assets/triangles.png', 'output-assets/squares.png' ]
imgs_composition    = [ PIL.Image.open(i) for i in list_im_composition ]

# here I pick the image which is the smallest, and resize the others to match it.
min_shape_composition = sorted( [(np.sum(i.size), i.size ) for i in imgs_composition])[0][1]

# here I'm doing a horizontal stacking composition in its simple way, using hstack
imgs_comb_composition = np.hstack( tuple(np.asarray( i.resize(min_shape_composition) ) for i in imgs_composition ) )

# here I'm saving the horizontal composition of the triangle, circle vertical compositions and square vertical composition.
imgs_comb_composition = PIL.Image.fromarray( imgs_comb_composition)
imgs_comb_composition.save( 'output-assets/composition.png', 'PNG' )

# here I confirm if the horizontal composition image of the triangle, circle and square vertical compositions was created.
imgs_comb_composition_file = Path("output-assets/composition.png")

# here I'm adding some positive space around the image for the sake of sake.
final_img = Image.open('output-assets/composition.png')
final_img_with_border = ImageOps.expand(final_img,border=200,fill='#1b1b1b')
final_img_with_border.save('output-assets/final-composition.png', 'PNG')

# Here I start to write some Content on the final composition image.
img_with_heading = Image.open('output-assets/final-composition.png')
font = ImageFont.truetype('Arial.ttf', 28)

# I start with the Heading 
analysis_output_heading = ImageDraw.Draw(img_with_heading)
analysis_message_heading = str("COMPOSITION RATIONALE")
analysis_output_heading.text((40,50), analysis_message_heading, font=font, fill=(114, 114, 114))
img_with_heading.save('output-assets/final-image-one.png')

# I move forward to the Description 
img_with_description = Image.open('output-assets/final-image-one.png')
font = ImageFont.truetype('Arial.ttf', 28)
analysis_output = ImageDraw.Draw(img_with_description)
analysis_message = str( str(total_triangles_count) + " triangles, " + str(total_squares_count) + " squares, and " + str(total_circles_count) + " circles recognized, amongst " + str(number_files) + " images analysed.")
analysis_output.text((40,100), analysis_message, font=font, fill=(255, 255, 255))
img_with_description.save('output-assets/final-image-two.png')

# I end up adding a visual anchor artifact, excuse me.
understood_visual_translation = Image.open('output-assets/final-image-two.png') 
ui_basic_artifact = ImageDraw.Draw(understood_visual_translation) 
ui_basic_artifact.line((1720,155, 40,155), fill="#636363")
understood_visual_translation.save('output-assets/outstanding-asset.png')

# Last things first
understood_visual_translation.show('output-assets/outstanding-asset.png', 'PNG')

# Cleaning up after I move out.
shutil.rmtree(output_assets_directory)
