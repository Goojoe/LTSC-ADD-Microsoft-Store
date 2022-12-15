py setup.py sdist bdist_wheel
py setup.py check
py -m twine upload --repository pypi dist/* --verbose