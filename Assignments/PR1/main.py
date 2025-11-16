###############################################################################
#
#  Author:           Rykir Evans & Victoria Heredia
#  Email:            rjevans0408@my.msutexas.edu | vdheredia1128@my.msutexas.edu
#  Title:            Python is Awesome - Pillow Library
#  Course:           CMPS 4143 Java and Python
#  Professor:        Dr. Tina Johnson
#  Semester:         Fall 2025
#
#  Description:
#         This program exhibits the numerous functions of the Python PIL/pillow
#         library, with this particular snippet focusing on orientation,
#         brightness, and contrast using images of real scenes from the San
#         Diego Balboa Park Botanical Gardens.
#         
#  Usage:
#         To use this program, ensure the files within the directory are
#         saved with proper names, or alter the `.open()` commands to open
#         other specified files. The exhibition style of this snippet is not
#         designed to be extremely customizable, so all changes must occur 
#         within the code.
#         
#         
#  Files: 
#         main.py
#         SD25_Botanical1.JPG
#         SD25_Botanical1_Rotated1.JPG
#         SD25_Botanical1_Rotated2.JPG
#         SD25_Botanical1_Bright.JPG
#         SD25_Botanical_Dim.JPG
#
#         SD25_Botanical2.JPG
#         SD25_Botanical2_HighCon.JPG
#         SD25_Botanical2_LowCon.JPG
###############################################################################

from PIL import Image, ImageEnhance, ImageOps

img = Image.open("SD25_Botanical1.JPG")

##############################
## Orientation Manipulation ##
##############################

# Simple rotation (prone to data loss)
rotated = img.rotate(270)

rotated.save("SD25_Botanical1_Rotated1.JPG")

# Transpose rotation (produces correct results)

rotated = img.transpose(Image.ROTATE_270)

rotated.save("SD25_Botanical1_Rotated2.JPG")

#############################
## Brightness Manipulation ##
#############################

# Brightness enhancement object
img = Image.open("SD25_Botanical1_Rotated2.JPG")
br_enhancer = ImageEnhance.Brightness(img)

# Convert brightness to 65%
dimImage = br_enhancer.enhance(0.65)
dimImage.save("SD25_Botanical1_Dim.JPG")

# Convert brightness to 135%
brightImage = br_enhancer.enhance(1.35)
brightImage.save("SD25_Botanical1_Bright.JPG")

###########################
## Contrast Manipulation ##
###########################
img = Image.open("SD25_Botanical2.JPG")
img = ImageOps.exif_transpose(img) # Needed because original stored image was externally rotated

con_enhancer = ImageEnhance.Contrast(img)

# Increase contrast (1.0 = original)
higher_contrast = con_enhancer.enhance(1.2)   # 20% more contrast
higher_contrast.save("SD25_Botanical2_HighCon.JPG")

# Decrease contrast
lower_contrast = con_enhancer.enhance(0.8)    # 20% less contrast
lower_contrast.save("SD25_Botanical2_LowCon.JPG")



