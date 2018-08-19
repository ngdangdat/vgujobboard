from os import path
from base64 import b64decode
import time

from django.core.files.base import ContentFile
from django.conf import settings

CDN = settings.CDN
PROFILE_AVATAR_KEY = 'profile.avatar'

def get_cdn_url(file_path, cdn_type='DEFAULT'):
    """
    :param file_path: str
    :param type: str
    :return: url
    """
    cdn = CDN.get(cdn_type, None) or CDN.get('DEFAULT')
    return '%s%s' % (cdn, file_path)

def get_storage_path(*args):
    """
    Get storage path
    :param args: external path
    :return str:
    """
    storage_dir = settings.MEDIA_ROOT
    if not path.isabs(storage_dir):
        storage_dir = path.join(settings.BASE_DIR, storage_dir)
    if args:
        args = (storage_dir, ) + args
        storage_dir = path.join(*args)
    return storage_dir

def create_image_file(data, name=PROFILE_AVATAR_KEY, file_path=None):
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
