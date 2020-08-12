Try installing the packages like so::

    pip install -i https://test.pypi.org/simple/ --no-deps funcx-endpoint-tando-test==0.0.1a1
    pip install -i https://test.pypi.org/simple/ --no-deps funcx-sdk-tando-test==0.0.1a1

Then you should be able to import them::

    import funcx.sdk
    import funcx.endpoint
    import funcx.executor
