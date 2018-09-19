import six
from django.conf import settings
from rest_framework.views import exception_handler

from drf_exception_handler.exception.exc_parse import get_class_name
from drf_exception_handler.exception.helpers import error_response

try:
    import http.client as httplib
except ImportError:
    import httplib

if hasattr(settings, "DRF_STATUS_CODE_MAP"):
    HTTP_STATUS_MAP = settings.DRF_STATUS_CODE_MAP
else:
    HTTP_STATUS_MAP = {}


def handler(exc, context):
    response = exception_handler(exc, context)
    exc_type = get_class_name(exc)

    if response:
        data = response.data
        http_status = response.status_code
    else:
        try:
            data = exc.message or six.text_type(exc)
        except AttributeError:
            data = six.text_type(exc)
        try:
            http_status = HTTP_STATUS_MAP[exc_type]
        except KeyError:
            http_status = httplib.INTERNAL_SERVER_ERROR

    return error_response(**{
        "data": data,
        "exc_type": exc_type,
        "http_status": http_status
    })
