from PIL import Image
import os

RESIZE_FACTOR = 2

path_in = 'C:/Users/szomi/Dropbox/Komputer/Desktop/NinjaAdventure'
path_out = 'C:/Users/szomi/Dropbox/Komputer/Desktop/graphics/32x32'

for path, dir_names, file_names in os.walk(path_out):
    for file in file_names:
        if file[-4:] == '.png': #and file[0] == "C":
            print(path.replace(path_in, path_out))
            # image = Image.open(path + '/' + file)
            # width, height = image.size
            # new_size = (width * RESIZE_FACTOR, height * RESIZE_FACTOR)
            # resized_image = image.resize(new_size, resample = 0)

            #resized_image.save(path_out + path.replace)