rm -rf build/ dist/ funcx_sdk_tando_test.egg-info/
python3 setup.py sdist bdist_wheel
python3 -m twine upload --repository testpypi dist/*


