try:
    import importlib.resources as pkg_resources
    read_pkg_text = pkg_resources.read_text
except ImportError:
    import pkg_resources
    read_pkg_text = pkg_resources.resource_string
import xml.etree.ElementTree


class MimeTypeDescription:
    _mime_types = dict()
    _descriptions = dict()

    def __init__(self):
        lang_attr = '{http://www.w3.org/XML/1998/namespace}lang'
        shared_mime_info = '{http://www.freedesktop.org/standards/shared-mime-info}'
        data = read_pkg_text(__package__, 'freedesktop.org.xml')
        root = xml.etree.ElementTree.fromstring(data)

        for mime_type in root:
            _type = mime_type.attrib['type']
            self._descriptions[_type] = dict()

            for child in mime_type:
                _tag = child.tag.replace(shared_mime_info, '')
                if _tag == 'comment':
                    lang = child.attrib[lang_attr] if child.attrib else 'en'
                    self._descriptions[_type][lang] = child.text
                elif _tag == 'glob':
                    ext = child.attrib['pattern'].replace('*.', '')
                    self._mime_types[ext] = _type

    def get_description(self, mime_type, language):
        try:
            return self._descriptions[mime_type][language]
        except KeyError:
            return None

    def get_mime_type(self, filename):
        try:
            return self._mime_types.get(filename.split('.')[-1])
        except IndexError:
            return None


_instance = MimeTypeDescription()


def get_mime_type_description(mime_type, language='en'):
    return _instance.get_description(mime_type, language)


def guess_mime_type(filename):
    return _instance.get_mime_type(filename)


__all__ = ('get_mime_type_description', 'guess_mime_type')
