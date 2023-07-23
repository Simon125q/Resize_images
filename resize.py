from PIL import Image
import os

RESIZE_FACTOR = 2

path_in = 'c:/Users/szomi/Dropbox/Komputer/Desktop/NinjaAdventure'
path_out = 'c:/Users/szomi/Dropbox/Komputer/Desktop/graphics/32x32'

for path, dir_names, file_names in os.walk(path_in):
    if not os.path.isdir(path.replace(path_in, path_out)):
                os.mkdir(path.replace(path_in, path_out))
    for file in file_names:
        if file[-4:] == '.png':
            p = path
            image = Image.open(path + '/' + file)
            p = p.replace(path_in, path_out)
            p = p.replace('\\', '/')
            p = p.strip()
            width, height = image.size
            new_size = (width * RESIZE_FACTOR, height * RESIZE_FACTOR)
            resized_image = image.resize(new_size, resample = 0)
            
            p = p + '/' + file
            resized_image.save(p)