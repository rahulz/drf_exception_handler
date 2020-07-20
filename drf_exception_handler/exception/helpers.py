import six

try:
    import http.client as httplib
except ImportError:
    import httplib

from django.conf import settings
from django.db import OperationalError
from rest_framework.response import Response

from .exc_parse import get_deep_text, simple_hash_code

from ..models import ErrorHash


def error_response(data, display_text=None, error_code=None, exc_type='Exception', extra_data=None,
                   http_status=httplib.INTERNAL_SERVER_ERROR):
    if extra_data is None:
        extra_data = {}
    if not display_text:
        display_text = get_deep_text(data)
    if not error_code:
        error_code = simple_hash_code(get_deep_text(data))
    err = {
        'message': six.text_type(display_text),
        'status_code': error_code,
        'data': extra_data
    }

    err['debug_data'] = data,
    err['debug_type'] = exc_type

    return Response(err, http_status)
