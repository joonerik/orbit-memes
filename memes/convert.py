from PIL import Image
from os import listdir
from os.path import splitext

target_directory = '.'
target = '.png'

for meme in listdir(target_directory):
    filename, extension = splitext(meme)
    try:
        if extension not in ['.py', target, '']:
            im = Image.open(filename + extension)
            im.save('png/' + filename + target)
    except OSError:
        print('Cannot convert %s' % meme)
