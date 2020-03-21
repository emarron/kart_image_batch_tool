import itertools
import shutil
import sys
from pathlib import Path

from PIL import Image, ImageOps


def check_path(path):
    if not Path(path).exists():
        Path(path).mkdir()
    return Path(path)


def copytree(source, destination):
    shutil.rmtree(destination)
    shutil.copytree(source, destination, ignore=ignore_list)


# sys.agrv is the folder selected
folder = sys.argv[1]
images = check_path('./' + folder)
images_rgb = check_path('./' + folder + '_rgb')
images_alpha = check_path('./' + folder + '_alpha')
images_merged = check_path('./' + folder + '_merged')

extensions = ['png', 'tga', 'jpg', 'dds']
ignore_list = shutil.ignore_patterns(*['*.' + extension for extension in extensions])
globs = [images.glob(f'**/*.{extension}') for extension in extensions]

if sys.argv[2] == 'split':
    copytree(images, images_alpha)
    copytree(images, images_rgb)
    for file in itertools.chain.from_iterable(globs):
        try:
            image = Image.open(file)
            image.convert('RGB').save(
                str(images_rgb) + '/' + '/'.join(file.parts[1:-1]) + '/' + str(file.stem) + '.png')
            try:
                alpha = image.getchannel('A')
                alpha.save(str(images_alpha) + '/' + '/'.join(file.parts[1:-1]) + '/' + str(file.stem) + '.png')
            except ValueError:
                pass
        except ValueError:
            pass
if sys.argv[2] == 'merge':
    copytree(images, images_merged)
    for file in images_rgb.glob('**/*.png'):
        try:
            alpha = Image.open(str(images_alpha) + '/' + '/'.join(file.parts[1:-1]) + '/' + str(file.name))
            alpha = ImageOps.grayscale(alpha)
            image = Image.open(file)
            out = Image.new("RGBA", image.size, (255, 255, 255, 255))
            out.paste(image)
            out.putalpha(alpha)
            try:
                out.save(str(images_merged) + '/' + '/'.join(file.parts[1:-1]) + '/' + str(file.stem) + '.' + sys.argv[3])
            except IndexError:
                out.save(str(images_merged) + '/' + '/'.join(file.parts[1:-1]) + '/' + str(file.stem)+ '.tga')
        except FileNotFoundError:
            out = Image.open(file)
            out.save(str(images_merged) + '/' + '/'.join(file.parts[1:-1]) + '/' + str(file.name))

