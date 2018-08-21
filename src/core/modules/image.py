from os import path
from base64 import b64decode
import time

from PIL import Image

from django.core.files.base import ContentFile

def create_image_from_b64(data, name='', file_path=None):
    """
    :param data: Data for writing to file
    :param name: File name
    :param file_path: File path
    :return: file
    """
    if 'data:' in data and ';base64,' in data:
        img_format, data = data.split(';base64,')
        ext = img_format.split('/')[-1]

    image = b64decode(data)
    file_name = '%s_%d.%s' % (name, int(time.time()), ext)
    if file_path:
        file_name = path.join(file_path, file_name)
    return ContentFile(image, name=file_name)


def box_params_center(width, height):
    """
    Calculate the box parameters for cropping the center of an image based
    on the image width and image height
    :param width: int
    :param height: int
    """
    is_landscape = width >= height
    if is_landscape:
        upper_x = int((width / 2) - (height / 2))
        upper_y = 0
        lower_x = int((width / 2) + (height / 2))
        lower_y = height
        return upper_x, upper_y, lower_x, lower_y
    else:
        upper_x = 0
        upper_y = int((height / 2) - (width / 2))
        lower_x = width
        lower_y = int((height / 2) + (width / 2))
        return upper_x, upper_y, lower_x, lower_y


def crop_it(img, size):
    """
    :param img: Image to crop
    :param size: Size to crop image to
    :return: Image cropped image
    """
    width, height = img.size
    upper_x, upper_y, lower_x, lower_y = box_params_center(width, height)
    box = (upper_x, upper_y, lower_x, lower_y)
    region = img.crop(box)
    return region.resize(size, Image.ANTIALIAS)
