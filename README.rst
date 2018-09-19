=====
drf_exception_handler
=====

A custom exception handler for django rest framework

Quick start
-----------

1. Add "drf_exception_handler" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'drf_exception_handler',
    ]

1. Set "drf_exception_handler.views.exception_handler" as your EXCEPTION_HANDLER setting like this::

    REST_FRAMEWORK = {
        ...
        'EXCEPTION_HANDLER': 'drf_exception_handler.views.exception_handler'

}

