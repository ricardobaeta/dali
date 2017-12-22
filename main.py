#
#
# {d}ali
#
# Understanding and applying Gestalt Laws of Perceptual Organization
#
#
# importing "things" (at this point I maybe importing "things" I dont need)
from PIL import Image
from PIL import ImageOps
import glob
import os
from pathlib import Path
import sys
import PIL
import cv2
import numpy as np

# MODULE ONE
# here we lazily find all circle images from images folder by its name
# here i would like to further improve and have a way for the program to analyse the images, recognize its circle shape and group them
all_circles = list(sorted(glob.glob('images/circle*')))

# here we lazily find all triangle images from images folder by its name
# here i would like to further improve and have a way for the program to analyse the images, recognize its triangle shape and group them
all_triangles = list(sorted(glob.glob('images/triangle*')))

# here we lazily find all square images from images folder by its name
# i would like to further improve and have a way for the program to analyse the images, recognize its square shape and group them
all_squares = list(sorted(glob.glob('images/square*')))

# MODULE TWO
# here is the circles images composition, really lazily though
# here I would like for the program to retreive all recognized circle images paths
# the main objective is to group similar shapes and create an image composition with a vertical alignment
list_circles = all_circles
imgs_circles = [ PIL.Image.open(i) for i in list_circles ]

# here I pick the image which is the smallest, and resize the others to match it
min_shape_circles = sorted( [(np.sum(i.size), i.size ) for i in imgs_circles])[0][1]
   
# here I'm doing a vertical stacking composition in its simple way, using vstack
imgs_comb_circles = np.vstack( (np.asarray( i.resize(min_shape_circles) ) for i in imgs_circles ) )
imgs_comb_circles = PIL.Image.fromarray( imgs_comb_circles)

# here I'm saving the vertical composition of all the circle images
imgs_comb_circles.save( 'circles.png', 'PNG' )

# here I confirm if the circle composition image was created
circle_compostion_file = Path("circles.png")
if circle_compostion_file.is_file():
	print("Circles composition ready!")
       
# here is the triangles images composition, really lazily though
# here I would like for the program to retreive all recognized triangle images paths
# the main objective is to group similar shapes and create an image composition with a vertical alignment
list_triangles = all_triangles
imgs_triangles = [ PIL.Image.open(i) for i in list_triangles ]

# here I pick the image which is the smallest, and resize the others to match it
min_shape_triangles = sorted( [(np.sum(i.size), i.size ) for i in imgs_triangles])[0][1]
   
# here I'm doing a vertical stacking composition in its simple way, using vstack
imgs_comb_triangles = np.vstack( (np.asarray( i.resize(min_shape_triangles) ) for i in imgs_triangles ) )
imgs_comb_triangles = PIL.Image.fromarray( imgs_comb_triangles)

# here I'm saving the vertical composition of all the triangle images
imgs_comb_triangles.save( 'triangles.png', 'PNG' )

# here I confirm if the triangle composition image was created
triangle_compostion_file = Path("triangles.png")
if triangle_compostion_file.is_file():
	print("Triangles composition ready!")

# here is the squares images composition, really lazily though
# here I would like for the program to retreive all recognized quare images paths
# the main objective is to group similar shapes and create an image composition with a vertical alignment
list_squares = all_squares
imgs_squares = [ PIL.Image.open(i) for i in list_squares ]

# here I pick the image which is the smallest, and resize the others to match it
min_shape_squares = sorted( [(np.sum(i.size), i.size ) for i in imgs_squares])[0][1]
   
# here I'm doing a vertical stacking composition in its simple way, using vstack
imgs_comb_squares = np.vstack( (np.asarray( i.resize(min_shape_squares) ) for i in imgs_squares ) )
imgs_comb_squares = PIL.Image.fromarray( imgs_comb_squares)

# here I'm saving the vertical composition of all the squares images
imgs_comb_squares.save( 'squares.png', 'PNG' )

# here I confirm if the square composition image was created
square_compostion_file = Path("squares.png")
if triangle_compostion_file.is_file():
	print("Squares composition ready!")	

# MODULE THREE
# here I combine the circles compostion image, the triangles compostion image, and the squares composition image
list_im_composition = ['circles.png', 'triangles.png', 'squares.png' ]
imgs_composition    = [ PIL.Image.open(i) for i in list_im_composition ]

# here I pick the image which is the smallest, and resize the others to match it
min_shape_composition = sorted( [(np.sum(i.size), i.size ) for i in imgs_composition])[0][1]

# here I'm doing a horizontal stacking composition in its simple way, using hstack
imgs_comb_composition = np.hstack( (np.asarray( i.resize(min_shape_composition) ) for i in imgs_composition ) )

# here I'm saving the horizontal composition of the triangle, circle vertical compositions and square vertical composition
imgs_comb_composition = PIL.Image.fromarray( imgs_comb_composition)
imgs_comb_composition.save( 'composition.png', 'PNG' )

# here I confirm if the horizontal composition image of the triangle, circle and square vertical compositions was created
imgs_comb_composition_file = Path("composition.png")
if triangle_compostion_file.is_file():
	print("Circles, Triangles and Squares composition ready!")

# here I'm adding some positive space around the image for the sake of sake
final_img = Image.open('composition.png')
final_img_with_border = ImageOps.expand(final_img,border=200,fill='white')
final_img_with_border.save('final-image.png', 'PNG')

# here I confirm if the final imgae with border was created
final_composition_with_border = Path("final-image.png")
if final_composition_with_border.is_file():
	print("Final composition ready!")

# here I show the result of all the compositions
final_img_with_border.show('final-image.png', 'PNG')


