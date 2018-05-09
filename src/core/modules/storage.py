from os import path

from django.conf import settings

CDN = settings.CDN

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
