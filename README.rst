=====================
drf_exception_handler
=====================

A custom exception handler for django rest framework. 

Based on raised exception this exception handler will set appropriate http response status and will format exception as readable json for easy debugging. Debug data will be dropped once you set `DEBUG=False`. 


Quick start
-----------

1. Installation::

   python setup.py install

2. Add "drf_exception_handler" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'drf_exception_handler',
    ]

3. Run migrations

    python manage.py migrate drf_exception_handler
    
4. Set `drf_exception_handler.views.exception_handler` as your `EXCEPTION_HANDLER` setting like this::

    REST_FRAMEWORK = {
        ...
        'EXCEPTION_HANDLER': 'drf_exception_handler.views.exception_handler'

    }

5. Optional: Configure http response status::

    DRF_STATUS_CODE_MAP = {"rest_framework.exceptions.NotAuthenticated": 401}

Example response::
    
    Status: 401 Unauthorized
    {
        "status_code": 100454,
        "debug_data": [
            {
                "detail": "Authentication credentials were not provided."
            }
        ],
        "message": "Authentication credentials were not provided.",
        "data": {},
        "debug_type": "rest_framework.exceptions.NotAuthenticated"
    }
    
