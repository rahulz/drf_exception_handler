import hashlib
import itertools

import six


def xstr(str_):
    try:
        if str_:
            if ':thisfieldisrequired.' in str_.replace(' ', '').lower():
                str_ = str_.replace(':This field', '')
            return replace_map(str_.replace('_', ' ').capitalize())
        else:
            return ""
    except TypeError:
        return six.text_type(str_)


def replace_map(s):
    key_map = {'Dob': 'DOB'}
    for key in key_map.keys():
        s = s.replace(key, key_map[key])
    return s


def get_deep_text(data, key=None):
    """
    Scans through dict/iterable and returns first found string

    """
    if isinstance(data, dict):
        key = next(iter(data.keys()))
        return get_deep_text(data[key], key)
    else:
        try:
            if isinstance(data, six.string_types) or data.__class__.__name__ == '__proxy__':
                raise TypeError()
            return get_deep_text(next(iter(data)), key)
        except TypeError:
            if key not in ['non_field_errors', 'detail', None]:
                return xstr('%s:%s' % (key, data))
            return xstr(data)


def simple_hash_code(s):
    """
    Creates simple hash code for a given string
    str => int
    purpose: error_msg==>error_code
    """
    a = str(int(hashlib.sha1(s.encode()).hexdigest(), 16))
    return sum([(i * int(p)) for p, i in itertools.zip_longest(a, range(1, len(a) + 1))])


def get_class_name(obj):
    """ Returns full class name for given object"""
    return str(obj.__class__).replace('<class \'', '').replace('\'>', '')
