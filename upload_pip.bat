rmdir /s /y build
rmdir /s /y dist
rmdir /s /y build
rmdir /s /y ltscaddstore.egg-info
py setup.py sdist bdist_wheel
py setup.py check
py -m twine upload --repository pypi dist/* --verbose